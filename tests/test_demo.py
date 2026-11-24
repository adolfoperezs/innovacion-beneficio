# Caso sembrado de ejemplo: horas y pesos nunca se suman

def estado(horas, dinero):
    if horas is None:
        return "REVISAR"
    if dinero is None:
        return "VALIDAR"
    return "OK"


def test_ok():
    assert estado(120, 1500000) == "OK"


def test_sin_medicion():
    assert estado(None, 1500000) == "REVISAR"


def test_solo_horas():
    assert estado(120, None) == "VALIDAR"
