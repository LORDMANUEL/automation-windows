import json
import os
from src.utils.logger import get_logger
from .intent_classifier import classify_intent

logger = get_logger(__name__)

class CommandParser:
    def __init__(self):
        self.commands = self._load_commands()
        if not self.commands:
            raise ValueError("No se pudo cargar el diccionario de comandos.")

    def _load_commands(self):
        """Carga el diccionario de intenciones desde el archivo JSON."""
        path = os.path.join('data', 'commands.json')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"El archivo de comandos no se encontró en: {path}")
            return None
        except json.JSONDecodeError:
            logger.error(f"Error al decodificar el archivo de comandos: {path}")
            return None

    def parse_command(self, user_input):
        """
        Analiza la entrada del usuario para encontrar la intención y la entidad.
        """
        logger.info(f"Analizando comando: '{user_input}'")

        # Clasifica la intención basada en las palabras clave
        intent = classify_intent(user_input, self.commands)

        if not intent:
            logger.warning(f"No se pudo clasificar la intención para el comando: '{user_input}'")
            return None, None

        # Si la intención no requiere una entidad, devolvemos la acción directamente
        if not intent.get('entity'):
            return intent['function'], None

        # Extrae la entidad (el texto que viene después de la palabra clave)
        # Esto es una implementación simple; se puede mejorar con NLP más avanzado
        entity = self._extract_entity(user_input, intent['keywords'])

        if not entity:
            logger.warning(f"No se pudo extraer la entidad para la intención '{intent['name']}' del comando '{user_input}'")
            return None, None

        return intent['function'], entity

    def _extract_entity(self, user_input, keywords):
        """
        Extrae la entidad de la entrada del usuario.
        Ejemplo: "abre notepad" -> keyword="abre", entidad="notepad"
        """
        user_input_lower = user_input.lower()
        for keyword in sorted(keywords, key=len, reverse=True):
            if user_input_lower.startswith(keyword):
                # La entidad es lo que viene después de la palabra clave
                entity = user_input[len(keyword):].strip()
                if entity:
                    return entity
        return None
