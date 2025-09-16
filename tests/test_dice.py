from backgammon.core.board import Board
from backgammon.core.dice import Dice


def test_import_board_and_dice():
    assert Board is not None
    assert Dice is not None
