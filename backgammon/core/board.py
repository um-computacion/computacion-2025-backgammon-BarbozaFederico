from typing import List, Optional, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from backgammon.core.player import (
        Player,
        OpcionMovimiento,
        PasoMovimiento,
        SecuenciaMovimiento,
    )
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
        if checker is None:
            return
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
        if checker is None:
            return
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
        if checker is None:
            return
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
        print("Picos:")
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

    def jugador_tiene_en_barra(self, player: "Player") -> bool:
        """
        Checks if a player has any checkers on the bar.

        Parameters
        ----------
        player : Player
            The player to check

        Returns
        -------
        bool
            True if the player has checkers on the bar
        """
        color = player.get_color()
        return len(self.bar[color]) > 0

    def jugador_todo_en_home(self, player: "Player") -> bool:
        """
        Checks if all of a player's checkers are in their home area.

        Parameters
        ----------
        player : Player
            The player to check

        Returns
        -------
        bool
            True if all checkers are in home area (not on bar, not borne off)
        """
        # If player has checkers on the bar, they're not all in home
        if self.jugador_tiene_en_barra(player):
            return False

        home_points = player.get_home_points()

        # Check all checkers that are still in play (not borne off)
        for checker in player.get_checkers():
            if not checker.fuera():  # If checker is not borne off
                if checker.en_barra():  # If on bar
                    return False
                elif checker.en_tablero():  # If on board
                    pos = checker.get_posicion()
                    if pos not in home_points:
                        return False

        return True

    def jugador_pip_count(self, player: "Player") -> int:
        """
        Calculates the pip count for a player.

        Parameters
        ----------
        player : Player
            The player to calculate pip count for

        Returns
        -------
        int
            The total pip count (distance to bear off all checkers)
        """
        pip_count = 0
        direccion = player.get_direccion()
        home_points = player.get_home_points()

        # Calculate the bearing off point based on direction
        if direccion == 1:  # white moves from low to high numbers
            bear_off_point = max(home_points)
        else:  # black moves from high to low numbers
            bear_off_point = min(home_points)

        for checker in player.get_checkers():
            if checker.fuera():  # Already borne off
                continue
            elif checker.en_barra():  # On the bar
                entry_point = player.get_entry_point()
                if direccion == 1:
                    pip_count += (bear_off_point - entry_point) + 1
                else:
                    pip_count += (entry_point - bear_off_point) + 1
            elif checker.en_tablero():  # On the board
                pos = checker.get_posicion()
                if direccion == 1:
                    pip_count += max(0, bear_off_point - pos)
                else:
                    pip_count += max(0, pos - bear_off_point)

        return pip_count

    def aplicar_movimiento(
        self, player: "Player", secuencia: "SecuenciaMovimiento"
    ) -> None:
        """
        Applies a sequence of moves to the board.

        Parameters
        ----------
        player : Player
            The player making the move
        secuencia : SecuenciaMovimiento
            Sequence of move steps to apply
        """
        from backgammon.core.player import SecuenciaMovimiento, PasoMovimiento

        for paso in secuencia:
            self._aplicar_paso_movimiento(player, paso)

    def _aplicar_paso_movimiento(
        self, player: "Player", paso: "PasoMovimiento"
    ) -> None:
        """
        Applies a single move step to the board.

        Parameters
        ----------
        player : Player
            The player making the move
        paso : PasoMovimiento
            Single move step to apply
        """
        color = player.get_color()

        # Find the checker to move
        checker = None

        if paso.desde is None:  # Moving from bar
            if self.bar[color]:
                checker = self.bar[color].pop()
        else:  # Moving from a point on the board
            point_checkers = self.points[paso.desde]
            # Find a checker of the right color
            for c in point_checkers:
                if c.get_color() == color:
                    checker = c
                    point_checkers.remove(c)
                    break

        if checker is None:
            raise ValueError(f"No checker found to move for step: {paso}")

        # Handle captures if needed
        if paso.captura and paso.hasta is not None:
            # Remove opponent's checker from destination point
            dest_checkers = self.points[paso.hasta]
            if dest_checkers:
                captured_checker = dest_checkers.pop()
                # Send to bar
                captured_color = captured_checker.get_color()
                self.bar[captured_color].append(captured_checker)
                captured_checker.enviar_a_barra()

        # Move the checker to destination
        if paso.hasta is None:  # Bear off
            self.borne_off[color].append(checker)
            checker.sacar()
        else:  # Move to a point
            self.points[paso.hasta].append(checker)
            checker.mover_a(paso.hasta)

    def _generar_movimientos_posibles(
        self, player: "Player", die_value: int, tablero: "Board"
    ) -> List["PasoMovimiento"]:
        """
        Genera todos los movimientos posibles para un jugador con un valor de dado específico,
        aplicando la regla de prioridad de bear-off.
        """
        from backgammon.core.player import PasoMovimiento

        moves: List["PasoMovimiento"] = []
        color = player.get_color()
        direccion = player.get_direccion()

        # Prioridad 1: Si el jugador tiene fichas en la barra, debe meterlas primero
        if tablero.jugador_tiene_en_barra(player):
            entry_point = player.get_entry_point()
            target_point = entry_point + (die_value * direccion)
            if self._es_movimiento_valido(player, None, target_point, tablero):
                captura = self._es_captura(player, target_point, tablero)
                moves.append(
                    PasoMovimiento(
                        desde=None, hasta=target_point, dado=die_value, captura=captura
                    )
                )
            return moves

        # Si no puede hacer bear-off, solo se generan movimientos regulares
        if not player.puede_bear_off(tablero):
            for point in range(24):
                if any(
                    c.get_color() == color for c in tablero.get_checkers_on_point(point)
                ):
                    target_point = point + (die_value * direccion)
                    if 0 <= target_point < 24 and self._es_movimiento_valido(
                        player, point, target_point, tablero
                    ):
                        captura = self._es_captura(player, target_point, tablero)
                        moves.append(
                            PasoMovimiento(
                                desde=point,
                                hasta=target_point,
                                dado=die_value,
                                captura=captura,
                            )
                        )
            return moves

        # Lógica de Bear-off:
        # 1. Buscar si existe un movimiento exacto para sacar una ficha.
        exact_move_point = -1
        point_needed = (24 - die_value) if direccion == 1 else (die_value - 1)

        if 0 <= point_needed < 24 and any(
            c.get_color() == color for c in tablero.get_checkers_on_point(point_needed)
        ):
            exact_move_point = point_needed

        # 2. Generar todos los movimientos regulares posibles dentro del tablero.
        regular_moves = []
        for point in range(24):
            if any(
                c.get_color() == color for c in tablero.get_checkers_on_point(point)
            ):
                target_point = point + (die_value * direccion)
                if 0 <= target_point < 24 and self._es_movimiento_valido(
                    player, point, target_point, tablero
                ):
                    captura = self._es_captura(player, target_point, tablero)
                    regular_moves.append(
                        PasoMovimiento(
                            desde=point,
                            hasta=target_point,
                            dado=die_value,
                            captura=captura,
                        )
                    )

        # 3. Determinar qué movimientos de bear-off son válidos.
        if exact_move_point != -1:
            # Si existe un movimiento exacto, solo ese bear-off es válido.
            exact_bear_off_move = PasoMovimiento(
                desde=exact_move_point, hasta=None, dado=die_value, captura=False
            )
            return regular_moves + [exact_bear_off_move]
        else:
            # No hay movimiento exacto. Se permite un bear-off "por exceso" solo
            # desde la ficha más alejada, si el dado es mayor que la distancia.
            farthest_point_with_checker = -1
            home_points = player.get_home_points()

            # Para las blancas (dirección 1), la ficha más lejana está en el índice más bajo.
            # Para las negras (dirección -1), está en el índice más alto.
            search_range = sorted(list(home_points), reverse=(direccion == -1))

            for p in search_range:
                if any(
                    c.get_color() == color for c in tablero.get_checkers_on_point(p)
                ):
                    farthest_point_with_checker = p
                    break

            if farthest_point_with_checker != -1:
                point_for_exact_move = (24 - die_value) if direccion == 1 else (die_value - 1)

                can_bear_off_inexact = False
                if direccion == 1: # Blancas
                    if farthest_point_with_checker < point_for_exact_move:
                        can_bear_off_inexact = True
                else: # Negras
                    if farthest_point_with_checker > point_for_exact_move:
                        can_bear_off_inexact = True

                # Además, no debe haber ninguna ficha entre el punto exacto y el final.
                has_checkers_beyond_exact = False
                if direccion == 1:
                    for p in range(point_for_exact_move):
                        if any(c.get_color() == color for c in tablero.get_checkers_on_point(p)):
                            has_checkers_beyond_exact = True
                            break
                else:
                     for p in range(point_for_exact_move + 1, 24):
                        if any(c.get_color() == color for c in tablero.get_checkers_on_point(p)):
                            has_checkers_beyond_exact = True
                            break

                if not has_checkers_beyond_exact:
                    inexact_bear_off_move = PasoMovimiento(
                        desde=farthest_point_with_checker,
                        hasta=None,
                        dado=die_value,
                        captura=False,
                    )
                    return regular_moves + [inexact_bear_off_move]

        # Si no hay movimientos de bear-off válidos, devolver solo los regulares.
        return regular_moves

    def _es_movimiento_valido(
        self,
        player: "Player",
        desde: Optional[int],
        hasta: Optional[int],
        tablero: "Board",
    ) -> bool:
        """
        Checks if a move is valid according to backgammon rules.

        Parameters
        ----------
        player : Player
            The player making the move
        desde : Optional[int]
            Source point (None if from bar)
        hasta : Optional[int]
            Target point (None if bearing off)
        tablero : Board
            Current board state

        Returns
        -------
        bool
            True if the move is valid
        """
        color = player.get_color()

        # If bearing off, the move is valid as long as the player can bear off
        if hasta is None:
            return player.puede_bear_off(tablero)

        # Check if player has checkers at source point (unless moving from bar or bearing off)
        if desde is not None:
            checkers_at_source = tablero.get_checkers_on_point(desde)
            player_checkers_at_source = [
                c for c in checkers_at_source if c.get_color() == color
            ]
            if not player_checkers_at_source:
                return False

        # If point is out of range, it's invalid
        if hasta < 0 or hasta >= 24:
            return False

        # Check destination point
        checkers_at_dest = tablero.get_checkers_on_point(hasta)

        # If empty, it's valid
        if not checkers_at_dest:
            return True

        # If has player's own checkers, it's valid
        if checkers_at_dest[0].get_color() == color:
            return True

        # If has opponent's checkers but only one, it's valid (blot)
        if len(checkers_at_dest) == 1:
            return True

        # If has multiple opponent checkers, it's invalid
        return False

    def _es_captura(self, player: "Player", punto: int, tablero: "Board") -> bool:
        """
        Checks if a move would result in capturing an opponent's checker.

        Parameters
        ----------
        player : Player
            The player making the move
        punto : int
            Target point
        tablero : Board
            Current board state

        Returns
        -------
        bool
            True if the move would result in a capture
        """
        if punto < 0 or punto >= 24:
            return False

        checkers_at_dest = tablero.get_checkers_on_point(punto)

        if not checkers_at_dest:
            return False

        color = player.get_color()
        if checkers_at_dest[0].get_color() != color and len(checkers_at_dest) == 1:
            return True

        return False

    def _calcular_hash_secuencia(
        self, player: "Player", secuencia: List["PasoMovimiento"]
    ) -> str:
        """
        Calculates a hash string for a move sequence.

        Parameters
        ----------
        player : Player
            The player making the moves
        secuencia : List[PasoMovimiento]
            The move sequence

        Returns
        -------
        str
            A string hash representing the sequence
        """
        # Simple implementation - just stringify the sequence
        steps = []
        for paso in secuencia:
            desde_str = "Bar" if paso.desde is None else str(paso.desde)
            hasta_str = "Off" if paso.hasta is None else str(paso.hasta)
            capture_str = "C" if paso.captura else ""
            steps.append(f"{desde_str}->{hasta_str}({paso.dado}){capture_str}")

        player_color = "None" if player is None else player.get_color()
        return f"{player_color}:{'|'.join(steps)}"

    def oponente_en_cuadrante(self, player: "Player") -> bool:
        """
        Checks if there is any opponent checker in the player's home board.
        """
        home_points = player.get_home_points()
        opponent_color = "negras" if player.get_color() == "blancas" else "blancas"

        for point in home_points:
            checkers = self.get_checkers_on_point(point)
            if checkers and checkers[0].get_color() == opponent_color:
                return True
        return False


class prueba1:
    pass
