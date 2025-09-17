import pytest
from backgammon.core.player import (
    Player,
    PoliticaNula,
    PasoMovimiento,
    OpcionMovimiento,
)
from backgammon.core.checker import Checker


class DummyTablero:
    """Tablero simulado para pruebas de Player."""

    def __init__(self):
        self.bar = False
        self.home = False
        self.pip = 42
        self.legal_moves = [OpcionMovimiento([PasoMovimiento(0, 1, 2)], "hash", 1.0)]
        self.applied = False

    def jugador_tiene_en_barra(self, jugador):
        return self.bar

    def jugador_todo_en_home(self, jugador):
        return self.home

    def jugador_pip_count(self, jugador):
        return self.pip

    def enumerar_opciones_legales(self, jugador, dados):
        return self.legal_moves

    def aplicar_movimiento(self, jugador, secuencia):
        self.applied = True


def make_player():
    checkers = [Checker("blancas"), Checker("blancas"), Checker("blancas")]
    return Player(
        player_id="P1",
        nombre="Ricardo",
        color="blancas",
        direccion=1,
        home_points=[0, 1, 2, 3, 4, 5],
        entry_point=0,
        checkers=checkers,
        politica=None,
    )


def test_player_initialization():
    """Testea la inicialización y getters básicos de Player."""
    p = make_player()
    assert p.get_id() == "P1"
    assert p.get_nombre() == "Ricardo"
    assert p.get_color() == "blancas"
    assert p.get_direccion() == 1
    assert 0 in p.get_home_points()
    assert p.get_entry_point() == 0
    assert len(p.get_checkers()) == 3


def test_player_checkers_management():
    """Testea métodos de gestión de fichas en Player."""
    p = make_player()
    c = p.get_checkers()[0]
    p.colocar_checker_en_posicion(c, 5)
    assert c.get_posicion() == 5
    p.mover_checker_a(c, 7)
    assert c.get_posicion() == 7
    p.enviar_checker_a_barra(c)
    assert c.en_barra()
    p.sacar_checker(c)
    assert c.fuera()


def test_player_checkers_filters():
    """Testea los métodos para filtrar fichas por estado."""
    p = make_player()
    c1, c2, c3 = p.get_checkers()
    p.colocar_checker_en_posicion(c1, 1)
    p.enviar_checker_a_barra(c2)
    p.sacar_checker(c3)
    tablero = p.checkers_en_tablero()
    barra = p.checkers_en_barra()
    fuera = p.checkers_fuera()
    assert c1 in tablero and len(tablero) == 1
    assert c2 in barra and len(barra) == 1
    assert c3 in fuera and len(fuera) == 1


def test_player_tablero_delegation():
    """Testea delegación de consultas al tablero."""
    p = make_player()
    dummy = DummyTablero()
    dummy.bar = True
    dummy.home = True
    assert p.tiene_en_barra(dummy) is True
    assert p.todas_en_home(dummy) is True
    assert p.pip_count(dummy) == 42


def test_player_movimientos_legales():
    """Testea obtención de movimientos legales desde el tablero."""
    p = make_player()
    dummy = DummyTablero()
    moves = p.movimientos_legales(dummy, [2, 3])
    assert isinstance(moves, list)
    assert isinstance(moves[0], OpcionMovimiento)


def test_player_elegir_movimiento():
    """Testea selección de movimiento usando la política."""
    p = make_player()
    dummy = DummyTablero()
    opciones = dummy.legal_moves
    secuencia = p.elegir_movimiento(opciones)
    assert secuencia is None  # PoliticaNula no elige


def test_player_confirmar_movimiento():
    """Testea confirmación de movimiento y aplicación en tablero."""
    p = make_player()
    dummy = DummyTablero()
    secuencia = [PasoMovimiento(0, 1, 2)]
    p.confirmar_movimiento(dummy, secuencia)
    assert dummy.applied is True


def test_player_puede_bear_off():
    """Testea la consulta de si el jugador puede hacer bear off."""
    p = make_player()
    dummy = DummyTablero()
    dummy.home = True
    dummy.bar = False
    assert p.puede_bear_off(dummy) is True
    dummy.bar = True
    assert p.puede_bear_off(dummy) is False


def test_player_str_repr():
    """Testea las representaciones __str__ y __repr__."""
    p = make_player()
    s = str(p)
    r = repr(p)
    assert "Player(" in s
    assert "Player(" in r


def test_politicanula_elegir_none():
    """Testea que PoliticaNula siempre retorna None al elegir."""
    politica = PoliticaNula()
    opciones = [OpcionMovimiento([PasoMovimiento(0, 1, 2)], "hash", 1.0)]
    assert politica.elegir(opciones) is None
    assert politica.elegir([]) is None


def test_get_checkers_returns_copy():
    """Testea que get_checkers retorna una copia defensiva de la lista de fichas."""
    p = make_player()
    checkers = p.get_checkers()
    checkers.append(Checker("blancas"))
    # La lista interna no debe verse afectada
    assert len(p.get_checkers()) == 3


def test_gestion_no_altera_otras_fichas():
    """Testea que los métodos de gestión no alteran el estado de otras fichas."""
    p = make_player()
    c1, c2, c3 = p.get_checkers()
    p.colocar_checker_en_posicion(c1, 2)
    p.mover_checker_a(c1, 3)
    p.enviar_checker_a_barra(c1)
    p.sacar_checker(c1)
    # Las otras fichas deben permanecer sin estado alterado
    assert not c2.en_tablero()
    assert not c2.en_barra()
    assert not c2.fuera()
    assert not c3.en_tablero()
    assert not c3.en_barra()
    assert not c3.fuera()
