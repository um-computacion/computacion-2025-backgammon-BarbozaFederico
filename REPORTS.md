# Automated Reports
## Coverage Report
```text

==================================== ERRORS ====================================
_____________________ ERROR collecting tests/test_move.py ______________________
ImportError while importing test module '/home/runner/work/computacion-2025-backgammon-BarbozaFederico/computacion-2025-backgammon-BarbozaFederico/tests/test_move.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.10.18/x64/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_move.py:1: in <module>
    from backgammon.core.move import Move
E   ImportError: cannot import name 'Move' from 'backgammon.core.move' (/home/runner/work/computacion-2025-backgammon-BarbozaFederico/computacion-2025-backgammon-BarbozaFederico/backgammon/core/move.py)
=========================== short test summary info ============================
ERROR tests/test_move.py
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
1 error in 0.27s

```
## Pylint Report
```text
************* Module cli.console
backgammon/cli/console.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/cli/console.py:1:0: E0401: Unable to import 'backgammon.core.backgammon' (import-error)
backgammon/cli/console.py:2:0: E0401: Unable to import 'backgammon.core.player' (import-error)
backgammon/cli/console.py:117:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
backgammon/cli/console.py:98:26: W0613: Unused argument 'player' (unused-argument)
backgammon/cli/console.py:2:0: W0611: Unused OpcionMovimiento imported from backgammon.core.player (unused-import)
backgammon/cli/console.py:2:0: W0611: Unused SecuenciaMovimiento imported from backgammon.core.player (unused-import)
************* Module core.backgammon
backgammon/core/backgammon.py:180:0: C0301: Line too long (107/100) (line-too-long)
backgammon/core/backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/backgammon.py:2:0: E0401: Unable to import 'backgammon.core.player' (import-error)
backgammon/core/backgammon.py:3:0: E0401: Unable to import 'backgammon.core.checker' (import-error)
backgammon/core/backgammon.py:4:0: E0401: Unable to import 'backgammon.core.dice' (import-error)
backgammon/core/backgammon.py:5:0: E0401: Unable to import 'backgammon.core.board' (import-error)
backgammon/core/backgammon.py:93:16: W0212: Access to a protected member _player of a client class (protected-access)
************* Module core.board
backgammon/core/board.py:486:0: C0325: Unnecessary parens after '=' keyword (superfluous-parens)
backgammon/core/board.py:514:0: W0311: Bad indentation. Found 21 spaces, expected 20 (bad-indentation)
backgammon/core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/board.py:66:8: C0104: Disallowed name "bar" (disallowed-name)
backgammon/core/board.py:213:8: C0206: Consider iterating with .items() (consider-using-dict-items)
backgammon/core/board.py:216:8: C0206: Consider iterating with .items() (consider-using-dict-items)
backgammon/core/board.py:273:16: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
backgammon/core/board.py:307:12: R1724: Unnecessary "elif" after "continue", remove the leading "el" from "elif" (no-else-continue)
backgammon/core/board.py:337:8: E0401: Unable to import 'backgammon.core.player' (import-error)
backgammon/core/board.py:337:8: C0415: Import outside toplevel (backgammon.core.player.SecuenciaMovimiento, backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
backgammon/core/board.py:337:8: W0611: Unused PasoMovimiento imported from backgammon.core.player (unused-import)
backgammon/core/board.py:394:4: R0914: Too many local variables (24/15) (too-many-locals)
backgammon/core/board.py:401:8: E0401: Unable to import 'backgammon.core.player' (import-error)
backgammon/core/board.py:401:8: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
backgammon/core/board.py:472:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
backgammon/core/board.py:394:4: R0912: Too many branches (25/12) (too-many-branches)
backgammon/core/board.py:394:4: R0915: Too many statements (55/50) (too-many-statements)
backgammon/core/board.py:498:16: W0612: Unused variable 'can_bear_off_inexact' (unused-variable)
backgammon/core/board.py:531:4: R0911: Too many return statements (7/6) (too-many-return-statements)
backgammon/core/board.py:669:0: C0115: Missing class docstring (missing-class-docstring)
backgammon/core/board.py:669:0: C0103: Class name "prueba1" doesn't conform to PascalCase naming style (invalid-name)
backgammon/core/board.py:669:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module core.checker
backgammon/core/checker.py:156:0: C0301: Line too long (155/100) (line-too-long)
backgammon/core/checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module core.dice
backgammon/core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module core.move
backgammon/core/move.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/move.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/move.py:57:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/move.py:58:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/move.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/move.py:60:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/move.py:64:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/move.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/move.py:69:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/move.py:88:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/move.py:88:21: W0613: Unused argument 'opciones' (unused-argument)
backgammon/core/move.py:80:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/move.py:92:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
backgammon/core/move.py:178:4: R0913: Too many arguments (9/5) (too-many-arguments)
backgammon/core/move.py:178:4: R0917: Too many positional arguments (9/5) (too-many-positional-arguments)
backgammon/core/move.py:92:0: R0904: Too many public methods (21/20) (too-many-public-methods)
************* Module core.player
backgammon/core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/player.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:57:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:58:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:60:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:64:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:69:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/player.py:88:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:88:21: W0613: Unused argument 'opciones' (unused-argument)
backgammon/core/player.py:80:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/player.py:92:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
backgammon/core/player.py:178:4: R0913: Too many arguments (9/5) (too-many-arguments)
backgammon/core/player.py:178:4: R0917: Too many positional arguments (9/5) (too-many-positional-arguments)
backgammon/core/player.py:92:0: R0904: Too many public methods (21/20) (too-many-public-methods)
************* Module pygame_ui.ui
backgammon/pygame_ui/ui.py:455:0: C0301: Line too long (109/100) (line-too-long)
backgammon/pygame_ui/ui.py:519:0: C0301: Line too long (117/100) (line-too-long)
backgammon/pygame_ui/ui.py:615:0: C0301: Line too long (104/100) (line-too-long)
backgammon/pygame_ui/ui.py:638:0: C0301: Line too long (106/100) (line-too-long)
backgammon/pygame_ui/ui.py:678:0: C0301: Line too long (108/100) (line-too-long)
backgammon/pygame_ui/ui.py:709:0: C0301: Line too long (133/100) (line-too-long)
backgammon/pygame_ui/ui.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/pygame_ui/ui.py:5:0: E0401: Unable to import 'backgammon.core.backgammon' (import-error)
backgammon/pygame_ui/ui.py:6:0: E0401: Unable to import 'backgammon.core.player' (import-error)
backgammon/pygame_ui/ui.py:46:0: R0902: Too many instance attributes (27/7) (too-many-instance-attributes)
backgammon/pygame_ui/ui.py:55:8: E1101: Module 'pygame' has no 'init' member (no-member)
backgammon/pygame_ui/ui.py:189:4: R0914: Too many local variables (26/15) (too-many-locals)
backgammon/pygame_ui/ui.py:189:4: R0912: Too many branches (14/12) (too-many-branches)
backgammon/pygame_ui/ui.py:217:19: W0612: Unused variable 'checker' (unused-variable)
backgammon/pygame_ui/ui.py:293:50: E1101: Module 'pygame' has no 'SRCALPHA' member (no-member)
backgammon/pygame_ui/ui.py:338:12: W0612: Unused variable 'color' (unused-variable)
backgammon/pygame_ui/ui.py:414:29: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
backgammon/pygame_ui/ui.py:442:29: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
backgammon/pygame_ui/ui.py:497:15: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
backgammon/pygame_ui/ui.py:546:12: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
backgammon/pygame_ui/ui.py:590:4: R0913: Too many arguments (7/5) (too-many-arguments)
backgammon/pygame_ui/ui.py:590:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
backgammon/pygame_ui/ui.py:627:25: E1101: Module 'pygame' has no 'MOUSEBUTTONDOWN' member (no-member)
backgammon/pygame_ui/ui.py:687:33: E1101: Module 'pygame' has no 'QUIT' member (no-member)
backgammon/pygame_ui/ui.py:697:41: E1101: Module 'pygame' has no 'MOUSEBUTTONDOWN' member (no-member)
backgammon/pygame_ui/ui.py:725:8: E1101: Module 'pygame' has no 'quit' member (no-member)
backgammon/pygame_ui/ui.py:682:4: R0912: Too many branches (14/12) (too-many-branches)
backgammon/pygame_ui/ui.py:46:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/pygame_ui/ui.py:2:0: C0411: standard import "sys" should be placed before third party import "pygame" (wrong-import-order)
backgammon/pygame_ui/ui.py:3:0: C0411: standard import "time" should be placed before third party import "pygame" (wrong-import-order)
backgammon/pygame_ui/ui.py:4:0: C0411: standard import "random" should be placed before third party import "pygame" (wrong-import-order)
backgammon/pygame_ui/ui.py:6:0: W0611: Unused PasoMovimiento imported from backgammon.core.player (unused-import)
backgammon/pygame_ui/ui.py:6:0: W0611: Unused SecuenciaMovimiento imported from backgammon.core.player (unused-import)
************* Module test_backgammon
tests/test_backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_backgammon.py:2:0: E0401: Unable to import 'backgammon.core.backgammon' (import-error)
tests/test_backgammon.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_backgammon.py:1:0: W0611: Unused import pytest (unused-import)
************* Module test_board
tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_board.py:2:0: E0401: Unable to import 'backgammon.core.board' (import-error)
tests/test_board.py:3:0: E0401: Unable to import 'backgammon.core.checker' (import-error)
tests/test_board.py:18:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:21:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:24:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:27:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:33:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:160:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:169:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:188:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:200:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:213:4: W0212: Access to a protected member _home_points of a client class (protected-access)
tests/test_board.py:224:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:234:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:235:11: W0212: Access to a protected member _es_captura of a client class (protected-access)
tests/test_board.py:239:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:275:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:273:4: E0401: Unable to import 'backgammon.core.player' (import-error)
tests/test_board.py:273:4: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
tests/test_board.py:275:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:276:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:275:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_board.py:281:8: W0212: Access to a protected member _aplicar_paso_movimiento of a client class (protected-access)
tests/test_board.py:289:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:287:4: E0401: Unable to import 'backgammon.core.player' (import-error)
tests/test_board.py:287:4: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
tests/test_board.py:289:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:290:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:289:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_board.py:298:4: W0212: Access to a protected member _aplicar_paso_movimiento of a client class (protected-access)
tests/test_board.py:307:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:307:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:308:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:311:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:314:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:317:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:320:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:323:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:323:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:334:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:334:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:335:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:338:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:341:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:344:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:347:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:350:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:350:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:353:13: W0212: Access to a protected member _generar_secuencias_movimiento of a client class (protected-access)
tests/test_board.py:362:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:360:4: E0401: Unable to import 'backgammon.core.player' (import-error)
tests/test_board.py:360:4: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
tests/test_board.py:362:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:363:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:366:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:369:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:372:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:375:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:378:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:378:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:384:12: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
tests/test_board.py:360:4: W0611: Unused PasoMovimiento imported from backgammon.core.player (unused-import)
tests/test_board.py:392:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:392:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:393:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:396:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:396:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:399:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:406:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:406:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:407:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:410:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:410:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:413:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:414:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:421:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:421:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:422:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:421:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_board.py:426:11: W0212: Access to a protected member _es_captura of a client class (protected-access)
tests/test_board.py:430:11: W0212: Access to a protected member _es_captura of a client class (protected-access)
tests/test_board.py:433:11: W0212: Access to a protected member _es_captura of a client class (protected-access)
tests/test_board.py:440:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:440:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:441:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:440:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_board.py:444:8: W0212: Access to a protected member _calcular_hash_secuencia of a client class (protected-access)
tests/test_board.py:523:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:523:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:523:4: R0903: Too few public methods (0/2) (too-few-public-methods)
tests/test_board.py:534:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:534:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:535:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:538:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:541:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:544:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:547:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:550:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:550:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:561:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:561:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:562:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:565:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:568:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:571:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:574:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:577:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:577:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:580:13: W0212: Access to a protected member _generar_secuencias_movimiento of a client class (protected-access)
tests/test_board.py:588:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:588:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:589:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:592:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:595:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:598:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:601:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:604:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:604:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:607:12: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
tests/test_board.py:615:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:615:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:616:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:619:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:619:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:623:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:630:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:630:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:631:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:630:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_board.py:634:11: W0212: Access to a protected member _es_captura of a client class (protected-access)
tests/test_board.py:640:4: E0401: Unable to import 'backgammon.core.player' (import-error)
tests/test_board.py:640:4: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
tests/test_board.py:643:8: W0212: Access to a protected member _calcular_hash_secuencia of a client class (protected-access)
tests/test_board.py:671:24: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
tests/test_board.py:668:4: W0612: Unused variable 'dados' (unused-variable)
tests/test_board.py:701:24: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
tests/test_board.py:732:12: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
tests/test_board.py:761:12: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
************* Module test_checker
tests/test_checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_checker.py:1:0: E0401: Unable to import 'backgammon.core.checker' (import-error)
tests/test_checker.py:62:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_checker.py:62:4: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module test_dice
tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_dice.py:1:0: E0401: Unable to import 'backgammon.core.board' (import-error)
tests/test_dice.py:2:0: E0401: Unable to import 'backgammon.core.dice' (import-error)
tests/test_dice.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module test_move
tests/test_move.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_move.py:1:0: E0401: Unable to import 'backgammon.core.move' (import-error)
tests/test_move.py:50:4: W0621: Redefining name 'Move' from outer scope (line 1) (redefined-outer-name)
tests/test_move.py:50:4: E0401: Unable to import 'backgammon.core.move' (import-error)
tests/test_move.py:50:4: W0404: Reimport 'Move' (imported line 1) (reimported)
tests/test_move.py:50:4: C0415: Import outside toplevel (backgammon.core.move.Move) (import-outside-toplevel)
tests/test_move.py:53:11: C2801: Unnecessarily calls dunder method __eq__. Use == operator. (unnecessary-dunder-call)
************* Module test_player
tests/test_player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_player.py:2:0: E0401: Unable to import 'backgammon.core.player' (import-error)
tests/test_player.py:8:0: E0401: Unable to import 'backgammon.core.checker' (import-error)
tests/test_player.py:15:8: C0104: Disallowed name "bar" (disallowed-name)
tests/test_player.py:21:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:21:37: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:24:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:24:35: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:27:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:27:36: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:30:32: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:33:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:33:40: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:33:49: W0613: Unused argument 'dados' (unused-argument)
tests/test_player.py:36:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:36:33: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:36:42: W0613: Unused argument 'secuencia' (unused-argument)
tests/test_player.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:147:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_player.py:200:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_player.py:201:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:201:44: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:201:53: W0613: Unused argument 'dados' (unused-argument)
tests/test_player.py:200:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_player.py:221:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_player.py:222:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:222:37: W0613: Unused argument 'jugador' (unused-argument)
tests/test_player.py:222:46: W0613: Unused argument 'secuencia' (unused-argument)
tests/test_player.py:221:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_player.py:1:0: W0611: Unused import pytest (unused-import)
************* Module test_ui
tests/test_ui.py:31:0: C0301: Line too long (105/100) (line-too-long)
tests/test_ui.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_ui.py:3:0: E0401: Unable to import 'backgammon.pygame_ui.ui' (import-error)
tests/test_ui.py:4:0: E0401: Unable to import 'backgammon.core.backgammon' (import-error)
tests/test_ui.py:13:36: W0621: Redefining name 'mock_pygame' from outer scope (line 7) (redefined-outer-name)
tests/test_ui.py:39:69: W0212: Access to a protected member _get_current_dice of a client class (protected-access)
tests/test_ui.py:45:4: W0212: Access to a protected member _handle_click of a client class (protected-access)
tests/test_ui.py:54:4: W0212: Access to a protected member _handle_click of a client class (protected-access)
tests/test_ui.py:67:36: W0621: Redefining name 'mock_pygame' from outer scope (line 7) (redefined-outer-name)
tests/test_ui.py:86:69: W0212: Access to a protected member _get_current_dice of a client class (protected-access)
tests/test_ui.py:91:4: W0212: Access to a protected member _handle_click of a client class (protected-access)
tests/test_ui.py:105:4: W0212: Access to a protected member _handle_click of a client class (protected-access)
tests/test_ui.py:117:42: W0621: Redefining name 'mock_pygame' from outer scope (line 7) (redefined-outer-name)
tests/test_ui.py:135:4: W0212: Access to a protected member _end_turn of a client class (protected-access)
tests/test_ui.py:2:0: C0411: standard import "unittest.mock.Mock" should be placed before third party import "pytest" (wrong-import-order)
tests/test_ui.py:4:0: W0611: Unused BackgammonGame imported from backgammon.core.backgammon (unused-import)
tests/test_ui.py:1:0: R0801: Similar lines in 2 files
==core.move:[4:500]
==core.player:[4:500]
if TYPE_CHECKING:
    from backgammon.core.checker import Checker

ValorDado = int  # 1..6


@dataclass(frozen=True)
class PasoMovimiento:
    """
    Qué recibe:
      - desde: índice 0..23 o None si entra desde barra.
      - hasta: índice 0..23 o None si es bear-off (fuera).
      - dado: valor del dado usado (1..6).
      - captura: True si captura una ficha rival.

    Qué hace: representa un paso individual de movimiento.
    Qué devuelve: contenedor inmutable.
    """

    desde: Optional[int]
    hasta: Optional[int]
    dado: ValorDado
    captura: bool = False


SecuenciaMovimiento = List[PasoMovimiento]


@dataclass(frozen=True)
class OpcionMovimiento:
    """
    Qué recibe:
      - secuencia: pasos válidos (1..4).
      - hash_tablero: firma/hash del estado simulado.
      - puntaje: heurística para ranking (mayor = mejor).

    Qué hace: encapsula una jugada completa válida.
    Qué devuelve: contenedor inmutable.
    """

    secuencia: SecuenciaMovimiento
    hash_tablero: str
    puntaje: float = 0.0


class TableroFachada(Protocol):
    """
    Contrato mínimo que Player necesita de Board.
    La implementación concreta vive en core/board.py.
    """

    def jugador_tiene_en_barra(self, jugador: "Player") -> bool: ...
    def jugador_todo_en_home(self, jugador: "Player") -> bool: ...
    def oponente_en_cuadrante(self, jugador: "Player") -> bool: ...
    def jugador_pip_count(self, jugador: "Player") -> int: ...
    def enumerar_opciones_legales(
        self, jugador: "Player", dados: Sequence[ValorDado]
    ) -> List[OpcionMovimiento]: ...

    def aplicar_movimiento(
        self, jugador: "Player", secuencia: SecuenciaMovimiento
    ) -> None: ...


class Politica(Protocol):
    """
    Estrategia de selección de jugada.
    Útil para Humano/CPU; Player no depende de UI.
    """

    def elegir(
        self, opciones: List[OpcionMovimiento]
    ) -> Optional[SecuenciaMovimiento]: ...


class PoliticaNula:
    """
    Política por defecto: no decide.
    Qué recibe: lista de opciones legales.
    Qué hace: no elige nada (delega a UI/Game).
    Qué devuelve: None.
    """

    def elegir(self, opciones: List[OpcionMovimiento]) -> Optional[SecuenciaMovimiento]:
        return None


class Player:
    """
    A class used to represent a Backgammon player.

    ...

    Attributes
    ----------
    __id__ : str
        Logical identifier for the player (e.g., "P1")
    __nombre__ : str
        Display name of the player
    __color__ : str
        Color of the player's checkers ("blancas" or "negras")
    __direccion__ : int
        Direction of movement (+1 or -1)
    __home_points__ : frozenset[int]
        Set of board indices (0..23) that form the player's home
    __entry_point__ : int
        Entry point index for re-entering from the bar
    __checkers__ : list[Checker]
        List of Checker objects owned by the player
    __politica__ : Politica
        Strategy for move selection

    Methods
    -------
    get_id()
        Returns the logical identifier of the player
    get_nombre()
        Returns the display name of the player
    get_color()
        Returns the color of the player's checkers
    get_direccion()
        Returns the direction of movement (+1 or -1)
    get_home_points()
        Returns the set of home point indices
    get_entry_point()
        Returns the entry point index
    get_checkers()
        Returns a defensive copy of the player's checkers
    tiene_en_barra(tablero)
        Returns True if the player has checkers on the bar
    todas_en_home(tablero)
        Returns True if all checkers are in the home area
    pip_count(tablero)
        Returns the pip count for the player
    movimientos_legales(tablero, dados)
        Returns a list of legal move options for the player
    elegir_movimiento(opciones)
        Selects a move sequence from available options using the player's strategy
    confirmar_movimiento(tablero, secuencia)
        Applies a move sequence to the board
    puede_bear_off(tablero)
        Returns True if the player can bear off checkers
    colocar_checker_en_posicion(checker, posicion)
        Places a checker at a given board position
    mover_checker_a(checker, posicion)
        Moves a checker to another board position
    enviar_checker_a_barra(checker)
        Sends a checker to the bar
    sacar_checker(checker)
        Marks a checker as borne off
    checkers_en_tablero()
        Returns a list of checkers currently on the board
    checkers_en_barra()
        Returns a list of checkers currently on the bar
    checkers_fuera()
        Returns a list of checkers that have been borne off
    __str__()
        Returns a friendly string representation of the player
    __repr__()
        Returns a technical string representation for debugging
    """

    __slots__ = (
        "__id__",
        "__nombre__",
        "__color__",
        "__direccion__",
        "__home_points__",
        "__entry_point__",
        "__checkers__",
        "__politica__",
    )

    def __init__(
        self,
        player_id: str,
        nombre: str,
        color: str,
        direccion: int,
        home_points: Iterable[int],
        entry_point: int,
        checkers: Iterable["Checker"],
        politica: Optional[Politica] = None,
    ) -> None:
        """
        Parameters
        ----------
        player_id : str
            Logical identifier for the player (e.g., "P1")
        nombre : str
            Display name of the player
        color : str
            Color of the player's checkers ("blancas" or "negras")
        direccion : int
            Direction of movement (+1 or -1)
        home_points : Iterable[int]
            Indices (0..23) forming the player's home area
        entry_point : int
            Entry point index for re-entering from the bar
        checkers : Iterable[Checker]
            Iterable of Checker objects owned by the player
        politica : Optional[Politica], optional
            Strategy for move selection (default is PoliticaNula)
        """
        self.__id__ = player_id
        self.__nombre__ = nombre
        self.__color__ = color
        self.__direccion__ = 1 if direccion >= 0 else -1
        self.__home_points__ = frozenset(int(p) for p in home_points)
        self.__entry_point__ = int(entry_point)
        self.__checkers__ = list(checkers)
        self.__politica__ = politica if politica is not None else PoliticaNula()

    def get_id(self) -> str:
        """
        Returns the logical identifier of the player.

        Returns
        -------
        str
            The player's logical identifier
        """
        return self.__id__

    def get_nombre(self) -> str:
        """
        Returns the display name of the player.

        Returns
        -------
        str
            The player's display name
        """
        return self.__nombre__

    def get_color(self) -> str:
        """
        Returns the color of the player's checkers.

        Returns
        -------
        str
            The color ("blancas" or "negras")
        """
        return self.__color__

    def get_direccion(self) -> int:
        """
        Returns the direction of movement (+1 or -1).

        Returns
        -------
        int
            The direction of movement
        """
        return self.__direccion__

    def get_home_points(self) -> frozenset[int]:
        """
        Returns the set of home point indices.

        Returns
        -------
        frozenset[int]
            Indices forming the player's home area
        """
        return self.__home_points__

    def get_entry_point(self) -> int:
        """
        Returns the entry point index.

        Returns
        -------
        int
            The entry point index for re-entering from the bar
        """
        return self.__entry_point__

    def get_checkers(self) -> List["Checker"]:
        """
        Returns a defensive copy of the player's checkers.

        Returns
        -------
        list[Checker]
            List of Checker objects
        """
        return list(self.__checkers__)  # copia defensiva

    def tiene_en_barra(self, tablero: TableroFachada) -> bool:
        """
        Returns True if the player has checkers on the bar.

        Parameters
        ----------
        tablero : TableroFachada
            Board facade implementing required methods

        Returns
        -------
        bool
            True if any checker is on the bar
        """
        return tablero.jugador_tiene_en_barra(self)

    def todas_en_home(self, tablero: TableroFachada) -> bool:
        """
        Returns True if all checkers are in the home area.

        Parameters
        ----------
        tablero : TableroFachada

        Returns
        -------
        bool
        """
        return tablero.jugador_todo_en_home(self)

    def pip_count(self, tablero: TableroFachada) -> int:
        """
        Returns the pip count for the player.

        Parameters
        ----------
        tablero : TableroFachada

        Returns
        -------
        int
        """
        return tablero.jugador_pip_count(self)

    def movimientos_legales(
        self, tablero: TableroFachada, dados: Sequence[ValorDado]
    ) -> List[OpcionMovimiento]:
        """
        Returns a list of legal move options for the player.

        Parameters
        ----------
        tablero : TableroFachada
        dados : Sequence[ValorDado]

        Returns
        -------
        list[OpcionMovimiento]
        """
        return tablero.enumerar_opciones_legales(self, dados)

    def elegir_movimiento(
        self, opciones: List[OpcionMovimiento]
    ) -> Optional[SecuenciaMovimiento]:
        """
        Selects a move sequence from available options using the player's strategy.

        Parameters
        ----------
        opciones : list[OpcionMovimiento]

        Returns
        -------
        Optional[SecuenciaMovimiento]
        """
        if not opciones:
            return None
        return self.__politica__.elegir(opciones)

    def confirmar_movimiento(
        self, tablero: TableroFachada, secuencia: SecuenciaMovimiento
    ) -> None:
        """
        Applies a move sequence to the board.

        Parameters
        ----------
        tablero : TableroFachada
        secuencia : SecuenciaMovimiento
        """
        tablero.aplicar_movimiento(self, secuencia)

    def puede_bear_off(self, tablero: TableroFachada) -> bool:
        """
        Returns True if the player can bear off checkers.

        Parameters
        ----------
        tablero : TableroFachada

        Returns
        -------
        bool
        """
        return (
            self.todas_en_home(tablero)
            and not self.tiene_en_barra(tablero)
            and not tablero.oponente_en_cuadrante(self)
        )

    def colocar_checker_en_posicion(self, checker: "Checker", posicion: int) -> None:
        """
        Places a checker at a given board position.

        Parameters
        ----------
        checker : Checker
        posicion : int
        """
        checker.colocar_en_posicion(posicion)

    def mover_checker_a(self, checker: "Checker", posicion: int) -> None:
        """
        Moves a checker to another board position.

        Parameters
        ----------
        checker : Checker
        posicion : int
        """
        checker.mover_a(posicion)

    def enviar_checker_a_barra(self, checker: "Checker") -> None:
        """
        Sends a checker to the bar.

        Parameters
        ----------
        checker : Checker
        """
        checker.enviar_a_barra()

    def sacar_checker(self, checker: "Checker") -> None:
        """
        Marks a checker as borne off.

        Parameters
        ----------
        checker : Checker
        """
        checker.sacar()

    def checkers_en_tablero(self) -> List["Checker"]:
        """
        Returns a list of checkers currently on the board.

        Returns
        -------
        list[Checker]
        """
        return [c for c in self.__checkers__ if c.en_tablero()]

    def checkers_en_barra(self) -> List["Checker"]:
        """
        Returns a list of checkers currently on the bar.

        Returns
        -------
        list[Checker]
        """
        return [c for c in self.__checkers__ if c.en_barra()]

    def checkers_fuera(self) -> List["Checker"]:
        """
        Returns a list of checkers that have been borne off.

        Returns
        -------
        list[Checker]
        """
        return [c for c in self.__checkers__ if c.fuera()]

    def __str__(self) -> str:
        """
        Returns a friendly string representation of the player.

        Returns
        -------
        str
        """
        return f"Player({self.__nombre__}, {self.__color__}, dir={self.__direccion__})"

    def __repr__(self) -> str:
        """
        Returns a technical string representation for debugging.

        Returns
        -------
        str
        """
        return (
            "Player("
            f"id={self.__id__!r}, nombre={self.__nombre__!r}, color={self.__color__!r}, "
            f"direccion={self.__direccion__!r}, home_points={sorted(self.__home_points__)!r}, "
            f"entry_point={self.__entry_point__!r}, checkers={len(self.__checkers__)!r})"
        ) (duplicate-code)
tests/test_ui.py:1:0: R0801: Similar lines in 2 files
==cli.console:[47:54]
==test_backgammon:[9:16]
            "color": "blancas",
            "direccion": 1,
            "home_points": [18, 19, 20, 21, 22, 23],
            "entry_point": 0,
        },
        {
            "id": "P2", (duplicate-code)

-----------------------------------
Your code has been rated at 7.65/10


```
