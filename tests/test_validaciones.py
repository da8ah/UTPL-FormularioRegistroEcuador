import pytest

from src.validar_cedula import validar_cedula
from src.validar_correo import validar_correo
from src.validar_nombre_apellido import validar_nombre_apellido
from src.validar_telefono import validar_telefono


@pytest.mark.parametrize(
    ['ci', 'province'],
    [
        ('1900512623', 'Zamora Chinchipe'),
        ('0598384754', 'Cotopaxi'),
        ('1192837484', 'Loja'),
        ('', None),
        ('9999999999', None),
        ('00000000000', None),
        ('00', None)
    ]
)
def test_validate_cedula(ci, province):
    assert validar_cedula(ci) == province


@pytest.mark.parametrize(
    ['email', 'isValid'],
    [
        ('example@mail.xyz', (True, False)),
        ('aalopez@utpl.edu.ec', (True, True)),
        ('', (False, False)),
        ('dad*^das#email.aa.x', (False, False)),
        ('pptorres@gov.ec', (True, False)),
        ('mariodelgado@uv.edu.es', (True, True))
    ]
)
def test_validate_email(email, isValid):
    assert all([a == b for a, b in zip(validar_correo(email), isValid)])


@pytest.mark.parametrize(
    ['name', 'isValid'],
    [
        ('Juan', True),
        ('Juan Gahona', True),
        ('Pedro', True),
        ('', False),
        ('*da%3', False),
        ('7amara', False)
    ]
)
def test_validate_names(name, isValid):
    assert validar_nombre_apellido(name) == isValid


@pytest.mark.parametrize(
    ['phone', 'isValid'],
    [
        ('0959011574', True),
        ('0942342145', True),
        ('2897982', False),
        ('9999999999', True),
        ('094728129923', False),
        ('+5930959001574', True),
        ('+045-231253674', True),
        ('+593 959011574', True)
    ]
)
def test_validate_phones(phone, isValid):
    assert validar_telefono(phone) == isValid
