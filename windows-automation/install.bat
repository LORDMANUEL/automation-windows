@echo off
echo ==========================================================
echo  Asistente de Instalacion para la Automatizacion de Windows
echo ==========================================================
echo.

REM --- Verificacion de Python ---
echo Verificando la instalacion de Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python no esta instalado o no se encuentra en el PATH.
    echo Por favor, instala Python 3.10+ y asegurate de marcar "Add Python to PATH" durante la instalacion.
    pause
    exit /b 1
)
echo Python encontrado.
echo.

REM --- Creacion del Entorno Virtual ---
echo Creando entorno virtual en la carpeta 'venv'...
if not exist venv (
    python -m venv venv
    if %errorlevel% neq 0 (
        echo Error: No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
    echo Entorno virtual creado.
) else (
    echo El entorno virtual 'venv' ya existe. Omitiendo creacion.
)
echo.

REM --- Activacion e Instalacion de Dependencias ---
echo Activando el entorno virtual e instalando dependencias...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Error: No se pudo activar el entorno virtual.
    pause
    exit /b 1
)

echo Instalando librerias desde requirements.txt. Esto puede tardar unos minutos...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Falla en la instalacion de dependencias. Revisa tu conexion a internet.
    pause
    exit /b 1
)
echo.

echo ==========================================================
echo  Instalacion completada con exito!
echo ==========================================================
echo.
echo Para ejecutar la aplicacion, usa el script 'run.bat'.
echo.
pause
