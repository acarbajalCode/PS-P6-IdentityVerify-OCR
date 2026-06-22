using AForge.Video;
using AForge.Video.DirectShow;
using FaceDocVerifyClient.Modelo;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FaceDocVerifyClient.Vista
{
    public partial class FrmValidacionIdentidad : Form
    {
        private string _jwtToken = "";

        //variables para enviar lo solicitado a Método de Verificación:
        private string _dniFrontPath = "";
        private string _dniBackPath = "";
        private string _selfiePath = "";

        //variables para capturas 
        private FilterInfoCollection videoDevices;
        private VideoCaptureDevice videoSource;
        private Bitmap currentFrame;
        public FrmValidacionIdentidad()
        {
            InitializeComponent();
        }

        //método para Iniciar Web Cam
        private void IniciarCamara()
        {
            videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);

            if (videoDevices.Count == 0)
            {
                MessageBox.Show("No se detectó cámara");
                return;
            }

            videoSource = new VideoCaptureDevice(videoDevices[2].MonikerString);
            videoSource.NewFrame += new NewFrameEventHandler(Video_NewFrame);
            videoSource.Start();
        }

        private void Video_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            Bitmap frame = (Bitmap)eventArgs.Frame.Clone();
            currentFrame = (Bitmap)frame.Clone();

            picCamara.Image = frame;
        }


        private async void btnObtenerToken_Click(object sender, EventArgs e)
        {
            lblEstadoConexion.ForeColor = Color.Red;
            try { 
                lblEstadoConexion.Text = "Conectando...";
                lblEstadoConexion.ForeColor = Color.Orange;
                HttpClient client = new HttpClient(); 
                var loginData = new LoginRequest { username = txtUsuario.Text.Trim(), password = txtPassword.Text.Trim() }; 
                var json = JsonConvert.SerializeObject(loginData); 
                var content = new StringContent(json, Encoding.UTF8, "application/json"); 
                string url = txtApiUrl.Text.Trim() + "/api/v1/login";
                HttpResponseMessage response = await client.PostAsync(url, content); 
                if (!response.IsSuccessStatusCode) { 
                    lblEstadoConexion.Text = "Error autenticando";
                    lblEstadoConexion.ForeColor = Color.Red;
                    MessageBox.Show("Credenciales inválidas", "FaceDocVerify", MessageBoxButtons.OK, MessageBoxIcon.Error); 
                    return; 
                } 
                string responseJson = await response.Content.ReadAsStringAsync(); 
                var loginResponse = JsonConvert.DeserializeObject<LoginResponse>(responseJson); 
                _jwtToken = loginResponse.access_token; 
                lblEstadoConexion.Text = "🟢 Conectado correctamente";
                lblEstadoConexion.ForeColor = Color.Blue;
                txtResultado.Text = _jwtToken;
                MessageBox.Show("Token obtenido correctamente", "FaceDocVerify", MessageBoxButtons.OK, MessageBoxIcon.Information); 
            } catch (Exception ex) 
            { 
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error); 
            }

        }

        private void btnIniciarCamara_Click(object sender, EventArgs e)
        {
            IniciarCamara();
        }

        private void btnTomarFoto_Click(object sender, EventArgs e)
        {


            if (currentFrame == null) return;

            using (Bitmap img = (Bitmap)currentFrame.Clone())
            {
                picSelfieCapturada.Image = new Bitmap(img);

                string tempPath = Path.Combine(Application.StartupPath, "selfie.jpeg");

                img.Save(tempPath, ImageFormat.Jpeg);

                _selfiePath = tempPath;
                txtSelfie.Text = tempPath;
            }
        }

        private void GuardarSelfie(string path)
        {
            if (picSelfieCapturada.Image == null)
                return;

            using (Bitmap bmp = new Bitmap(picSelfieCapturada.Image))
            {
                bmp.Save(path, ImageFormat.Jpeg);
            }
        }

        private void FrmValidacionIdentidad_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (videoSource != null && videoSource.IsRunning)
            {
                videoSource.SignalToStop();
                videoSource.WaitForStop();
            }
        }

        private void btnDniFront_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "Imagen JPG|*.jpg;*.jpeg|PNG|*.png";

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                txtDniFront.Text = ofd.FileName;
                
            }
        }

        private void btnDniBack_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "Imagen JPG|*.jpg;*.jpeg|PNG|*.png";

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                txtDniBack.Text = ofd.FileName;
                
            }
        }

        private async void btnValidar_Click(object sender, EventArgs e)
        {
            try
            {
                btnValidar.Enabled = false;
                btnValidar.Text = "Validando...";

                using (var client = new HttpClient())
                {
                    // =========================
                    // TOKEN JWT
                    // =========================
                    string token = _jwtToken; // o donde lo guardes

                    client.DefaultRequestHeaders.Authorization =
                        new AuthenticationHeaderValue("Bearer", token);

                    // =========================
                    // MULTIPART FORM DATA
                    // =========================
                    var form = new MultipartFormDataContent();

                    // DNI FRONT
                    var frontBytes = File.ReadAllBytes(txtDniFront.Text);
                    var frontContent = new ByteArrayContent(frontBytes);
                    frontContent.Headers.ContentType = MediaTypeHeaderValue.Parse("image/jpeg");
                    var fileNameFront = Path.GetFileName(txtDniFront.Text);
                    form.Add(frontContent, "front", fileNameFront);

                    // DNI BACK
                    var backBytes = File.ReadAllBytes(txtDniBack.Text);
                    var backContent = new ByteArrayContent(backBytes);
                    backContent.Headers.ContentType = MediaTypeHeaderValue.Parse("image/jpeg");
                    var fileNameBack = Path.GetFileName(txtDniBack.Text);
                    form.Add(backContent, "back", fileNameBack);

                    // SELFIE (capturada en vivo)
                    var selfieBytes = File.ReadAllBytes(_selfiePath);
                    var selfieContent = new ByteArrayContent(selfieBytes);
                    selfieContent.Headers.ContentType = MediaTypeHeaderValue.Parse("image/jpeg");

                    var fileName = Path.GetFileName(_selfiePath);
                    form.Add(selfieContent, "selfie", fileName);

                    // =========================
                    // LLAMADA API
                    // =========================
                    string url = "http://127.0.0.1:8000/api/v1/verify-identity";

                    HttpResponseMessage response = await client.PostAsync(url, form);

                    string result = await response.Content.ReadAsStringAsync();

                    // =========================
                    // RESULTADO
                    // =========================
                    if (response.IsSuccessStatusCode)
                    {
                        MessageBox.Show("VALIDACIÓN EXITOSA");

                        txtResultado.Text = result;
                    }
                    else
                    {
                        MessageBox.Show("ERROR: " + result);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
            finally
            {
                btnValidar.Enabled = true;
                btnValidar.Text = "VALIDAR IDENTIDAD";
            }
        }
    }
}
