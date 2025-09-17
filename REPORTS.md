# Automated Reports
## Coverage Report
```text

==================================== ERRORS ====================================
____________________ ERROR collecting tests/test_checker.py ____________________
ImportError while importing test module '/home/runner/work/computacion-2025-backgammon-BarbozaFederico/computacion-2025-backgammon-BarbozaFederico/tests/test_checker.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.10.18/x64/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_checker.py:1: in <module>
    from backgammon.core.checker import Checker
backgammon/core/checker.py:3: in <module>
    from backgammon.core.player import Player
backgammon/core/player.py:5: in <module>
    from backgammon.core.checker import Checker
E   ImportError: cannot import name 'Checker' from partially initialized module 'backgammon.core.checker' (most likely due to a circular import) (/home/runner/work/computacion-2025-backgammon-BarbozaFederico/computacion-2025-backgammon-BarbozaFederico/backgammon/core/checker.py)
=========================== short test summary info ============================
ERROR tests/test_checker.py
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
1 error in 0.07s

```
## Pylint Report
```text
************* Module backgammon.__init__
backgammon/__init__.py:4:0: C0304: Final newline missing (missing-final-newline)
************* Module backgammon.core.board
backgammon/core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/board.py:1:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module backgammon.core.checker
backgammon/core/checker.py:155:0: C0301: Line too long (155/100) (line-too-long)
backgammon/core/checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon.core.dice
backgammon/core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon.core.player
backgammon/core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/player.py:55:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:57:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:58:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:62:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:73:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:67:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/player.py:86:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:86:21: W0613: Unused argument 'opciones' (unused-argument)
backgammon/core/player.py:78:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/player.py:90:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
backgammon/core/player.py:176:4: R0913: Too many arguments (9/5) (too-many-arguments)
backgammon/core/player.py:176:4: R0917: Too many positional arguments (9/5) (too-many-positional-arguments)
backgammon/core/player.py:90:0: R0904: Too many public methods (21/20) (too-many-public-methods)
************* Module tests.test_board
tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module tests.test_checker
tests/test_checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module tests.test_dice
tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_dice.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_player
tests/test_player.py:1:0: R0401: Cyclic import (backgammon.core.checker -> backgammon.core.player) (cyclic-import)

-----------------------------------
Your code has been rated at 8.80/10


```
