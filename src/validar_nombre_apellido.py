import re


def validar_nombre_apellido(nombre):
    return re.compile(
        r'(^[A-Za-zÑ]+){1}(\s[A-Za-zÑ]+){1,4}$'
    ).match(nombre) is not None
