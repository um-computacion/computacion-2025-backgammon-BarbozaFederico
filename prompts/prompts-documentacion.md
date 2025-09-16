# Prompt: Cambia la documentación docstring de la clase checker planteandolo en prompt de documentación, debe seguir el formato de docstring tipo "A class used to represent an Animal..." con sección de Attributes y Methods

## Modelo / herramienta usada: GitHub Copilot

### Instrucciones del sistema: Siempre sigue los principios SOLID, incluye docstrings y comentarios claros, documenta el prompt y la respuesta en prompts/prompts-documentacion.md

### Prompt exacto

Cambia la documentacion docstring de la clase checker planteandolo en promt de documentacion, deber seguir
""""
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs=4):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """
        "

### Respuesta

Se reemplazó el docstring de la clase `Checker` por uno estructurado tipo NumPy, siguiendo el ejemplo dado.  
Incluye sección de Attributes y Methods, describiendo cada atributo y método relevante de la clase.  
La salida fue usada sin cambios en `backgammon/core/checker.py`.

**Referencia:** `backgammon/core/checker.py`
