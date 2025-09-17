# Changelog

Todas las modificaciones notables de este proyecto serán documentadas en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto sigue [Semantic Versioning](https://semver.org/lang/es/).

## [1.2.0] 17/09/2025

### Added

- Se creo la clase [board.py](./backgammon/core/board.py)
- Tests completos con pytest para las clases [Player](./tests/test_player.py), [Checker](./tests/test_checker.py), [Dice](./tests/test_dice.py) y [Board](./tests/test_board.py), cubriendo el 100% de los métodos públicos y privados relevantes.
- Tests para asegurar copia defensiva en `Player.get_checkers()` y que los métodos de gestión no alteran el estado de otras fichas.
- Tests para los métodos `get_owner`, `__str__` y `__repr__` en `Checker`.
- Tests para inicialización, lanzamiento y consulta de valores en `Dice`.
- Tests para inicialización, gestión de jugadores y fichas, barra, borne off, display y reset en `Board`.
- Documentación de todos los prompts y respuestas generadas en los archivos correspondientes de la carpeta `prompts`.

### Fixed

- Se resolvió el problema de importación circular entre `checker.py` y `player.py` usando `TYPE_CHECKING` para anotaciones de tipo.
- Se corrigieron inconsistencias de nombres de atributos y métodos para asegurar compatibilidad entre módulos.
- Se mejoró la cobertura y claridad de la documentación y los tests para las clases principales del núcleo del juego.

### Changed

- Se actualizaron los docstrings de todas las clases principales para cumplir con el formato requerido.
- Se mejoró la estructura de los tests para asegurar cobertura total y separación de responsabilidades.
- Se actualizaron los prompts de documentación y testing para reflejar todos los cambios realizados.

---

**Referencias:**  

- `backgammon/core/player.py`  
- `backgammon/core/checker.py`  
- `backgammon/core/dice.py`  
- `backgammon/core/board.py`  
- `tests/test_player.py`  
- `tests/test_checker.py`  
- `tests/test_dice.py`  
- `tests/test_board.py`  
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
