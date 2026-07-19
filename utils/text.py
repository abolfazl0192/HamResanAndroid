import arabic_reshaper
from bidi.algorithm import get_display


def fa(text):
    if not text:
        return ""

    reshaped = arabic_reshaper.reshape(str(text))
    return get_display(reshaped)