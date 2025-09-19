# Automated Reports
## Coverage Report
```text
.......................................                                  [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.10.18-final-0 _______________

Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
backgammon/__init__.py                 0      0   100%
backgammon/cli/__init__.py             0      0   100%
backgammon/cli/console.py             45     45     0%   1-127
backgammon/core/__init__.py            0      0   100%
backgammon/core/backgammon.py         49      0   100%
backgammon/core/board.py             229    166    28%   240-241, 258-273, 289-315, 330-333, 348-385, 405-445, 473-528, 550-620, 648-674, 694-706, 727-734
backgammon/core/checker.py            44      0   100%
backgammon/core/dice.py               11      0   100%
backgammon/core/move.py               18     18     0%   1-28
backgammon/core/player.py             80      1    99%   370
backgammon/pygame_ui/__init__.py       0      0   100%
----------------------------------------------------------------
TOTAL                                476    230    52%
Coverage XML written to file cobertura.xml
39 passed in 0.35s

```
## Pylint Report
```text
************* Module backgammon.__init__
backgammon/__init__.py:4:0: C0304: Final newline missing (missing-final-newline)
************* Module backgammon.cli.console
backgammon/cli/console.py:127:0: C0304: Final newline missing (missing-final-newline)
backgammon/cli/console.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/cli/console.py:117:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
backgammon/cli/console.py:98:26: W0613: Unused argument 'player' (unused-argument)
backgammon/cli/console.py:2:0: W0611: Unused OpcionMovimiento imported from backgammon.core.player (unused-import)
backgammon/cli/console.py:2:0: W0611: Unused SecuenciaMovimiento imported from backgammon.core.player (unused-import)
************* Module backgammon.core.backgammon
backgammon/core/backgammon.py:166:0: C0301: Line too long (107/100) (line-too-long)
backgammon/core/backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/backgammon.py:93:16: W0212: Access to a protected member _player of a client class (protected-access)
backgammon/core/backgammon.py:121:24: W0612: Unused variable 'i' (unused-variable)
backgammon/core/backgammon.py:1:0: W0611: Unused Optional imported from typing (unused-import)
************* Module backgammon.core.board
backgammon/core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/board.py:66:8: C0104: Disallowed name "bar" (disallowed-name)
backgammon/core/board.py:206:8: C0206: Consider iterating with .items() (consider-using-dict-items)
backgammon/core/board.py:209:8: C0206: Consider iterating with .items() (consider-using-dict-items)
backgammon/core/board.py:266:16: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
backgammon/core/board.py:300:12: R1724: Unnecessary "elif" after "continue", remove the leading "el" from "elif" (no-else-continue)
backgammon/core/board.py:330:8: C0415: Import outside toplevel (backgammon.core.player.SecuenciaMovimiento, backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
backgammon/core/board.py:330:8: W0611: Unused PasoMovimiento imported from backgammon.core.player (unused-import)
backgammon/core/board.py:405:8: C0415: Import outside toplevel (backgammon.core.player.OpcionMovimiento, backgammon.core.player.PasoMovimiento, backgammon.core.player.SecuenciaMovimiento) (import-outside-toplevel)
backgammon/core/board.py:410:8: C0415: Import outside toplevel (copy) (import-outside-toplevel)
backgammon/core/board.py:447:4: R0914: Too many local variables (20/15) (too-many-locals)
backgammon/core/board.py:473:8: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
backgammon/core/board.py:474:8: C0415: Import outside toplevel (copy) (import-outside-toplevel)
backgammon/core/board.py:492:28: W0212: Access to a protected member _generar_secuencias_movimiento of a client class (protected-access)
backgammon/core/board.py:502:16: W0212: Access to a protected member _aplicar_paso_movimiento of a client class (protected-access)
backgammon/core/board.py:509:28: W0212: Access to a protected member _generar_secuencias_movimiento of a client class (protected-access)
backgammon/core/board.py:550:8: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
backgammon/core/board.py:585:20: R1724: Unnecessary "elif" after "continue", remove the leading "el" from "elif" (no-else-continue)
backgammon/core/board.py:625:8: W0613: Unused argument 'desde' (unused-argument)
************* Module backgammon.core.checker
backgammon/core/checker.py:156:0: C0301: Line too long (155/100) (line-too-long)
backgammon/core/checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon.core.dice
backgammon/core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module backgammon.core.move
backgammon/core/move.py:4:0: C0301: Line too long (129/100) (line-too-long)
backgammon/core/move.py:28:0: C0301: Line too long (109/100) (line-too-long)
backgammon/core/move.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/move.py:3:0: C0115: Missing class docstring (missing-class-docstring)
backgammon/core/move.py:4:4: R0913: Too many arguments (6/5) (too-many-arguments)
backgammon/core/move.py:4:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
backgammon/core/move.py:1:0: W0611: Unused Optional imported from typing (unused-import)
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
************* Module tests.test_backgammon
tests/test_backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_backgammon.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_backgammon.py:30:11: C1803: "game.players == []" can be simplified to "not game.players", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_backgammon.py:1:0: W0611: Unused import pytest (unused-import)
************* Module tests.test_board
tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_board.py:6:0: R0903: Too few public methods (0/2) (too-few-public-methods)
tests/test_board.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:25:11: C1803: "board.players == []" can be simplified to "not board.players", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:89:11: C1803: "board.get_checkers_on_point(...) == []" can be simplified to "not board.get_checkers_on_point(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:90:11: C1803: "board.get_checkers_on_point(...) == []" can be simplified to "not board.get_checkers_on_point(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:104:11: C1803: "board.get_borne_off(...) == []" can be simplified to "not board.get_borne_off(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:138:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:139:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:140:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:141:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:142:11: C1803: "board.players == []" can be simplified to "not board.players", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:1:0: W0611: Unused import pytest (unused-import)
************* Module tests.test_checker
tests/test_checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_checker.py:62:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_checker.py:62:4: R0903: Too few public methods (0/2) (too-few-public-methods)
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
tests/test_player.py:1:0: R0801: Similar lines in 2 files
==backgammon.cli.console:[47:54]
==tests.test_backgammon:[9:16]
                "color": "blancas",
                "direccion": 1,
                "home_points": [18, 19, 20, 21, 22, 23],
                "entry_point": 0,
            },
            {
                "id": "P2", (duplicate-code)

-----------------------------------
Your code has been rated at 8.90/10


```
