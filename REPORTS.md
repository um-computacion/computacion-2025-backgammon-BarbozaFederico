# Automated Reports
## Coverage Report
```text
...                                                                      [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.10.18-final-0 _______________

Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
backgammon/__init__.py                 0      0   100%
backgammon/cli/__init__.py             0      0   100%
backgammon/core/__init__.py            0      0   100%
backgammon/core/backgammon.py          0      0   100%
backgammon/core/board.py               6      0   100%
backgammon/core/dice.py               11      6    45%   24-25, 36-38, 49
backgammon/core/player.py              2      2     0%   1-2
backgammon/pygame_ui/__init__.py       0      0   100%
----------------------------------------------------------------
TOTAL                                 19      8    58%
Coverage XML written to file cobertura.xml
3 passed in 0.05s

```
## Pylint Report
```text
************* Module backgammon.__init__
backgammon/__init__.py:4:0: C0304: Final newline missing (missing-final-newline)
************* Module backgammon.core.board
backgammon/core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/board.py:1:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module backgammon.core.dice
backgammon/core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon.core.player
backgammon/core/player.py:2:0: C0304: Final newline missing (missing-final-newline)
backgammon/core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/player.py:1:0: C0115: Missing class docstring (missing-class-docstring)
backgammon/core/player.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module tests.conftest
tests/conftest.py:11:0: C0304: Final newline missing (missing-final-newline)
************* Module tests.test_board
tests/test_board.py:20:0: C0304: Final newline missing (missing-final-newline)
tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_board.py:1:0: W0611: Unused import pytest (unused-import)
************* Module tests.test_dice
tests/test_dice.py:6:0: C0304: Final newline missing (missing-final-newline)
tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_dice.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 6.51/10


```
