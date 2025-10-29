# Automated Reports
## Coverage Report
```text
........................................................................ [ 84%]
..........F
=================================== FAILURES ===================================
______________________________ test_move_from_bar ______________________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f4b5b5901c0>
mock_pygame = <Mock id='139961631838352'>

    def test_move_from_bar(monkeypatch, mock_pygame):
        """Test moving a checker from the bar to the board."""
        # Mock pygame to avoid display initialization
        monkeypatch.setattr("backgammon.pygame_ui.ui.pygame", mock_pygame)
    
        # Initialize UI
        ui = PygameUI()
        game = ui.game
>       player = game.get_current_player()

tests/test_ui.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <backgammon.core.backgammon.BackgammonGame object at 0x7f4b5b153280>

    def get_current_player(self) -> Player:
        """
        Returns the current Player object.
    
        Returns
        -------
        Player
        """
>       return self.players[self.current_player_idx]
E       IndexError: list index out of range

backgammon/core/backgammon.py:158: IndexError
=========================== short test summary info ============================
FAILED tests/test_ui.py::test_move_from_bar - IndexError: list index out of range
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
1 failed, 82 passed in 1.37s

```
## Pylint Report
```text
************* Module cli.console
backgammon/cli/console.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/cli/console.py:115:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
backgammon/cli/console.py:98:26: W0613: Unused argument 'player' (unused-argument)
backgammon/cli/console.py:2:0: W0611: Unused OpcionMovimiento imported from backgammon.core.player (unused-import)
backgammon/cli/console.py:2:0: W0611: Unused SecuenciaMovimiento imported from backgammon.core.player (unused-import)
************* Module core.backgammon
backgammon/core/backgammon.py:180:0: C0301: Line too long (107/100) (line-too-long)
backgammon/core/backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/backgammon.py:93:16: W0212: Access to a protected member _player of a client class (protected-access)
************* Module core.board
backgammon/core/board.py:488:0: C0325: Unnecessary parens after '=' keyword (superfluous-parens)
backgammon/core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/board.py:15:0: C0413: Import "from backgammon.core.player import OpcionMovimiento" should be placed at the top of the module (wrong-import-position)
backgammon/core/board.py:70:8: C0104: Disallowed name "bar" (disallowed-name)
backgammon/core/board.py:217:8: C0206: Consider iterating with .items() (consider-using-dict-items)
backgammon/core/board.py:220:8: C0206: Consider iterating with .items() (consider-using-dict-items)
backgammon/core/board.py:277:16: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
backgammon/core/board.py:311:12: R1724: Unnecessary "elif" after "continue", remove the leading "el" from "elif" (no-else-continue)
backgammon/core/board.py:396:4: R0914: Too many local variables (24/15) (too-many-locals)
backgammon/core/board.py:403:8: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
backgammon/core/board.py:474:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
backgammon/core/board.py:396:4: R0912: Too many branches (25/12) (too-many-branches)
backgammon/core/board.py:396:4: R0915: Too many statements (55/50) (too-many-statements)
backgammon/core/board.py:541:4: R0911: Too many return statements (7/6) (too-many-return-statements)
backgammon/core/board.py:686:8: W0404: Reimport 'OpcionMovimiento' (imported line 15) (reimported)
backgammon/core/board.py:686:8: C0415: Import outside toplevel (backgammon.core.player.OpcionMovimiento, backgammon.core.player.ValorDado) (import-outside-toplevel)
backgammon/core/board.py:774:8: W0404: Reimport 'OpcionMovimiento' (imported line 15) (reimported)
backgammon/core/board.py:774:8: C0415: Import outside toplevel (backgammon.core.player.OpcionMovimiento) (import-outside-toplevel)
************* Module core.dice
backgammon/core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module core.move
backgammon/core/move.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/move.py:4:0: C0115: Missing class docstring (missing-class-docstring)
backgammon/core/move.py:5:4: R0913: Too many arguments (6/5) (too-many-arguments)
backgammon/core/move.py:5:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
backgammon/core/move.py:1:0: W0611: Unused Optional imported from typing (unused-import)
************* Module core.player
backgammon/core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/player.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:57:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:58:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:60:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:64:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:73:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:67:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/player.py:84:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:84:21: W0613: Unused argument 'opciones' (unused-argument)
backgammon/core/player.py:76:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/player.py:88:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
backgammon/core/player.py:174:4: R0913: Too many arguments (9/5) (too-many-arguments)
backgammon/core/player.py:174:4: R0917: Too many positional arguments (9/5) (too-many-positional-arguments)
backgammon/core/player.py:88:0: R0904: Too many public methods (21/20) (too-many-public-methods)
************* Module pygame_ui.ui
backgammon/pygame_ui/ui.py:700:0: C0301: Line too long (109/100) (line-too-long)
backgammon/pygame_ui/ui.py:799:0: C0301: Line too long (117/100) (line-too-long)
backgammon/pygame_ui/ui.py:991:0: C0301: Line too long (106/100) (line-too-long)
backgammon/pygame_ui/ui.py:1076:0: C0301: Line too long (133/100) (line-too-long)
backgammon/pygame_ui/ui.py:1:0: C0302: Too many lines in module (1098/1000) (too-many-lines)
backgammon/pygame_ui/ui.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/pygame_ui/ui.py:50:0: R0902: Too many instance attributes (27/7) (too-many-instance-attributes)
backgammon/pygame_ui/ui.py:325:4: R0914: Too many local variables (32/15) (too-many-locals)
backgammon/pygame_ui/ui.py:325:4: R0912: Too many branches (15/12) (too-many-branches)
backgammon/pygame_ui/ui.py:325:4: R0915: Too many statements (62/50) (too-many-statements)
backgammon/pygame_ui/ui.py:523:12: W0612: Unused variable 'color' (unused-variable)
backgammon/pygame_ui/ui.py:649:29: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
backgammon/pygame_ui/ui.py:687:29: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
backgammon/pygame_ui/ui.py:772:15: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
backgammon/pygame_ui/ui.py:837:12: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
backgammon/pygame_ui/ui.py:898:4: R0913: Too many arguments (7/5) (too-many-arguments)
backgammon/pygame_ui/ui.py:898:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
backgammon/pygame_ui/ui.py:1041:4: R0912: Too many branches (14/12) (too-many-branches)
backgammon/pygame_ui/ui.py:50:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/pygame_ui/ui.py:2:0: C0411: standard import "sys" should be placed before third party import "pygame" (wrong-import-order)
backgammon/pygame_ui/ui.py:3:0: C0411: standard import "time" should be placed before third party import "pygame" (wrong-import-order)
backgammon/pygame_ui/ui.py:4:0: C0411: standard import "random" should be placed before third party import "pygame" (wrong-import-order)
backgammon/pygame_ui/ui.py:6:0: W0611: Unused PasoMovimiento imported from backgammon.core.player (unused-import)
backgammon/pygame_ui/ui.py:6:0: W0611: Unused SecuenciaMovimiento imported from backgammon.core.player (unused-import)
************* Module test_backgammon
tests/test_backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_backgammon.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_backgammon.py:30:11: C1803: "game.players == []" can be simplified to "not game.players", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_backgammon.py:1:0: W0611: Unused import pytest (unused-import)
************* Module test_board
tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_board.py:18:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:21:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:24:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:27:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:33:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:52:11: C1803: "board.players == []" can be simplified to "not board.players", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:103:11: C1803: "board.get_checkers_on_point(...) == []" can be simplified to "not board.get_checkers_on_point(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:104:11: C1803: "board.get_checkers_on_point(...) == []" can be simplified to "not board.get_checkers_on_point(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:118:11: C1803: "board.get_borne_off(...) == []" can be simplified to "not board.get_borne_off(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:152:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:153:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:154:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:155:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:156:11: C1803: "board.players == []" can be simplified to "not board.players", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:160:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:169:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:188:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:200:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:221:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:231:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:232:11: W0212: Access to a protected member _es_captura of a client class (protected-access)
tests/test_board.py:236:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:263:11: C1803: "board.get_checkers_on_point(...) == []" can be simplified to "not board.get_checkers_on_point(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:264:11: C1803: "board.get_checkers_on_point(...) == []" can be simplified to "not board.get_checkers_on_point(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:272:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:270:4: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
tests/test_board.py:272:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:273:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:272:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_board.py:278:8: W0212: Access to a protected member _aplicar_paso_movimiento of a client class (protected-access)
tests/test_board.py:286:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:284:4: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
tests/test_board.py:286:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:287:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:286:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_board.py:295:4: W0212: Access to a protected member _aplicar_paso_movimiento of a client class (protected-access)
tests/test_board.py:306:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:306:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:307:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:310:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:313:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:316:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:319:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:322:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:322:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:326:11: C1803: "result == []" can be simplified to "not result", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:334:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:332:4: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
tests/test_board.py:334:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:335:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:338:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:341:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:344:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:347:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:350:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:350:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:356:12: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
tests/test_board.py:357:11: C1803: "moves == []" can be simplified to "not moves", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:332:4: W0611: Unused PasoMovimiento imported from backgammon.core.player (unused-import)
tests/test_board.py:364:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:364:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:365:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:368:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:368:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:371:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:378:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:378:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:379:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:382:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:382:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:385:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:386:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:393:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:393:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:394:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:393:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_board.py:398:11: W0212: Access to a protected member _es_captura of a client class (protected-access)
tests/test_board.py:402:11: W0212: Access to a protected member _es_captura of a client class (protected-access)
tests/test_board.py:405:11: W0212: Access to a protected member _es_captura of a client class (protected-access)
tests/test_board.py:412:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:412:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:413:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:412:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_board.py:416:8: W0212: Access to a protected member _calcular_hash_secuencia of a client class (protected-access)
tests/test_board.py:459:11: C1803: "board.get_bar(...) == []" can be simplified to "not board.get_bar(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:465:11: C1803: "board.get_borne_off(...) == []" can be simplified to "not board.get_borne_off(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:483:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:484:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:485:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:486:11: C1803: "x == []" can be simplified to "not x", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:487:11: C1803: "board.players == []" can be simplified to "not board.players", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:495:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:495:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:495:4: R0903: Too few public methods (0/2) (too-few-public-methods)
tests/test_board.py:506:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:506:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:507:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:510:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:513:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:516:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:519:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:522:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:522:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:526:11: C1803: "opciones == []" can be simplified to "not opciones", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:533:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:533:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:534:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:537:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:540:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:543:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:546:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:549:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:549:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:553:11: C1803: "result == []" can be simplified to "not result", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:560:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:560:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:561:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:564:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:567:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:570:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:573:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:576:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:576:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:579:12: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
tests/test_board.py:580:11: C1803: "moves == []" can be simplified to "not moves", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board.py:587:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:587:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:588:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:591:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:591:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board.py:595:11: W0212: Access to a protected member _es_movimiento_valido of a client class (protected-access)
tests/test_board.py:602:4: W0621: Redefining name 'DummyPlayer' from outer scope (line 6) (redefined-outer-name)
tests/test_board.py:602:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:603:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:602:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_board.py:606:11: W0212: Access to a protected member _es_captura of a client class (protected-access)
tests/test_board.py:612:4: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
tests/test_board.py:615:8: W0212: Access to a protected member _calcular_hash_secuencia of a client class (protected-access)
tests/test_board.py:643:24: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
tests/test_board.py:640:4: W0612: Unused variable 'dados' (unused-variable)
tests/test_board.py:673:24: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
tests/test_board.py:704:12: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
tests/test_board.py:733:12: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
************* Module test_board_invalid_dados
tests/test_board_invalid_dados.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_board_invalid_dados.py:10:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_board_invalid_dados.py:11:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board_invalid_dados.py:14:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board_invalid_dados.py:17:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board_invalid_dados.py:20:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board_invalid_dados.py:23:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board_invalid_dados.py:26:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board_invalid_dados.py:26:33: W0613: Unused argument 'b' (unused-argument)
tests/test_board_invalid_dados.py:31:11: C1803: "opciones == []" can be simplified to "not opciones", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_board_invalid_dados.py:1:0: W0611: Unused import pytest (unused-import)
************* Module test_checker
tests/test_checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_checker.py:62:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_checker.py:62:4: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module test_dice
tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_dice.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module test_move
tests/test_move.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_move.py:50:4: W0621: Redefining name 'Move' from outer scope (line 1) (redefined-outer-name)
tests/test_move.py:50:4: W0404: Reimport 'Move' (imported line 1) (reimported)
tests/test_move.py:50:4: C0415: Import outside toplevel (backgammon.core.move.Move) (import-outside-toplevel)
tests/test_move.py:53:11: C2801: Unnecessarily calls dunder method __eq__. Use == operator. (unnecessary-dunder-call)
************* Module test_player
tests/test_player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_player.py:17:8: C0104: Disallowed name "bar" (disallowed-name)
tests/test_player.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:35:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:38:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:150:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_player.py:203:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_player.py:204:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:203:4: R0903: Too few public methods (1/2) (too-few-public-methods)
tests/test_player.py:209:11: C1803: "moves == []" can be simplified to "not moves", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
tests/test_player.py:224:4: C0115: Missing class docstring (missing-class-docstring)
tests/test_player.py:225:8: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:224:4: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module test_ui
tests/test_ui.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_ui.py:7:0: C0411: standard import "unittest.mock.Mock" should be placed before third party import "pytest" (wrong-import-order)
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
Your code has been rated at 8.62/10


```
