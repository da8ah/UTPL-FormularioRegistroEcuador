import re


def validar_telefono(telefono: str):
    telefono = re.sub(r'[\s\_\-\\/.,\'\"\(\)]', '', telefono)
    return re.compile(
        r'([+]\d{3})?\d{9,10}'
    ).match(telefono) is not None
