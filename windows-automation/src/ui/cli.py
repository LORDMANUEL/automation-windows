from src.core.app_manager import abrir_aplicacion, cerrar_aplicacion
from src.utils.logger import get_logger

logger = get_logger(__name__)

def main_loop():
    """
    Bucle principal de la interfaz de línea de comandos.
    """
    logger.info("Iniciando CLI...")
    print("Bienvenido al Asistente de Automatización de Windows.")
    print("Comandos disponibles: 'abre [app]', 'cierra [app]', 'salir'")

    while True:
        command = input("> ").strip().lower()
        if not command:
            continue

        logger.info(f"Comando recibido: '{command}'")

        if command == "salir":
            logger.info("Cerrando CLI...")
            break

        parts = command.split()
        action = parts[0]

        if len(parts) < 2:
            print("Comando incompleto. Uso: 'accion [argumento]'")
            continue

        target = parts[1]

        if action == "abre":
            result = abrir_aplicacion(target)
            print(result)
        elif action == "cierra":
            result = cerrar_aplicacion(target)
            print(result)
        else:
            print(f"Comando '{action}' no reconocido.")

if __name__ == '__main__':
    main_loop()
