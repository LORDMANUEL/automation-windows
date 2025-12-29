from pywinauto import Desktop
from src.utils.logger import get_logger

logger = get_logger(__name__)

def listar_ventanas_abiertas():
    """
    Obtiene una lista de los títulos de todas las ventanas visibles.
    """
    logger.info("Listando ventanas abiertas...")
    try:
        # Usamos el backend "uia" que es más moderno y compatible
        windows = Desktop(backend="uia").windows()
        # Filtramos para obtener solo las ventanas que tienen un título visible
        titulos = [w.window_text() for w in windows if w.window_text()]
        if not titulos:
            return "No se encontraron ventanas abiertas con título."
        return titulos
    except Exception as e:
        logger.error(f"Error al listar las ventanas: {e}")
        return "Error: No se pudo obtener la lista de ventanas."

def enfocar_ventana(titulo):
    """
    Pone en primer plano (enfoca) una ventana basándose en su título.
    """
    logger.info(f"Intentando enfocar la ventana con título: '{titulo}'")
    try:
        # Busca la ventana por el título. best_match encuentra la más parecida.
        ventana = Desktop(backend="uia").window(title_re=f".*{titulo}.*", best_match=True)

        if ventana.exists() and ventana.is_visible():
            ventana.set_focus()
            logger.info(f"Ventana '{ventana.window_text()}' enfocada.")
            return f"Ventana '{ventana.window_text()}' enfocada."
        else:
            logger.warning(f"No se encontró una ventana visible con el título parecido a '{titulo}'.")
            return f"No se encontró una ventana visible con el título '{titulo}'."
    except Exception as e:
        logger.error(f"Error al enfocar la ventana '{titulo}': {e}")
        return f"Error: No se pudo enfocar la ventana '{titulo}'."
