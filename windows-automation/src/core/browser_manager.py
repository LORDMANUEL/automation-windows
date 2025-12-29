from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Variable global para mantener la instancia del driver
driver = None

def abrir_navegador(url, navegador="chrome"):
    """
    Abre un navegador y navega a la URL especificada.
    """
    global driver
    if driver is not None:
        logger.warning("El navegador ya está abierto. Cierra la sesión actual antes de abrir una nueva.")
        return "El navegador ya está abierto."

    logger.info(f"Abriendo navegador '{navegador}' en la URL: {url}")

    try:
        if navegador.lower() == "chrome":
            # Usar webdriver-manager para instalar y gestionar chromedriver automáticamente
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        # Aquí se podrían añadir otros navegadores (firefox, edge)
        else:
            logger.error(f"Navegador '{navegador}' no es soportado.")
            return f"Navegador '{navegador}' no es soportado."

        driver.get(url)
        return f"Navegador '{navegador}' abierto en '{url}'."

    except WebDriverException as e:
        logger.error(f"Error de WebDriver: {e}")
        logger.error("Asegúrate de que el WebDriver para Chrome está instalado y en el PATH.")
        logger.error("Consulta 'docs/user_guide.md' para instrucciones de instalación.")
        driver = None # Resetea el driver si falla
        return "Error: No se pudo iniciar el navegador. ¿Está el WebDriver instalado correctamente?"
    except Exception as e:
        logger.error(f"Un error inesperado ocurrió al abrir el navegador: {e}")
        driver = None
        return "Error: Ocurrió un error inesperado al abrir el navegador."

def navegar_a(url):
    """
    Navega a una nueva URL en el navegador abierto.
    """
    global driver
    if driver is None:
        logger.warning("No hay ningún navegador abierto para navegar.")
        return "No hay ningún navegador abierto. Usa 'abre navegador [url]' primero."

    logger.info(f"Navegando a: {url}")
    try:
        driver.get(url)
        return f"Navegando a '{url}'."
    except Exception as e:
        logger.error(f"Error durante la navegación a '{url}': {e}")
        return f"Error al intentar navegar a '{url}'."

def cerrar_navegador():
    """
    Cierra el navegador y termina la sesión del WebDriver.
    """
    global driver
    if driver is None:
        logger.info("No hay ningún navegador abierto para cerrar.")
        return "No hay ningún navegador abierto."

    try:
        logger.info("Cerrando el navegador...")
        driver.quit()
        driver = None # Limpia la variable global
        return "Navegador cerrado."
    except Exception as e:
        logger.error(f"Error al cerrar el navegador: {e}")
        # Intenta limpiar la variable de todas formas
        driver = None
        return "Error al cerrar el navegador."

def buscar_en_google(termino):
    """
    Realiza una búsqueda en Google en el navegador abierto.
    Si el navegador no está en google.com, navega allí primero.
    """
    global driver
    if driver is None:
        logger.warning("No se puede buscar porque no hay un navegador abierto.")
        return "No hay ningún navegador abierto. Usa 'abre navegador [url]' para empezar."

    logger.info(f"Buscando en Google: '{termino}'")

    try:
        # Si no estamos en Google, vamos primero
        if "google.com" not in driver.current_url:
            driver.get("https://www.google.com")

        # Encuentra el elemento de búsqueda por su nombre ('q' es el nombre estándar del input de búsqueda de Google)
        search_box = driver.find_element(By.NAME, "q")

        # Limpia el cuadro de búsqueda, escribe el término y presiona Enter
        search_box.clear()
        search_box.send_keys(termino)
        search_box.send_keys(Keys.RETURN)

        return f"Búsqueda de '{termino}' realizada."
    except Exception as e:
        logger.error(f"Error al realizar la búsqueda en Google: {e}")
        return f"Error al buscar '{termino}' en Google."
