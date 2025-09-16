class Board:
    """Tablero para Backgammon con 24 puntas enumeradas del 1 al 24.
    La lógica de las fichas estará separada en otro archivo

    atributes
    ----------
    triangulo : list[list]
        Lista de 24 listas (una por punta). Cada lista contendrá las fichas
        ubicadas en esa punta. Inicialmente todas están vacías.

    methods
    --------
    display()
        Imprime cada punta del tablero con su contenido.

    """

    def __init__(self) -> None:
        """Inicializa un tablero vacío con 24 puntas.

        Notes
        -------
        Aquí no se implementa la lógica de las fichas ni sus movimientos;
        la clase solo modela el contenedor (las 24 puntas).

        """
        # Inicializa las 24 puntas del tablero como listas vacías
        self.triangulo = [[] for x in range(1, 25)]
        # No se maneja la lógica de fichas aquí

    def display(self) -> None:
        """Muestra en la pantalla los triangulos del tablero con sus elementos.
        Returns
        -------
        None

        Examples
        --------
        board = Board()
         board.display()

        """
        for i, point in enumerate(self.triangulo):
            print(f"Punta {i+1}: {point}")


# Test code removed - should be in test files instead
# if __name__ == "__main__":
#     prueba = Board()
#     prueba.display()
