#  Siempre sigue los principios SOLID
#  Incluir docstrings y comentarios claros en el código generado
#  Proporciona una explicación detallada para cada prompt y documenta tanto el prompt como la respuesta generada dentro de los archivos prompts/prompts-desarrollo.md, prompts/prompts-documentacion.md o prompts/prompts-testing.md. Usa únicamente estos archivos para la documentación de prompts.
#  Por cada prompt debe quedar registrado:Modelo / herramienta usada (nombre y versión si corresponde),El texto exacto del prompt (sin reescrituras subjetivas),Instrucciones del sistema (si las hubo),Respuesta/resultado completo devuelto por la IA, Indicar si la salida fue usada sin cambios, usada con modificaciones (mostrar lasmodificaciones) o descartada,Referencia a los archivos finales que incorporaron contenido generado por IA (ej:core/board.py)
# Genera documentacion de clases y funciones de la siguiente manera: 
```python

class Animal:
    """
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

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))

```

