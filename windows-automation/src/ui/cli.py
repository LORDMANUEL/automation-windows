from src.nlp.command_parser import CommandParser
from src.core import app_manager, browser_manager, window_manager, task_scheduler
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Mapeo de nombres de función a las funciones reales
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
    "organizar_ventanas": window_manager.organizar_ventanas,
    # Task Scheduler (acciones especiales, manejadas en la CLI)
    "ejecutar_tarea": "execute_task_flow",
    "crear_tarea": "create_task_flow"
}

def execute_task_flow(task_name, parser):
    """Flujo para ejecutar una tarea: obtiene los comandos y los procesa."""
    print(f"--- Ejecutando tarea: {task_name} ---")
    commands = task_scheduler.get_task_commands(task_name)
    if not commands:
        print(f"No se encontró la tarea '{task_name}'.")
        return

    for command in commands:
        print(f"> {command}")
        # Aquí procesamos cada comando de la tarea
        function_name, entity = parser.parse_command(command)
        if function_name and function_name in FUNCTION_MAP:
            # Evitamos recursión infinita
            if function_name in ["execute_task_flow", "create_task_flow"]:
                print("No se pueden anidar tareas.")
                continue

            action_function = FUNCTION_MAP[function_name]
            # ... (Lógica de ejecución similar al bucle principal)
            if entity:
                print(action_function(entity))
            else:
                print(action_function())
        else:
            print(f"Comando no reconocido en la tarea: '{command}'")
    print(f"--- Tarea '{task_name}' finalizada ---")

def create_task_flow(task_name):
    """Flujo interactivo para que el usuario grabe una nueva tarea."""
    print(f"--- Creando nueva tarea: {task_name} ---")
    print("Introduce los comandos uno por uno. Escribe 'fin' para guardar la tarea.")

    commands = []
    while True:
        command = input("... ")
        if command.lower() == 'fin':
            break
        commands.append(command)

    if commands:
        result = task_scheduler.save_new_task(task_name, commands)
        print(result)
    else:
        print("No se grabaron comandos. Tarea no guardada.")

def main_loop():
    """Bucle principal de la CLI."""
    logger.info("Iniciando CLI con NLP y gestión de tareas...")
    print("Asistente de Automatización. Escribe 'salir' para terminar.")
    parser = CommandParser()

    while True:
        command = input("> ").strip()
        if not command: continue

        if command.lower() == "salir":
            logger.info("Cerrando CLI...")
            browser_manager.cerrar_navegador()
            break

        function_name, entity = parser.parse_command(command)

        if function_name and function_name in FUNCTION_MAP:
            action = FUNCTION_MAP[function_name]

            if action == "create_task_flow":
                create_task_flow(entity)
                continue

            if action == "execute_task_flow":
                execute_task_flow(entity, parser)
                continue

            # Ejecución de comandos normales
            try:
                if entity:
                    result = action(entity)
                else:
                    result = action()

                if result:
                    if isinstance(result, list):
                        print("Ventanas abiertas:")
                        for item in result: print(f"- {item}")
                    else:
                        print(result)
            except Exception as e:
                logger.error(f"Error al ejecutar '{function_name}': {e}")
                print("Ocurrió un error al ejecutar el comando.")
        else:
            print("No entendí ese comando. Intenta de nuevo.")

if __name__ == '__main__':
    main_loop()
