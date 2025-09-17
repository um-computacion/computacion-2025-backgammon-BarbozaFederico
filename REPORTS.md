# Automated Reports

## Coverage Report

```text
..................                                                       [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.10.18-final-0 _______________

Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
backgammon/__init__.py                 0      0   100%
backgammon/cli/__init__.py             0      0   100%
backgammon/core/__init__.py            0      0   100%
backgammon/core/backgammon.py          0      0   100%
backgammon/core/board.py               6      0   100%
backgammon/core/checker.py            44      4    91%   100, 139-152, 156
backgammon/core/dice.py               11      6    45%   24-25, 36-38, 49
backgammon/core/player.py             80      1    99%   370
backgammon/pygame_ui/__init__.py       0      0   100%
----------------------------------------------------------------
TOTAL                                141     11    92%
Coverage XML written to file cobertura.xml
18 passed in 0.16s

```

## Pylint Report

```text
************* Module backgammon.__init__
backgammon/__init__.py:4:0: C0304: Final newline missing (missing-final-newline)
************* Module backgammon.core.board
backgammon/core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/board.py:1:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module backgammon.core.checker
backgammon/core/checker.py:156:0: C0301: Line too long (155/100) (line-too-long)
backgammon/core/checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon.core.dice
backgammon/core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon.core.player
backgammon/core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/player.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:57:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:58:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:63:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:74:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:68:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/player.py:87:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:87:21: W0613: Unused argument 'opciones' (unused-argument)
backgammon/core/player.py:79:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/player.py:91:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
backgammon/core/player.py:177:4: R0913: Too many arguments (9/5) (too-many-arguments)
backgammon/core/player.py:177:4: R0917: Too many positional arguments (9/5) (too-many-positional-arguments)
backgammon/core/player.py:91:0: R0904: Too many public methods (21/20) (too-many-public-methods)
************* Module tests.test_board
tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module tests.test_checker
tests/test_checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module tests.test_dice
tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_dice.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_player
tests/test_player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_player.py:15:8: C0104: Disallowed name "bar" (disallowed-name)
tests/test_player.py:21:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:21:37: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:24:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:24:35: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:27:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:27:32: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:30:40: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:30:49: W0613: Unused argument 'dados' (unused-argument)
tests/test_player.py:33:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:33:33: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:33:42: W0613: Unused argument 'secuencia' (unused-argument)
tests/test_player.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:1:0: W0611: Unused import pytest (unused-import)

-----------------------------------
Your code has been rated at 8.71/10


```
