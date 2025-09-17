import pytest
from backgammon.core.board import Board
from backgammon.core.checker import Checker


class DummyPlayer:
    """Dummy player for board tests."""

    def __init__(self, color="blancas"):
        self.color = color


def make_checker(color="blancas"):
    return Checker(color)


def test_board_initialization():
    """Testea que el tablero se inicializa correctamente."""
    board = Board()
    assert isinstance(board.points, list)
    assert len(board.points) == 24
    assert all(isinstance(point, list) and len(point) == 0 for point in board.points)
    assert isinstance(board.bar, dict)
    assert isinstance(board.borne_off, dict)
    assert board.players == []
    assert board.dice is None


def test_add_player():
    """Testea agregar jugadores al tablero."""
    board = Board()
    p1 = DummyPlayer("blancas")
    p2 = DummyPlayer("negras")
    board.add_player(p1)
    board.add_player(p2)
    assert p1 in board.players
    assert p2 in board.players
    assert len(board.players) == 2


def test_place_checker():
    """Testea colocar una ficha en una punta específica."""
    board = Board()
    checker = make_checker("blancas")
    board.place_checker(checker, 5)
    assert checker in board.points[5]
    assert checker.get_posicion() == 5


def test_move_checker():
    """Testea mover una ficha de una punta a otra."""
    board = Board()
    checker = make_checker("blancas")
    board.place_checker(checker, 2)
    board.move_checker(checker, 2, 10)
    assert checker in board.points[10]
    assert checker.get_posicion() == 10
    assert checker not in board.points[2]


def test_send_to_bar():
    """Testea enviar una ficha a la barra."""
    board = Board()
    checker = make_checker("negras")
    board.send_to_bar(checker)
    assert checker in board.bar["negras"]
    assert checker.en_barra()


def test_bear_off_checker():
    """Testea sacar una ficha del tablero (bear off)."""
    board = Board()
    checker = make_checker("blancas")
    board.bear_off_checker(checker)
    assert checker in board.borne_off["blancas"]
    assert checker.fuera()


def test_get_checkers_on_point():
    """Testea obtener fichas en una punta específica."""
    board = Board()
    checker1 = make_checker("blancas")
    checker2 = make_checker("blancas")
    board.place_checker(checker1, 0)
    board.place_checker(checker2, 0)
    result = board.get_checkers_on_point(0)
    assert checker1 in result and checker2 in result
    assert len(result) == 2
    assert board.get_checkers_on_point(23) == []
    assert board.get_checkers_on_point(24) == []


def test_get_bar_and_borne_off():
    """Testea obtener fichas en barra y fuera."""
    board = Board()
    c1 = make_checker("blancas")
    c2 = make_checker("negras")
    board.send_to_bar(c1)
    board.send_to_bar(c2)
    board.bear_off_checker(c1)
    assert c1 in board.get_bar("blancas")
    assert c2 in board.get_bar("negras")
    assert c1 in board.get_borne_off("blancas")
    assert board.get_borne_off("negras") == []


def test_display(capsys):
    """Testea que el método display imprime el estado del tablero."""
    board = Board()
    c1 = make_checker("blancas")
    c2 = make_checker("negras")
    board.place_checker(c1, 0)
    board.place_checker(c2, 23)
    board.send_to_bar(c1)
    board.bear_off_checker(c2)
    board.display()
    captured = capsys.readouterr()
    assert "Tablero:" in captured.out
    assert "Barra:" in captured.out
    assert "Fuera (Bear Off):" in captured.out
    assert "Punta 1:" in captured.out
    assert "Punta 24:" in captured.out
    assert "blancas:" in captured.out
    assert "negras:" in captured.out


def test_reset():
    """Testea el reseteo del tablero."""
    board = Board()
    c1 = make_checker("blancas")
    board.place_checker(c1, 5)
    board.send_to_bar(c1)
    board.bear_off_checker(c1)
    board.add_player(DummyPlayer())
    board.dice = "dummy"
    board.reset()
    assert all(len(point) == 0 for point in board.points)
    assert board.bar["blancas"] == []
    assert board.bar["negras"] == []
    assert board.borne_off["blancas"] == []
    assert board.borne_off["negras"] == []
    assert board.players == []
    assert board.dice is None
