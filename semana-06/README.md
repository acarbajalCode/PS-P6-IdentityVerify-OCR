# Semana 6 — API Segura + Azure Deployment

**Rama:** `feature/s6-secure-api-azure` → PR hacia `main`

## Entregables
- [ ] API completa en FastAPI con todos los middlewares de seguridad
- [ ] `Azure_Deploy.md` — pasos reproducibles de despliegue
- [ ] URL pública funcionando: `https://verifyid.uqaisolutions.com.pe`
- [ ] Azure Blob Storage configurado con AES-256
- [ ] Azure Key Vault — secrets no hardcodeados en código
- [ ] Score ≥A en https://securityheaders.com con la URL pública

## Azure_Deploy.md (completar con tus pasos reales)

```bash
# 1. Crear Resource Group
az group create --name rg-verifyid-prod --location westus3

# 2. Crear App Service Plan
az appservice plan create \
  --name plan-verifyid \
  --resource-group rg-verifyid-prod \
  --sku B1 --is-linux

# 3. Crear Web App
az webapp create \
  --name verifyid-uqai \
  --resource-group rg-verifyid-prod \
  --plan plan-verifyid \
  --runtime "PYTHON|3.11"

# 4. Crear Key Vault
az keyvault create \
  --name kv-verifyid \
  --resource-group rg-verifyid-prod \
  --location westus3

# 5. Agregar secrets al Key Vault
az keyvault secret set --vault-name kv-verifyid --name "SECRET-KEY" --value "$(python -c 'import secrets; print(secrets.token_hex(32))')"
az keyvault secret set --vault-name kv-verifyid --name "DB-CONNECTION-STRING" --value "TU_CONNECTION_STRING"
```

## Checklist de seguridad del deploy

- [ ] HTTPS forzado (HTTP → 301 → HTTPS)
- [ ] Security headers presentes (verificar en securityheaders.com)
- [ ] Variables de entorno en Key Vault (no en código)
- [ ] Logs activos en Azure Monitor
- [ ] Rate limiting funcionando (probar con 6 requests en 1 minuto → 429)
