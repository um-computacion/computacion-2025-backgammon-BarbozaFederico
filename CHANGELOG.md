# Changelog

Todas las modificaciones notables de este proyecto serán documentadas en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto sigue [Semantic Versioning](https://semver.org/lang/es/).

## [0.7.0] 17/09/2025

### Added

- Se creó la clase [backgammon.py](./backgammon/core/backgammon.py) que integra y coordina las clases principales del juego (Player, Checker, Dice, Board).
- Se creó la clase [board.py](./backgammon/core/board.py).
- Documentación tipo NumPy para las clases `Player`, `Checker`, `Dice`, `Board` y `BackgammonGame`, siguiendo el formato de copilot-instructions.md.
- Tests completos con pytest para las clases [Player](./tests/test_player.py), [Checker](./tests/test_checker.py), [Dice](./tests/test_dice.py), [Board](./tests/test_board.py) y [BackgammonGame](./tests/test_backgammon.py), cubriendo el 100% de los métodos públicos y privados relevantes.

---

**Referencias:**  

- `backgammon/core/backgammon.py`
- `backgammon/core/player.py`  
- `backgammon/core/checker.py`  
- `backgammon/core/dice.py`  
- `backgammon/core/board.py`  
- `tests/test_player.py`  
- `tests/test_checker.py`  
- `tests/test_dice.py`  
- `tests/test_board.py`  
- `tests/test_backgammon.py`
- `prompts/prompts-desarrollo.md`  
- `prompts/prompts-documentacion.md`  
- `prompts/prompts-testing.md`

## [0.6.0] 17/09/2025

### Added

- Creacion de [test_player.py](./tests/test_player.py) para la clase [player](./backgammon/core/player.py)
- Creacion del archivo [coverage_report.txt](./coverage_report.txt) para dejar registro del porcentaje de codigo cubierto

### Fixed

- Se resolvió el problema de importación circular entre `checker.py` y `player.py` usando `TYPE_CHECKING` para anotaciones de tipo.

### Changed

- Se mejoró la cobertura y claridad de la documentación y los tests para las clases principales del núcleo del juego.

---

**Referencias:**  

- `backgammon/core/player.py`  
- `backgammon/core/checker.py`  
- `tests/test_player.py`

## [0.5.0] 16/09/2025

### Added

- Creacion de clase [player](./backgammon/core/player.py)
- Actualizacion del [copilot-intructions](./.github/copilot-instructions.md)

## [0.4.0] 16/09/2025

### added

- Creacion de la logica de la clase [checker.py](./backgammon/core/checker.py)

- se añadio [REPORTS.md](./REPORTS.md)

- Se creo estructura completa de [core](./backgammon/core/) y [tests](./tests/)
- creacion de la carpeta [workflows](./.github/workflows/)

- creacion del archivo [ci.yml](./.github/workflows/ci.yml)

### Fixed

- Se realizo el debug y reescritura de [ci.yml](./.github/workflows/ci.yml)

- se corrigio errores de tests creando [conftest.py](./tests/conftest.py) y [pytest.ini](./pytest.ini)

## [0.3.0] 10-08-2025

### Added+

- logica basica de la clase [dice](./backgammon/core/dice.py)
- Documentacion de funciones de la clase [dice](./backgammon/core/dice.py)

## [0.2.0] 08-09/2025

### Added

- Creacion de logica basica de tablero
- Actualizacion de prompts a traves de [copilot-instructions](./.github/copilot-instructions.md)

## [0.1.0] 07-08-2025

### Added

- Creacion del esqueleto del proyecto
- Creacion de archivo [requeriments.txt](./requirements.txt)
