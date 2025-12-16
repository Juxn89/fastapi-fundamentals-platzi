# Crear entorno virtual en Python
- Crear el entorno virtual: ```python3 -m venv EVN_NAME FOLDER_NAME```
- Activar el entorno virtual: ```source FOLDER_NAME/bin/activate```, si estás en Windows: ```FOLDER_NAME/Scripts/activate```
- Instalar dependencias: ````pip install "fastapi[standard]"```

# Run project
- ```fastapi dev```

# SQLite3
## Commands
- Access to **SQLite**: ```sqlite3 .\db.sqlite3```
- Get current tables: ````.tables```

## Recomendadas para VS Code (instalación automática)

Hay un script PowerShell para instalar las extensiones recomendadas del workspace. Ejecuta desde la raíz del repo:

```powershell
./scripts/install-vscode-extensions.ps1
```

Si tu entorno usa proxy o inspección TLS (certificados self-signed), la instalación puede fallar. En ese caso instala las extensiones manualmente desde la UI de VS Code o añade la CA a Windows/trust store.