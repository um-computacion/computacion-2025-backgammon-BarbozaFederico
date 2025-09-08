class Board:
    """Tablero para Backgammon con 24 puntas enumeradas del 1 al 24.
    La lógica de las fichas estará separada en otro archivo"""

    def __init__(self):
        # Inicializa las 24 puntas del tablero como listas vacías
        self.__triangulo__ = [[] for x in range(1, 25)]
        # No se maneja la lógica de fichas aquí

    def display(self) -> None:
        """Muestra en la pantalla los triangulos del tablero con sus elementos."""
        for i, point in enumerate(self.triangulo):
            print(f"Punta {i+1}: {point}")


prueba = Board()
prueba.display()
