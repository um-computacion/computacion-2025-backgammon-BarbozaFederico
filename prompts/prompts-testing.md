# Prompt: Genera tests para cheker.py en el archivo test_cheker.py y deja este promt planteado en promts-testing

## Modelo / herramienta usada: GitHub Copilot

### Instrucciones del sistema: Siempre sigue los principios SOLID, incluye docstrings y comentarios claros, documenta el prompt y la respuesta en prompts/prompts-testing.md

### Respuesta

Se generaron cinco tests unitarios en `tests/test_checker.py` para la clase `Checker`:

1. `test_checker_initial_state`: Verifica el estado inicial de una ficha recién creada.
2. `test_colocar_en_posicion`: Testea colocar la ficha en una posición válida.
3. `test_enviar_a_barra`: Testea enviar la ficha a la barra.
4. `test_sacar`: Testea sacar la ficha del tablero (bear off).
5. `test_resetear`: Testea el reseteo de estado de la ficha.

Todos los tests usan pytest, incluyen docstrings y cubren la funcionalidad esencial de la clase.

**Salida usada sin cambios.**
**Referencia:** `tests/test_checker.py`

---

# Prompt: genera tests completos cubriendo todo con pytest para el archivo "player.py" y deja este promt planteado en "promt-testing.md"

## Modelo / herramienta usada: GitHub Copilot

### Instrucciones del sistema: Siempre sigue los principios SOLID, incluye docstrings y comentarios claros, documenta el prompt y la respuesta en prompts/prompts-testing.md

### Respuesta

Se generaron tests completos en `tests/test_player.py` para la clase `Player`, cubriendo inicialización, getters, gestión de fichas, filtros de estado, delegación al tablero, obtención y selección de movimientos, confirmación de movimientos, consulta de bear off y representaciones de texto.  
Todos los tests usan pytest, incluyen docstrings y cubren la funcionalidad esencial y avanzada de la clase.

**Salida usada sin cambios.**  
**Referencia:** `tests/test_player.py`
