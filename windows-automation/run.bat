@echo off
echo ==========================================================
echo  Lanzando el Asistente de Automatizacion de Windows
echo ==========================================================
echo.

REM --- Activacion del Entorno Virtual ---
echo Activando entorno virtual...
if not exist venv\Scripts\activate (
    echo Error: Entorno virtual no encontrado.
    echo Por favor, ejecuta 'install.bat' primero.
    pause
    exit /b 1
)
call venv\Scripts\activate

REM --- Ejecucion de la Aplicacion ---
echo Iniciando aplicacion...
python main.py

echo.
echo La aplicacion ha finalizado. Presiona cualquier tecla para cerrar esta ventana.
pause >nul
