from src.core.app_manager import abrir_aplicacion, cerrar_aplicacion
from src.core.browser_manager import abrir_navegador, navegar_a, cerrar_navegador, buscar_en_google
from src.core.window_manager import (
    listar_ventanas_abiertas, enfocar_ventana, mover_ventana,
    redimensionar_ventana, minimizar_ventana, maximizar_ventana, organizar_ventanas
)
from src.utils.logger import get_logger
import re

logger = get_logger(__name__)

def main_loop():
    """Bucle principal de la interfaz de línea de comandos."""
    logger.info("Iniciando CLI...")
    print("Bienvenido al Asistente de Automatización de Windows.")
    print("Para ver los comandos disponibles, escribe 'ayuda'.")

    while True:
        command = input("> ").strip().lower()
        if not command:
            continue

        logger.info(f"Comando recibido: '{command}'")

        if command == "salir":
            logger.info("Cerrando CLI...")
            cerrar_navegador()
            break

        if command == "ayuda":
            print("""
Comandos Disponibles:
  - abre [app]                      -> Abre una aplicación (notepad, calculator).
  - cierra [app]                    -> Cierra una aplicación.
  - navega a [url]                  -> Abre el navegador en una URL.
  - busca [termino]                 -> Busca un término en Google.
  - cierra navegador                -> Cierra el navegador.
  - lista ventanas                  -> Muestra las ventanas abiertas.
  - enfoca [titulo]                 -> Pone una ventana en primer plano.
  - minimiza [titulo]               -> Minimiza una ventana.
  - maximiza [titulo]               -> Maximiza una ventana.
  - mueve [titulo] a [x],[y]        -> Mueve una ventana a coordenadas.
  - redimensiona [titulo] a [w]x[h] -> Cambia el tamaño de una ventana.
  - organiza [titulo] en [layout]   -> Organiza una ventana (layouts: izquierda, derecha).
  - salir                           -> Cierra la aplicación.
            """)
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

        if command == "cierra navegador":
            print(cerrar_navegador())
            continue

        # --- Comandos con argumentos complejos ---

        match_move = re.match(r"mueve (.*) a (\d+),(\d+)", command)
        if match_move:
            titulo, x, y = match_move.groups()
            print(mover_ventana(titulo.strip(), x, y))
            continue

        match_resize = re.match(r"redimensiona (.*) a (\d+)x(\d+)", command)
        if match_resize:
            titulo, ancho, alto = match_resize.groups()
            print(redimensionar_ventana(titulo.strip(), ancho, alto))
            continue

        match_organize = re.match(r"organiza (.*) en (izquierda|derecha)", command)
        if match_organize:
            titulo, disposicion = match_organize.groups()
            print(organizar_ventanas(titulo.strip(), disposicion))
            continue

        # --- Comandos con argumentos simples ---

        parts = command.split()
        action = parts[0]

        if len(parts) < 2:
            print("Comando incompleto. Escribe 'ayuda' para ver los comandos.")
            continue

        target = " ".join(parts[1:])

        if action == "abre":
            print(abrir_aplicacion(target))
        elif action == "cierra":
            print(cerrar_aplicacion(target))
        elif action == "navega" and parts[1] == "a":
            url = " ".join(parts[2:])
            result = abrir_navegador(url)
            if "ya está abierto" in result:
                result = navegar_a(url)
            print(result)
        elif action == "busca":
            print(buscar_en_google(target))
        elif action == "enfoca":
            print(enfocar_ventana(target))
        elif action == "minimiza":
            print(minimizar_ventana(target))
        elif action == "maximiza":
            print(maximizar_ventana(target))
        else:
            print(f"Comando '{command}' no reconocido. Escribe 'ayuda' para ver la lista de comandos.")

if __name__ == '__main__':
    main_loop()
