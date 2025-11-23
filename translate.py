from deep_translator import GoogleTranslator

def batch_translate(items, src="en", tgt="es", delimiter="|||"):
    if not items:
        return []

    # Make sure the delimiter does not accidentally appear in the text
    safe_delimiter = delimiter
    while any(safe_delimiter in item for item in items):
        safe_delimiter += "_"

    translator = GoogleTranslator(source=src, target=tgt)

    joined = safe_delimiter.join(items)
    translated_joined = translator.translate(joined)

    return translated_joined.split(safe_delimiter)
