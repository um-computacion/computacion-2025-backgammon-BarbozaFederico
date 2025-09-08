# Prompt: Explica paso a paso de forma sencilla como crear el tablero para el juego backgammon en (CLI)

## Modelo / herramienta usada: GitHub Copilot

### Instrucciones del sistema: Siempre sigue los principios SOLID, incluye docstrings y comentarios claros, documenta el prompt y la respuesta en prompts/prompts-desarrollo.md

### Respuesta

¡Mirá, te lo explico como Ricardo Fort, papá! Para crear el tablero de Backgammon en una interfaz de línea de comandos (CLI), seguí estos pasos sencillos:

1. **Definí la clase Board**
   - Creá una clase llamada `Board` que represente el tablero. Usá una lista de 24 elementos para las puntas.

2. **Inicializá las puntas**
   - Cada punta puede ser una lista que contenga las fichas de cada jugador. Inicializá las posiciones según las reglas del Backgammon.

3. **Agregá un método para mostrar el tablero**
   - Implementá un método `display()` que imprima el estado actual del tablero en la terminal, usando texto y símbolos para representar las fichas.

4. **Separá responsabilidades**
   - La clase `Board` solo debe encargarse del tablero. Los movimientos y la lógica de los jugadores van en otras clases.

#### Ejemplo básico en Python

```python
class Board:
    """Tablero de Backgammon para CLI, con 24 puntas."""
    def __init__(self):
        # Cada punta es una lista con las fichas que tiene
        self.points = [[] for _ in range(24)]
        # Inicializá las fichas según las reglas
        # Por ejemplo: self.points[0] = ['X', 'X']
        # ...y así con el resto...

    def display(self):
        """Muestra el tablero en la terminal."""
        for i, point in enumerate(self.points):
            print(f"Punta {i+1}: {point}")
```

---

# Prompt: Explicame como hacer una clase desde 0, que elementos tiene? y que son los principios solid?

## Modelo / herramienta usada: GitHub Copilot

### Instrucciones del sistema: Siempre sigue los principios SOLID, incluye docstrings y comentarios claros, documenta el prompt y la respuesta en prompts/prompts-desarrollo.md

### Respuesta

¡Mirá, te lo explico como Ricardo Fort, papá!

Para crear una clase desde cero en Python, seguí estos pasos:

1. **Definí el nombre de la clase**
   - Usá la palabra clave `class` y elegí un nombre representativo.

2. **Agregá el método constructor `__init__`**
   - Este método se ejecuta al crear una instancia de la clase y sirve para inicializar atributos.

3. **Definí atributos**
   - Son variables que guardan el estado de la clase.

4. **Agregá métodos**
   - Son funciones que definen el comportamiento de la clase.

5. **Incluí docstrings y comentarios claros**
   - Documentá la clase y sus métodos para que todo el mundo entienda el código.

#### Ejemplo básico

```python
class Ejemplo:
    """Clase de ejemplo que muestra cómo crear una clase desde cero."""
    def __init__(self, valor):
        """Inicializa la clase con un valor."""
        self.valor = valor

    def mostrar(self):
        """Muestra el valor almacenado."""
        print(f"El valor es: {self.valor}")
```

---

### ¿Qué son los principios SOLID?

Los principios SOLID son cinco reglas para escribir código orientado a objetos que sea fácil de mantener y escalar:

1. **S**ingle Responsibility Principle (Responsabilidad Única):
   - Cada clase debe tener una sola responsabilidad.
2. **O**pen/Closed Principle (Abierta/Cerrada):
   - El código debe estar abierto a extensión, pero cerrado a modificación.
3. **L**iskov Substitution Principle (Sustitución de Liskov):
   - Las subclases deben poder usarse en lugar de la clase base sin problemas.
4. **I**nterface Segregation Principle (Segregación de Interfaces):
   - Las clases no deben depender de interfaces que no usan.
5. **D**ependency Inversion Principle (Inversión de Dependencias):
   - Depender de abstracciones, no de implementaciones concretas.

---

**Indicación de uso:**

- Usá estos pasos y principios para crear clases limpias y mantenibles en tu proyecto.
- Documentá siempre el prompt y la respuesta en prompts/prompts-desarrollo.md.

**Referencia:**

- Documentación: prompts/prompts-desarrollo.md
