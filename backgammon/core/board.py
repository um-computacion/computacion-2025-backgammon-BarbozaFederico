from typing import List, Optional, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from backgammon.core.player import Player
    from backgammon.core.checker import Checker
    from backgammon.core.dice import Dice


class Board:
    """
    A class used to represent the Backgammon board.

    ...

    Attributes
    ----------
    points : List[List[Checker]]
        List of 24 points (triangles), each containing a list of Checker objects.
    bar : Dict[str, List[Checker]]
        Dictionary with color keys ("blancas", "negras") for checkers on the bar.
    borne_off : Dict[str, List[Checker]]
        Dictionary with color keys for checkers that have been borne off.
    players : List[Player]
        List of Player objects participating in the game.
    dice : Optional[Dice]
        Dice object used for rolling moves (optional, can be set externally).

    Methods
    -------
    add_player(player)
        Adds a player to the board.
    place_checker(checker, point)
        Places a checker on a specific point (0..23).
    move_checker(checker, from_point, to_point)
        Moves a checker from one point to another.
    send_to_bar(checker)
        Sends a checker to the bar.
    bear_off_checker(checker)
        Removes a checker from the board (bear off).
    get_checkers_on_point(point)
        Returns the list of checkers on a given point.
    get_bar(color)
        Returns the list of checkers on the bar for a given color.
    get_borne_off(color)
        Returns the list of checkers that have been borne off for a given color.
    display()
        Prints the current state of the board, bar, and borne off checkers.
    reset()
        Resets the board to its initial empty state.
    """

    def __init__(self) -> None:
        """
        Initializes an empty Backgammon board with 24 points, empty bar and borne off areas.

        Parameters
        ----------
        None
        """
        self.points: List[List["Checker"]] = [[] for _ in range(24)]
        self.bar: Dict[str, List["Checker"]] = {"blancas": [], "negras": []}
        self.borne_off: Dict[str, List["Checker"]] = {"blancas": [], "negras": []}
        self.players: List["Player"] = []
        self.dice: Optional["Dice"] = None

    def add_player(self, player: "Player") -> None:
        """
        Adds a player to the board.

        Parameters
        ----------
        player : Player
            The player to add.
        """
        self.players.append(player)

    def place_checker(self, checker: "Checker", point: int) -> None:
        """
        Places a checker on a specific point (0..23).

        Parameters
        ----------
        checker : Checker
            The checker to place.
        point : int
            The index of the point (0..23).
        """
        if 0 <= point < 24:
            self.points[point].append(checker)
            checker.colocar_en_posicion(point)

    def move_checker(self, checker: "Checker", from_point: int, to_point: int) -> None:
        """
        Moves a checker from one point to another.

        Parameters
        ----------
        checker : Checker
            The checker to move.
        from_point : int
            The index of the starting point (0..23).
        to_point : int
            The index of the destination point (0..23).
        """
        if 0 <= from_point < 24 and 0 <= to_point < 24:
            if checker in self.points[from_point]:
                self.points[from_point].remove(checker)
                self.points[to_point].append(checker)
                checker.mover_a(to_point)

    def send_to_bar(self, checker: "Checker") -> None:
        """
        Sends a checker to the bar.

        Parameters
        ----------
        checker : Checker
            The checker to send to the bar.
        """
        color = checker.get_color()
        self.bar[color].append(checker)
        checker.enviar_a_barra()

    def bear_off_checker(self, checker: "Checker") -> None:
        """
        Removes a checker from the board (bear off).

        Parameters
        ----------
        checker : Checker
            The checker to bear off.
        """
        color = checker.get_color()
        self.borne_off[color].append(checker)
        checker.sacar()

    def get_checkers_on_point(self, point: int) -> List["Checker"]:
        """
        Returns the list of checkers on a given point.

        Parameters
        ----------
        point : int
            The index of the point (0..23).

        Returns
        -------
        List[Checker]
        """
        if 0 <= point < 24:
            return list(self.points[point])
        return []

    def get_bar(self, color: str) -> List["Checker"]:
        """
        Returns the list of checkers on the bar for a given color.

        Parameters
        ----------
        color : str
            The color ("blancas" or "negras").

        Returns
        -------
        List[Checker]
        """
        return list(self.bar.get(color, []))

    def get_borne_off(self, color: str) -> List["Checker"]:
        """
        Returns the list of checkers that have been borne off for a given color.

        Parameters
        ----------
        color : str
            The color ("blancas" or "negras").

        Returns
        -------
        List[Checker]
        """
        return list(self.borne_off.get(color, []))

    def display(self) -> None:
        """
        Prints the current state of the board, bar, and borne off checkers.

        Returns
        -------
        None

        Examples
        --------
        board = Board()
        board.display()
        """
        print("Tablero:")
        for i, point in enumerate(self.points):
            print(f"Punta {i+1}: {[str(c) for c in point]}")
        print("Barra:")
        for color in self.bar:
            print(f"{color}: {[str(c) for c in self.bar[color]]}")
        print("Fuera (Bear Off):")
        for color in self.borne_off:
            print(f"{color}: {[str(c) for c in self.borne_off[color]]}")

    def reset(self) -> None:
        """
        Resets the board to its initial empty state.

        Returns
        -------
        None
        """
        self.points = [[] for _ in range(24)]
        self.bar = {"blancas": [], "negras": []}
        self.borne_off = {"blancas": [], "negras": []}
        self.players = []
        self.dice = None
