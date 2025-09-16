import pytest
from backgammon.core.board import Board


def test_board_initialization():
    """Testea que el tablero se inicializa con 24 puntas vacías."""
    board = Board()
    assert hasattr(board, "triangulo")
    assert isinstance(board.triangulo, list)
    assert len(board.triangulo) == 24
    assert all(isinstance(point, list) and len(point) == 0 for point in board.triangulo)


def test_board_display(capsys):
    """Testea que el método display imprime las 24 puntas correctamente."""
    board = Board()
    board.display()
    captured = capsys.readouterr()
    for i in range(1, 25):
        assert f"Punta {i}:" in captured.out