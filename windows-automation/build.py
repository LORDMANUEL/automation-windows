# Este script utiliza PyInstaller para empaquetar la aplicación en un solo ejecutable.
# Para ejecutarlo, primero instala PyInstaller: pip install pyinstaller
# Luego, ejecuta este script: python build.py

import PyInstaller.__main__
import os

# Nombre del archivo ejecutable de salida
EXE_NAME = "AsistenteAutomatizacion"

# Archivos y carpetas de datos que deben incluirse
DATA_TO_INCLUDE = [
    'src',
    'data'
]

def build_executable():
    """
    Construye el ejecutable usando PyInstaller.
    """
    print("Iniciando el proceso de compilacion...")

    # Construye la lista de argumentos para PyInstaller
    pyinstaller_args = [
        'main.py',
        '--name', EXE_NAME,
        '--onefile',          # Crea un solo archivo .exe
        '--windowed',         # Oculta la consola de comandos al ejecutar la GUI
        '--noconsole',        # Sin consola (equivalente a --windowed en Windows)
    ]

    # Añade las carpetas de datos
    for item in DATA_TO_INCLUDE:
        if os.path.exists(item):
            print(f"Añadiendo datos desde: {item}")
            pyinstaller_args.extend(['--add-data', f'{item}{os.pathsep}{item}'])
        else:
            print(f"Advertencia: La carpeta/archivo de datos '{item}' no se encontró y no será incluido.")

    print(f"\nEjecutando PyInstaller con los siguientes argumentos: {' '.join(pyinstaller_args)}\n")

    try:
        PyInstaller.__main__.run(pyinstaller_args)
        print("\n========================================================")
        print(" Compilacion completada con exito!")
        print(f" El ejecutable se encuentra en la carpeta 'dist/{EXE_NAME}.exe'")
        print("========================================================")
    except Exception as e:
        print("\n========================================================")
        print(f" Error durante la compilacion: {e}")
        print("========================================================")

if __name__ == '__main__':
    build_executable()
