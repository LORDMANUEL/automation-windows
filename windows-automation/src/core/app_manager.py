import subprocess
import json
import os
import psutil
from src.utils.logger import get_logger

logger = get_logger(__name__)

def _load_app_paths():
    """
    Carga las rutas de las aplicaciones desde el archivo JSON.
    """
    # Construir la ruta al archivo app_paths.json
    # Se asume que el script se ejecuta desde la raíz del proyecto 'windows-automation'
    # o que la ruta de trabajo está configurada correctamente.
    path = os.path.join('data', 'app_paths.json')
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"No se pudo encontrar el archivo de configuración de aplicaciones en: {path}")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Error al decodificar el archivo JSON: {path}")
        return {}

APP_PATHS = _load_app_paths()

def abrir_aplicacion(nombre_app):
    """
    Abre una aplicación utilizando su nombre corto.
    """
    nombre_app = nombre_app.lower()
    if nombre_app in APP_PATHS:
        try:
            exe_path = APP_PATHS[nombre_app]
            logger.info(f"Abriendo aplicación: {nombre_app} ({exe_path})")
            subprocess.Popen(exe_path)
            return f"Aplicación '{nombre_app}' abierta."
        except FileNotFoundError:
            logger.error(f"El ejecutable '{exe_path}' no fue encontrado.")
            return f"Error: El ejecutable para '{nombre_app}' no fue encontrado."
        except Exception as e:
            logger.error(f"Ocurrió un error al abrir '{nombre_app}': {e}")
            return f"Error: Ocurrió un error al abrir '{nombre_app}'."
    else:
        logger.warning(f"Aplicación '{nombre_app}' no reconocida.")
        return f"Aplicación '{nombre_app}' no reconocida."

def cerrar_aplicacion(nombre_app):
    """
    Cierra una aplicación buscando el proceso por su nombre de ejecutable.
    """
    nombre_app = nombre_app.lower()
    if nombre_app in APP_PATHS:
        exe_name = APP_PATHS[nombre_app]
        logger.info(f"Intentando cerrar la aplicación: {nombre_app} ({exe_name})")

        found = False
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'].lower() == exe_name.lower():
                try:
                    p = psutil.Process(proc.info['pid'])
                    p.terminate() # Termina el proceso
                    logger.info(f"Proceso {proc.info['name']} (PID: {proc.info['pid']}) terminado.")
                    found = True
                except psutil.NoSuchProcess:
                    logger.warning(f"El proceso con PID {proc.info['pid']} ya no existía.")
                except psutil.AccessDenied:
                    logger.error(f"Acceso denegado para terminar el proceso con PID {proc.info['pid']}.")
                except Exception as e:
                    logger.error(f"Error inesperado al terminar el proceso {proc.info['pid']}: {e}")

        if found:
            return f"Aplicación '{nombre_app}' cerrada."
        else:
            logger.warning(f"No se encontró ningún proceso en ejecución para '{exe_name}'.")
            return f"La aplicación '{nombre_app}' no parece estar en ejecución."
    else:
        logger.warning(f"Aplicación '{nombre_app}' no reconocida.")
        return f"Aplicación '{nombre_app}' no reconocida."
