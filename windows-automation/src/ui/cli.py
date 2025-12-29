from src.core.app_manager import abrir_aplicacion, cerrar_aplicacion
from src.core.browser_manager import abrir_navegador, navegar_a, cerrar_navegador, buscar_en_google
from src.core.window_manager import listar_ventanas_abiertas, enfocar_ventana
from src.utils.logger import get_logger

logger = get_logger(__name__)

def main_loop():
    """
    Bucle principal de la interfaz de línea de comandos.
    """
    logger.info("Iniciando CLI...")
    print("Bienvenido al Asistente de Automatización de Windows.")
    print("Comandos: 'abre [app]', 'cierra [app]', 'navega a [url]', 'busca [termino]', 'lista ventanas', 'enfoca [titulo]', 'cierra navegador', 'salir'")

    while True:
        command = input("> ").strip().lower()
        if not command:
            continue

        logger.info(f"Comando recibido: '{command}'")

        if command == "salir":
            logger.info("Cerrando CLI...")
            cerrar_navegador() # Cierra el navegador al salir
            break

        if command == "cierra navegador":
            result = cerrar_navegador()
            print(result)
            continue

        if command == "lista ventanas":
            result = listar_ventanas_abiertas()
            if isinstance(result, list):
                print("Ventanas abiertas:")
                for titulo in result:
                    print(f"- {titulo}")
            else:
                print(result)
            continue

        parts = command.split()
        action = parts[0]

        if len(parts) < 2:
            print("Comando incompleto. Uso: 'accion [argumento]'")
            continue

        if action == "abre":
            target = parts[1]
            result = abrir_aplicacion(target)
            print(result)
        elif action == "cierra":
            target = parts[1]
            result = cerrar_aplicacion(target)
            print(result)
        elif action == "navega":
            if len(parts) >= 3 and parts[1] == "a":
                url = parts[2]
                result = abrir_navegador(url)
                if "ya está abierto" in result:
                    result = navegar_a(url)
                print(result)
            else:
                print("Comando 'navega' mal formado. Uso: 'navega a [url]'")
        elif action == "busca":
            search_term = " ".join(parts[1:])
            result = buscar_en_google(search_term)
            print(result)
        elif action == "enfoca":
            window_title = " ".join(parts[1:])
            result = enfocar_ventana(window_title)
            print(result)
        else:
            print(f"Comando '{action}' no reconocido.")

if __name__ == '__main__':
    main_loop()
