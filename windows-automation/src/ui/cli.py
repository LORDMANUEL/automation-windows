from src.nlp.command_parser import CommandParser
from src.core import app_manager, browser_manager, window_manager
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Mapeo de nombres de función (string) a las funciones reales (callable)
FUNCTION_MAP = {
    # App Manager
    "abrir_aplicacion": app_manager.abrir_aplicacion,
    "cerrar_aplicacion": app_manager.cerrar_aplicacion,
    # Browser Manager
    "navegar_a": browser_manager.navegar_a,
    "buscar_en_google": browser_manager.buscar_en_google,
    "cerrar_navegador": browser_manager.cerrar_navegador,
    # Window Manager
    "listar_ventanas_abiertas": window_manager.listar_ventanas_abiertas,
    "enfocar_ventana": window_manager.enfocar_ventana,
    "minimizar_ventana": window_manager.minimizar_ventana,
    "maximizar_ventana": window_manager.maximizar_ventana,
    "mover_ventana": window_manager.mover_ventana,
    "redimensionar_ventana": window_manager.redimensionar_ventana,
    "organizar_ventanas": window_manager.organizar_ventanas
}

def main_loop():
    """Bucle principal de la CLI, ahora impulsado por NLP."""
    logger.info("Iniciando CLI con NLP...")
    print("Bienvenido al Asistente de Automatización (NLP activado).")
    print("Escribe 'salir' para terminar.")

    parser = CommandParser()

    while True:
        command = input("> ").strip()
        if not command:
            continue

        if command.lower() == "salir":
            logger.info("Cerrando CLI...")
            browser_manager.cerrar_navegador()
            break

        function_name, entity = parser.parse_command(command)

        if function_name and function_name in FUNCTION_MAP:
            action_function = FUNCTION_MAP[function_name]

            try:
                if entity:
                    result = action_function(entity)
                else:
                    result = action_function()

                # Imprimir el resultado si no es nulo
                if result:
                    # Manejo especial para listas (de listar_ventanas)
                    if isinstance(result, list):
                        print("Ventanas abiertas:")
                        for item in result:
                            print(f"- {item}")
                    else:
                        print(result)

            except TypeError as e:
                logger.error(f"Error al llamar a la función '{function_name}': {e}")
                print(f"Error: El comando para '{function_name}' parece estar mal formado.")
            except Exception as e:
                logger.error(f"Un error inesperado ocurrió al ejecutar el comando: {e}")
                print("Ocurrió un error inesperado.")
        else:
            print("No entendí ese comando. Intenta de nuevo.")

if __name__ == '__main__':
    main_loop()
