namespace FaceDocVerifyClient.Vista
{
    partial class FrmValidacionIdentidad
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.grp_ConexionAPI = new System.Windows.Forms.GroupBox();
            this.lblEstadoConexion = new System.Windows.Forms.Label();
            this.btnObtenerToken = new System.Windows.Forms.Button();
            this.txtPassword = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.txtUsuario = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.txtApiUrl = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.btnDniBack = new System.Windows.Forms.Button();
            this.txtDniBack = new System.Windows.Forms.TextBox();
            this.btnDniFront = new System.Windows.Forms.Button();
            this.txtDniFront = new System.Windows.Forms.TextBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.txtSelfie = new System.Windows.Forms.TextBox();
            this.picSelfieCapturada = new System.Windows.Forms.PictureBox();
            this.btnTomarFoto = new System.Windows.Forms.Button();
            this.picCamara = new System.Windows.Forms.PictureBox();
            this.btnIniciarCamara = new System.Windows.Forms.Button();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.progressValidacion = new System.Windows.Forms.ProgressBar();
            this.btnValidar = new System.Windows.Forms.Button();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.txtResultado = new System.Windows.Forms.TextBox();
            this.grp_ConexionAPI.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picSelfieCapturada)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picCamara)).BeginInit();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.SuspendLayout();
            // 
            // grp_ConexionAPI
            // 
            this.grp_ConexionAPI.Controls.Add(this.lblEstadoConexion);
            this.grp_ConexionAPI.Controls.Add(this.btnObtenerToken);
            this.grp_ConexionAPI.Controls.Add(this.txtPassword);
            this.grp_ConexionAPI.Controls.Add(this.label3);
            this.grp_ConexionAPI.Controls.Add(this.txtUsuario);
            this.grp_ConexionAPI.Controls.Add(this.label2);
            this.grp_ConexionAPI.Controls.Add(this.txtApiUrl);
            this.grp_ConexionAPI.Controls.Add(this.label1);
            this.grp_ConexionAPI.Font = new System.Drawing.Font("Segoe UI Emoji", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.grp_ConexionAPI.Location = new System.Drawing.Point(12, 12);
            this.grp_ConexionAPI.Name = "grp_ConexionAPI";
            this.grp_ConexionAPI.Size = new System.Drawing.Size(1222, 137);
            this.grp_ConexionAPI.TabIndex = 0;
            this.grp_ConexionAPI.TabStop = false;
            this.grp_ConexionAPI.Text = "Conexión API";
            // 
            // lblEstadoConexion
            // 
            this.lblEstadoConexion.AutoSize = true;
            this.lblEstadoConexion.Font = new System.Drawing.Font("Segoe UI Emoji", 7.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblEstadoConexion.ForeColor = System.Drawing.Color.Red;
            this.lblEstadoConexion.Location = new System.Drawing.Point(574, 19);
            this.lblEstadoConexion.Name = "lblEstadoConexion";
            this.lblEstadoConexion.Size = new System.Drawing.Size(98, 17);
            this.lblEstadoConexion.TabIndex = 7;
            this.lblEstadoConexion.Text = "SIN CONECTAR";
            // 
            // btnObtenerToken
            // 
            this.btnObtenerToken.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnObtenerToken.Font = new System.Drawing.Font("Algerian", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnObtenerToken.ForeColor = System.Drawing.Color.DarkSlateGray;
            this.btnObtenerToken.Location = new System.Drawing.Point(564, 85);
            this.btnObtenerToken.Name = "btnObtenerToken";
            this.btnObtenerToken.Size = new System.Drawing.Size(190, 36);
            this.btnObtenerToken.TabIndex = 6;
            this.btnObtenerToken.Text = "Obtener Token";
            this.btnObtenerToken.UseVisualStyleBackColor = true;
            this.btnObtenerToken.Click += new System.EventHandler(this.btnObtenerToken_Click);
            // 
            // txtPassword
            // 
            this.txtPassword.ForeColor = System.Drawing.Color.DarkGreen;
            this.txtPassword.Location = new System.Drawing.Point(167, 91);
            this.txtPassword.MaxLength = 200;
            this.txtPassword.Name = "txtPassword";
            this.txtPassword.Size = new System.Drawing.Size(362, 30);
            this.txtPassword.TabIndex = 5;
            this.txtPassword.Text = "1234";
            this.txtPassword.UseSystemPasswordChar = true;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(9, 99);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(135, 22);
            this.label3.TabIndex = 4;
            this.label3.Text = "PASSWORD API:";
            // 
            // txtUsuario
            // 
            this.txtUsuario.ForeColor = System.Drawing.Color.DarkGreen;
            this.txtUsuario.Location = new System.Drawing.Point(167, 55);
            this.txtUsuario.MaxLength = 200;
            this.txtUsuario.Name = "txtUsuario";
            this.txtUsuario.Size = new System.Drawing.Size(362, 30);
            this.txtUsuario.TabIndex = 3;
            this.txtUsuario.Text = "admin";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(9, 63);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(117, 22);
            this.label2.TabIndex = 2;
            this.label2.Text = "USUARIO API:";
            // 
            // txtApiUrl
            // 
            this.txtApiUrl.ForeColor = System.Drawing.Color.DarkGreen;
            this.txtApiUrl.Location = new System.Drawing.Point(167, 19);
            this.txtApiUrl.MaxLength = 200;
            this.txtApiUrl.Name = "txtApiUrl";
            this.txtApiUrl.Size = new System.Drawing.Size(362, 30);
            this.txtApiUrl.TabIndex = 1;
            this.txtApiUrl.Text = "http://127.0.0.1:8000";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 27);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(75, 22);
            this.label1.TabIndex = 0;
            this.label1.Text = "API URL:";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.btnDniBack);
            this.groupBox1.Controls.Add(this.txtDniBack);
            this.groupBox1.Controls.Add(this.btnDniFront);
            this.groupBox1.Controls.Add(this.txtDniFront);
            this.groupBox1.Font = new System.Drawing.Font("Segoe UI Emoji", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox1.Location = new System.Drawing.Point(12, 155);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(1222, 125);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Carga y Validación DNIe";
            // 
            // btnDniBack
            // 
            this.btnDniBack.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnDniBack.Font = new System.Drawing.Font("Bell MT", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnDniBack.ForeColor = System.Drawing.Color.DarkSlateGray;
            this.btnDniBack.Location = new System.Drawing.Point(14, 64);
            this.btnDniBack.Name = "btnDniBack";
            this.btnDniBack.Size = new System.Drawing.Size(205, 32);
            this.btnDniBack.TabIndex = 9;
            this.btnDniBack.Text = "Seleccionar DNIe Posterior";
            this.btnDniBack.UseVisualStyleBackColor = true;
            this.btnDniBack.Click += new System.EventHandler(this.btnDniBack_Click);
            // 
            // txtDniBack
            // 
            this.txtDniBack.Enabled = false;
            this.txtDniBack.ForeColor = System.Drawing.Color.DarkGreen;
            this.txtDniBack.Location = new System.Drawing.Point(241, 66);
            this.txtDniBack.MaxLength = 200;
            this.txtDniBack.Name = "txtDniBack";
            this.txtDniBack.Size = new System.Drawing.Size(692, 30);
            this.txtDniBack.TabIndex = 8;
            // 
            // btnDniFront
            // 
            this.btnDniFront.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnDniFront.Font = new System.Drawing.Font("Bell MT", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnDniFront.ForeColor = System.Drawing.Color.DarkSlateGray;
            this.btnDniFront.Location = new System.Drawing.Point(14, 27);
            this.btnDniFront.Name = "btnDniFront";
            this.btnDniFront.Size = new System.Drawing.Size(205, 32);
            this.btnDniFront.TabIndex = 6;
            this.btnDniFront.Text = "Seleccionar DNIe Frontal";
            this.btnDniFront.UseVisualStyleBackColor = true;
            this.btnDniFront.Click += new System.EventHandler(this.btnDniFront_Click);
            // 
            // txtDniFront
            // 
            this.txtDniFront.Enabled = false;
            this.txtDniFront.ForeColor = System.Drawing.Color.DarkGreen;
            this.txtDniFront.Location = new System.Drawing.Point(241, 29);
            this.txtDniFront.MaxLength = 200;
            this.txtDniFront.Name = "txtDniFront";
            this.txtDniFront.Size = new System.Drawing.Size(692, 30);
            this.txtDniFront.TabIndex = 1;
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.picCamara);
            this.groupBox2.Controls.Add(this.txtSelfie);
            this.groupBox2.Controls.Add(this.picSelfieCapturada);
            this.groupBox2.Controls.Add(this.btnTomarFoto);
            this.groupBox2.Controls.Add(this.btnIniciarCamara);
            this.groupBox2.Font = new System.Drawing.Font("Segoe UI Emoji", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox2.Location = new System.Drawing.Point(12, 286);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(816, 270);
            this.groupBox2.TabIndex = 2;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Captura y Validación Selfie";
            // 
            // txtSelfie
            // 
            this.txtSelfie.Font = new System.Drawing.Font("Segoe UI Emoji", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtSelfie.ForeColor = System.Drawing.Color.DarkGreen;
            this.txtSelfie.Location = new System.Drawing.Point(13, 237);
            this.txtSelfie.MaxLength = 200;
            this.txtSelfie.Name = "txtSelfie";
            this.txtSelfie.Size = new System.Drawing.Size(237, 27);
            this.txtSelfie.TabIndex = 10;
            // 
            // picSelfieCapturada
            // 
            this.picSelfieCapturada.Location = new System.Drawing.Point(544, 22);
            this.picSelfieCapturada.Name = "picSelfieCapturada";
            this.picSelfieCapturada.Size = new System.Drawing.Size(246, 232);
            this.picSelfieCapturada.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.picSelfieCapturada.TabIndex = 9;
            this.picSelfieCapturada.TabStop = false;
            // 
            // btnTomarFoto
            // 
            this.btnTomarFoto.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnTomarFoto.Font = new System.Drawing.Font("Bell MT", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnTomarFoto.ForeColor = System.Drawing.Color.DarkSlateGray;
            this.btnTomarFoto.Location = new System.Drawing.Point(30, 84);
            this.btnTomarFoto.Name = "btnTomarFoto";
            this.btnTomarFoto.Size = new System.Drawing.Size(126, 32);
            this.btnTomarFoto.TabIndex = 8;
            this.btnTomarFoto.Text = "Tomar Foto";
            this.btnTomarFoto.UseVisualStyleBackColor = true;
            this.btnTomarFoto.Click += new System.EventHandler(this.btnTomarFoto_Click);
            // 
            // picCamara
            // 
            this.picCamara.Location = new System.Drawing.Point(256, 22);
            this.picCamara.Name = "picCamara";
            this.picCamara.Size = new System.Drawing.Size(273, 232);
            this.picCamara.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.picCamara.TabIndex = 7;
            this.picCamara.TabStop = false;
            // 
            // btnIniciarCamara
            // 
            this.btnIniciarCamara.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnIniciarCamara.Font = new System.Drawing.Font("Bell MT", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnIniciarCamara.ForeColor = System.Drawing.Color.DarkSlateGray;
            this.btnIniciarCamara.Location = new System.Drawing.Point(30, 46);
            this.btnIniciarCamara.Name = "btnIniciarCamara";
            this.btnIniciarCamara.Size = new System.Drawing.Size(126, 32);
            this.btnIniciarCamara.TabIndex = 6;
            this.btnIniciarCamara.Text = "Iniciar Cámara";
            this.btnIniciarCamara.UseVisualStyleBackColor = true;
            this.btnIniciarCamara.Click += new System.EventHandler(this.btnIniciarCamara_Click);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.progressValidacion);
            this.groupBox3.Controls.Add(this.btnValidar);
            this.groupBox3.Font = new System.Drawing.Font("Segoe UI Emoji", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox3.Location = new System.Drawing.Point(851, 295);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(383, 261);
            this.groupBox3.TabIndex = 3;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "VALIDACIÓN INTEGRADA CON API";
            // 
            // progressValidacion
            // 
            this.progressValidacion.Location = new System.Drawing.Point(6, 77);
            this.progressValidacion.Name = "progressValidacion";
            this.progressValidacion.Size = new System.Drawing.Size(314, 30);
            this.progressValidacion.TabIndex = 7;
            this.progressValidacion.Visible = false;
            // 
            // btnValidar
            // 
            this.btnValidar.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnValidar.Font = new System.Drawing.Font("Bell MT", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnValidar.ForeColor = System.Drawing.Color.DarkSlateGray;
            this.btnValidar.Location = new System.Drawing.Point(6, 37);
            this.btnValidar.Name = "btnValidar";
            this.btnValidar.Size = new System.Drawing.Size(269, 32);
            this.btnValidar.TabIndex = 6;
            this.btnValidar.Text = "VALIDAR IDENTIDAD";
            this.btnValidar.UseVisualStyleBackColor = true;
            this.btnValidar.Click += new System.EventHandler(this.btnValidar_Click);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.txtResultado);
            this.groupBox4.Font = new System.Drawing.Font("Segoe UI Emoji", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox4.Location = new System.Drawing.Point(12, 562);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(1222, 182);
            this.groupBox4.TabIndex = 4;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Resultado";
            // 
            // txtResultado
            // 
            this.txtResultado.Font = new System.Drawing.Font("Segoe UI Emoji", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtResultado.ForeColor = System.Drawing.Color.DarkGreen;
            this.txtResultado.Location = new System.Drawing.Point(11, 29);
            this.txtResultado.MaxLength = 200;
            this.txtResultado.Multiline = true;
            this.txtResultado.Name = "txtResultado";
            this.txtResultado.Size = new System.Drawing.Size(1180, 147);
            this.txtResultado.TabIndex = 10;
            // 
            // FrmValidacionIdentidad
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1292, 756);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.grp_ConexionAPI);
            this.Name = "FrmValidacionIdentidad";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "FaceDocVerify - Cliente de Validación de Identidad";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.FrmValidacionIdentidad_FormClosing);
            this.grp_ConexionAPI.ResumeLayout(false);
            this.grp_ConexionAPI.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picSelfieCapturada)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picCamara)).EndInit();
            this.groupBox3.ResumeLayout(false);
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox grp_ConexionAPI;
        private System.Windows.Forms.TextBox txtPassword;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtUsuario;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtApiUrl;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnObtenerToken;
        private System.Windows.Forms.Label lblEstadoConexion;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button btnDniFront;
        private System.Windows.Forms.TextBox txtDniFront;
        private System.Windows.Forms.Button btnDniBack;
        private System.Windows.Forms.TextBox txtDniBack;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.PictureBox picCamara;
        private System.Windows.Forms.Button btnIniciarCamara;
        private System.Windows.Forms.PictureBox picSelfieCapturada;
        private System.Windows.Forms.Button btnTomarFoto;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Button btnValidar;
        private System.Windows.Forms.ProgressBar progressValidacion;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.TextBox txtResultado;
        private System.Windows.Forms.TextBox txtSelfie;
    }
}