import re


def validar_telefono(telefono: str):
    telefono = re.sub(r'[\s\_\-\\/.,\'\"\(\)]', '', telefono)
    lenghtTel = len(telefono)

    matches = re.compile(r'([+]\d{3})?\d{9,10}').match(telefono)

    # Se comprueba que exista un match
    if (matches is None):
        return False

    # Si existe el primer grupo '+000' el numero no debe ser
    # mayor a 14 digitos
    if (matches.group(1) and lenghtTel > 14):
        return False

    # Si no existe el primer grupo '+000' el numero no debe ser
    # mayor a 10 ni menor a 9
    if (matches.group(1) is None and (lenghtTel > 10 or lenghtTel < 9)):
        return False

    # Si pasa todo es valido
    return True
