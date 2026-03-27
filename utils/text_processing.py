# utils/text_processing.py

# Basic Sanskrit cleaner + transliteration (safe fallback)

def clean_sanskrit(text):
    if not text:
        return ""
    return text.strip()


def transliterate_iast(text):
    """
    Simple fallback transliteration.
    (You can upgrade later using indic-transliteration)
    """
    return text.lower()


def process_text(text):
    """
    Main pipeline function
    """
    text = clean_sanskrit(text)
    return transliterate_iast(text)
