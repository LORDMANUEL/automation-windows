from pywinauto import Desktop
import pyautogui # Para obtener las dimensiones de la pantalla
from src.utils.logger import get_logger

logger = get_logger(__name__)

def _get_window(titulo):
    """Helper function to find a window by its title using regex."""
    try:
        ventana = Desktop(backend="uia").window(title_re=f".*{titulo}.*", best_match=True)
        if ventana.exists() and ventana.is_visible():
            return ventana
        else:
            logger.warning(f"No se encontró una ventana visible con el título parecido a '{titulo}'.")
            return None
    except Exception as e:
        logger.error(f"Ocurrió un error al buscar la ventana '{titulo}': {e}")
        return None

def listar_ventanas_abiertas():
    """Obtiene una lista de los títulos de todas las ventanas visibles."""
    logger.info("Listando ventanas abiertas...")
    try:
        windows = Desktop(backend="uia").windows()
        titulos = [w.window_text() for w in windows if w.window_text()]
        return titulos if titulos else "No se encontraron ventanas abiertas con título."
    except Exception as e:
        logger.error(f"Error al listar las ventanas: {e}")
        return "Error: No se pudo obtener la lista de ventanas."

def enfocar_ventana(titulo):
    """Pone en primer plano (enfoca) una ventana basándose en su título."""
    logger.info(f"Intentando enfocar la ventana con título: '{titulo}'")
    ventana = _get_window(titulo)
    if ventana:
        try:
            ventana.set_focus()
            return f"Ventana '{ventana.window_text()}' enfocada."
        except Exception as e:
            logger.error(f"Error al enfocar la ventana '{titulo}': {e}")
            return f"Error al enfocar la ventana '{titulo}'."
    return f"No se encontró una ventana visible con el título '{titulo}'."

def mover_ventana(titulo, x, y):
    """Mueve la ventana especificada a las coordenadas (x, y)."""
    logger.info(f"Moviendo ventana '{titulo}' a ({x}, {y})")
    ventana = _get_window(titulo)
    if ventana:
        try:
            ventana.move_window(x=int(x), y=int(y))
            return f"Ventana '{titulo}' movida a ({x}, {y})."
        except Exception as e:
            logger.error(f"Error al mover la ventana '{titulo}': {e}")
            return f"Error al mover la ventana '{titulo}'."
    return f"No se encontró la ventana '{titulo}'."

def redimensionar_ventana(titulo, ancho, alto):
    """Redimensiona la ventana especificada."""
    logger.info(f"Redimensionando ventana '{titulo}' a {ancho}x{alto}")
    ventana = _get_window(titulo)
    if ventana:
        try:
            ventana.resize(width=int(ancho), height=int(alto))
            return f"Ventana '{titulo}' redimensionada a {ancho}x{alto}."
        except Exception as e:
            logger.error(f"Error al redimensionar la ventana '{titulo}': {e}")
            return f"Error al redimensionar la ventana '{titulo}'."
    return f"No se encontró la ventana '{titulo}'."

def minimizar_ventana(titulo):
    """Minimiza la ventana especificada."""
    logger.info(f"Minimizando ventana '{titulo}'")
    ventana = _get_window(titulo)
    if ventana:
        try:
            ventana.minimize()
            return f"Ventana '{titulo}' minimizada."
        except Exception as e:
            logger.error(f"Error al minimizar la ventana '{titulo}': {e}")
            return f"Error al minimizar la ventana '{titulo}'."
    return f"No se encontró la ventana '{titulo}'."

def maximizar_ventana(titulo):
    """Maximiza la ventana especificada."""
    logger.info(f"Maximizando ventana '{titulo}'")
    ventana = _get_window(titulo)
    if ventana:
        try:
            ventana.maximize()
            return f"Ventana '{titulo}' maximizada."
        except Exception as e:
            logger.error(f"Error al maximizar la ventana '{titulo}': {e}")
            return f"Error al maximizar la ventana '{titulo}'."
    return f"No se encontró la ventana '{titulo}'."

def organizar_ventanas(titulo, disposicion):
    """Organiza una ventana según un layout predefinido."""
    logger.info(f"Organizando ventana '{titulo}' en disposición '{disposicion}'")
    ventana = _get_window(titulo)
    if not ventana:
        return f"No se encontró la ventana '{titulo}'."

    try:
        screen_width, screen_height = pyautogui.size()

        if disposicion == "izquierda":
            ventana.move_window(x=0, y=0, width=screen_width // 2, height=screen_height, repaint=True)
            return f"Ventana '{titulo}' organizada a la izquierda."
        elif disposicion == "derecha":
            ventana.move_window(x=screen_width // 2, y=0, width=screen_width // 2, height=screen_height, repaint=True)
            return f"Ventana '{titulo}' organizada a la derecha."
        else:
            return f"Disposición '{disposicion}' no reconocida. Opciones: izquierda, derecha."

    except Exception as e:
        logger.error(f"Error al organizar la ventana '{titulo}': {e}")
        return f"Error al organizar la ventana '{titulo}'."
