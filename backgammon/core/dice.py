import random


class Dice:
    """
    Clase que representa dos dados para Backgammon.

    Atributes
    ----------
    dice1 : int
        Representa al dado uno y las posibilidades de la salida de cada numero
    dice2 : int
        Representa al dado dos y las posibilidades de la salida de cada numero
    metods
    --------
     lanzamiento()
        Lanza ambos dados y actualiza sus valores.
    get_values()
        Devuelve los valores actuales de los dos dados.
    """

    def __init__(self) -> None:
        # Cada dado comienza en 1
        self.dice1 = 1
        self.dice2 = 1

    def lanzamiento(self) -> tuple[int, int]:
        """Lanza ambos dados y actualiza sus valores con números aleatorios entre 1 y 6.

        returns 
        --------
        tuple [int, int]
            Una tupla con los valores de los dos dados después del lanzamiento.
        """

        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        return (self.dice1, self.dice2)

    def get_values(self) -> tuple[int, int]:
        """Devuelve los valores actuales de los dados.

        returns
        --------
        tuple [int, int]
        Una tupla con los valores actuales de los dos dados.

        """
        return (self.dice1, self.dice2)
