# Paso 3 — Conexión al API y Obtención de JWT

## 1. Crear variable global en el formulario

Dentro de `FrmValidacionIdentidad.cs`

```csharp
private string _jwtToken = "";
```

---

## 2. Instalar paquete NuGet

Menú:

```text
Tools
→ NuGet Package Manager
→ Manage NuGet Packages for Solution
```

Instalar:

```text
Newtonsoft.Json
```

---

## 3. Crear clases para Login

Crear archivo:

```text
Models/LoginRequest.cs
```

```csharp
namespace FaceDocVerifyClient.Models
{
    public class LoginRequest
    {
        public string username { get; set; }
        public string password { get; set; }
    }
}
```

---

Crear archivo:

```text
Models/LoginResponse.cs
```

```csharp
namespace FaceDocVerifyClient.Models
{
    public class LoginResponse
    {
        public string access_token { get; set; }
        public string token_type { get; set; }
    }
}
```

---

## 4. Agregar using

En el formulario:

```csharp
using System.Text;
using Newtonsoft.Json;
using FaceDocVerifyClient.Models;
```

---

## 5. Evento btnObtenerToken_Click

Doble clic al botón:

```text
btnObtenerToken
```

y reemplazar por:

```csharp
private async void btnObtenerToken_Click(object sender, EventArgs e)
{
    try
    {
        lblEstadoConexion.Text = "Conectando...";

        using HttpClient client = new HttpClient();

        var loginData = new LoginRequest
        {
            username = txtUsuario.Text.Trim(),
            password = txtPassword.Text.Trim()
        };

        var json = JsonConvert.SerializeObject(loginData);

        var content = new StringContent(
            json,
            Encoding.UTF8,
            "application/json");

        string url = txtApiUrl.Text.Trim() + "/api/v1/login";

        HttpResponseMessage response =
            await client.PostAsync(url, content);

        if (!response.IsSuccessStatusCode)
        {
            lblEstadoConexion.Text = "Error autenticando";
            MessageBox.Show(
                "Credenciales inválidas",
                "FaceDocVerify",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
            return;
        }

        string responseJson =
            await response.Content.ReadAsStringAsync();

        var loginResponse =
            JsonConvert.DeserializeObject<LoginResponse>(responseJson);

        _jwtToken = loginResponse.access_token;

        lblEstadoConexion.Text =
            "🟢 Conectado correctamente";

        MessageBox.Show(
            "Token obtenido correctamente",
            "FaceDocVerify",
            MessageBoxButtons.OK,
            MessageBoxIcon.Information);
    }
    catch (Exception ex)
    {
        MessageBox.Show(
            ex.Message,
            "Error",
            MessageBoxButtons.OK,
            MessageBoxIcon.Error);
    }
}
```

---

## Resultado esperado

Al presionar:

```text
Obtener Token
```

Debe ocurrir:

```text
POST
http://127.0.0.1:8000/api/v1/login
```

Si todo está correcto:

```text
🟢 Conectado correctamente
```

y la variable:

```csharp
_jwtToken
```

debe contener el JWT emitido por FaceDocVerify.

---

## Validación

Antes de seguir a cámara web:

1. Ejecutar API FastAPI.
2. Ejecutar aplicación .NET.
3. Presionar "Obtener Token".
4. Confirmar que aparece:

```text
Token obtenido correctamente
```

5. Confirmar que:

```text
lblEstadoConexion
```

muestra:

```text
🟢 Conectado correctamente
```
