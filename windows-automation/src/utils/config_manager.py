import json
import os
from src.utils.logger import get_logger

logger = get_logger(__name__)
CONFIG_FILE = os.path.join('data', 'config.json')

def get_config():
    """
    Carga la configuración completa desde el archivo JSON.
    Si el archivo no existe, crea uno con valores por defecto.
    """
    if not os.path.exists(CONFIG_FILE):
        logger.warning(f"Archivo de configuración no encontrado. Creando uno nuevo en '{CONFIG_FILE}'.")
        default_config = {
            "llm": {
                "endpoint": "http://localhost:11434/api/generate",
                "model": "llama3"
            }
        }
        save_config(default_config)
        return default_config

    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error al cargar el archivo de configuración: {e}")
        return {} # Devuelve un dict vacío en caso de error

def save_config(config_data):
    """
    Guarda el diccionario de configuración completo en el archivo JSON.
    """
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, indent=2)
        logger.info("Configuración guardada exitosamente.")
        return True
    except Exception as e:
        logger.error(f"Error al guardar la configuración: {e}")
        return False

def get_setting(key_path):
    """
    Obtiene un valor específico de la configuración usando una ruta de claves.
    Ejemplo: get_setting("llm.endpoint")
    """
    config = get_config()
    keys = key_path.split('.')
    value = config
    try:
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError):
        logger.warning(f"No se encontró la configuración para la clave: '{key_path}'")
        return None
