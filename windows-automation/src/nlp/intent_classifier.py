from src.utils.logger import get_logger

logger = get_logger(__name__)

def classify_intent(user_input, commands_data):
    """
    Clasifica la intención del usuario comparando la entrada con las palabras clave.
    """
    user_input_lower = user_input.lower()

    # Buscamos la coincidencia más larga primero para evitar ambigüedades
    # (ej. "cierra navegador" debe coincidir antes que "cierra")

    best_match = None
    longest_keyword_len = 0

    for intent in commands_data.get('intents', []):
        for keyword in intent.get('keywords', []):
            if user_input_lower.startswith(keyword):
                if len(keyword) > longest_keyword_len:
                    longest_keyword_len = len(keyword)
                    best_match = intent

    if best_match:
        logger.info(f"Intención clasificada como '{best_match['name']}' con la palabra clave '{user_input_lower[:longest_keyword_len]}'")
    else:
        logger.warning(f"No se encontró una intención para la entrada: '{user_input}'")

    return best_match
