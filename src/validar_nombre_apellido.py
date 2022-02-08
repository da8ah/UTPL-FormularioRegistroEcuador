import re


def validar_nombre_apellido(nombre: str):
    return re.compile(
        r'(^[A-Za-zÑñ]+){1}(\s[A-Za-zÑñ]+)*$'
    ).match(nombre) is not None
