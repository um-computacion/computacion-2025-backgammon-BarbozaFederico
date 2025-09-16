from backgammon.core.checker import Checker


def test_checker_initial_state():
    """Testea que una ficha recién creada esté fuera del tablero, barra y bear off."""
    checker = Checker(color="blancas")
    assert not checker.en_tablero()
    assert not checker.en_barra()
    assert not checker.fuera()
    assert checker.get_color() == "blancas"
    assert checker.get_posicion() is None


def test_colocar_en_posicion():
    """Testea colocar la ficha en una posición válida."""
    checker = Checker(color="negras")
    checker.colocar_en_posicion(5)
    assert checker.en_tablero()
    assert checker.get_posicion() == 5
    assert not checker.en_barra()
    assert not checker.fuera()


def test_enviar_a_barra():
    """Testea enviar la ficha a la barra."""
    checker = Checker(color="blancas")
    checker.colocar_en_posicion(10)
    checker.enviar_a_barra()
    assert checker.en_barra()
    assert not checker.en_tablero()
    assert not checker.fuera()
    assert checker.get_posicion() is None


def test_sacar():
    """Testea sacar la ficha del tablero (bear off)."""
    checker = Checker(color="negras")
    checker.colocar_en_posicion(23)
    checker.sacar()
    assert checker.fuera()
    assert not checker.en_tablero()
    assert not checker.en_barra()
    assert checker.get_posicion() is None


def test_resetear():
    """Testea el reseteo de estado de la ficha."""
    checker = Checker(color="blancas")
    checker.colocar_en_posicion(7)
    checker.enviar_a_barra()
    checker.sacar()
    checker.resetear()
    assert not checker.en_tablero()
    assert not checker.en_barra()
    assert not checker.fuera()
    assert checker.get_posicion() is None
