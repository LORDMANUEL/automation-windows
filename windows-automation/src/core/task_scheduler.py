import json
import os
from src.utils.logger import get_logger

logger = get_logger(__name__)
TASKS_FILE = os.path.join('data', 'tasks.json')

def _load_tasks():
    """Carga las tareas desde el archivo JSON."""
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"tasks": {}}
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error al cargar el archivo de tareas: {e}")
        return {"tasks": {}}

def _save_tasks(tasks_data):
    """Guarda las tareas en el archivo JSON."""
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(tasks_data, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error al guardar las tareas: {e}")
        return False

def get_task_commands(task_name):
    """Obtiene la lista de comandos para una tarea específica."""
    tasks_data = _load_tasks()
    task = tasks_data.get("tasks", {}).get(task_name)
    if task:
        logger.info(f"Comandos para la tarea '{task_name}' obtenidos.")
        return task
    else:
        logger.warning(f"No se encontró la tarea '{task_name}'.")
        return None

def save_new_task(task_name, commands):
    """Guarda una nueva tarea o actualiza una existente."""
    if not isinstance(commands, list) or not all(isinstance(c, str) for c in commands):
        logger.error("Formato de comandos inválido. Debe ser una lista de strings.")
        return "Error: Los comandos deben ser una lista de strings."

    logger.info(f"Guardando nueva tarea '{task_name}' con {len(commands)} comandos.")
    tasks_data = _load_tasks()
    tasks_data["tasks"][task_name] = commands

    if _save_tasks(tasks_data):
        return f"Tarea '{task_name}' guardada exitosamente."
    else:
        return "Error: No se pudo guardar la tarea."

# Nota: La ejecución real de los comandos será manejada por la CLI,
# que llamará a `get_task_commands` y luego procesará cada comando.
