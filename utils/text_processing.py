from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import re

def to_iast(text):
    return transliterate(text, sanscript.DEVANAGARI, sanscript.IAST)

def syllabify(text):
    vowels = "aāiīuūeēoōṛ"
    pattern = r'[^{}]*[{}]+'.format(vowels, vowels)
    return re.findall(pattern, text)