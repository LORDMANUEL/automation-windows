import sys
import os
import argparse

# Configura la ruta del proyecto para que los módulos se encuentren correctamente
project_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_dir)
sys.path.append('src')

from src.utils.logger import get_logger

logger = get_logger(__name__)

def main():
    """
    Punto de entrada principal de la aplicación.
    Lanza la GUI por defecto o la CLI si se especifica con un argumento.
    """
    parser = argparse.ArgumentParser(description="Asistente de Automatización de Windows")
    parser.add_argument(
        '--cli',
        action='store_true',
        help='Ejecuta la aplicación en modo de interfaz de línea de comandos (CLI).'
    )
    args = parser.parse_args()

    if args.cli:
        logger.info("Lanzando en modo CLI...")
        from src.ui.cli import main_loop
        main_loop()
    else:
        logger.info("Lanzando en modo GUI...")
        # Importamos aquí para evitar problemas de tkinter en entornos sin display
        try:
            from src.ui.gui import start_gui
            start_gui()
        except ImportError as e:
            logger.error(f"No se pudo iniciar la GUI. Error: {e}")
            logger.error("Asegúrate de que el entorno soporta una interfaz gráfica (ej. Tkinter).")
            print("Error: No se pudo iniciar la GUI. Para usar la versión de texto, ejecuta: python main.py --cli")

if __name__ == "__main__":
    main()
