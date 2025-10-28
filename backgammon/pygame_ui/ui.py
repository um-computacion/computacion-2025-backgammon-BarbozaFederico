import pygame
import sys
import time
import random
from backgammon.core.backgammon import BackgammonGame
from backgammon.core.player import PasoMovimiento, SecuenciaMovimiento

# Constants
WIDTH, HEIGHT = 1400, 800

# --- Nueva Paleta de Colores ---
# --- Nueva Paleta de Colores (Dark Edition) ---

COLOR_FONDO_TABLERO   = (40, 40, 45)      # Gris grafito oscuro (fondo principal)
COLOR_TRIANGULO_CLARO = (175, 155, 135)   # Beige apagado
COLOR_TRIANGULO_OSCURO= (92, 64, 51)      # Marrón chocolate profundo

COLOR_FONDO_MESA      = (32, 32, 35)      # Gris muy oscuro (background interno)
COLOR_BEAR_OFF_BAR    = (110, 85, 60)     # Madera tostada (zona de borneado)

COLOR_PIEZA_NEGRA     = (15, 15, 15)      # Negro mate
COLOR_PIEZA_BLANCA    = (245, 240, 230)   # Marfil cálido (evita blanco chillón)

COLOR_BORDE_FICHA     = (153, 45, 45)     # Vino oscuro suave (en vez de rojo puro)
COLOR_TEXTO_NEGRO     = (230, 230, 230)   # Gris claro para texto sobre fondo oscuro
COLOR_TEXTO_BLANCO    = (250, 244, 227)   # Blanco cálido para contraste

COLOR_HIGHLIGHT       = (0, 155, 130)     # Verde azulado profundo (destaca sin molestar)
COLOR_BOTON_HOVER     = (119, 97, 82)     # Marrón suave (hover amigable)


# --- Colores Antiguos (se mantendrán si son necesarios para elementos no temáticos) ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BOARD_COLOR = COLOR_FONDO_TABLERO
GREEN = (0, 255, 0)


# Game States
SELECCION_COLOR = "SELECCION_COLOR"
TIRADA_INICIAL = "TIRADA_INICIAL"
JUEGO = "JUEGO"


class PygameUI:
    """
    A class to handle the Pygame user interface for the Backgammon game.
    """

    def __init__(self):
        """
        Initializes the Pygame UI.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Backgammon")
        self.font = pygame.font.Font(None, 24)
        self.large_font = pygame.font.Font(None, 74)
        self.clock = pygame.time.Clock()

        # Game state
        self.estado_juego = SELECCION_COLOR
        self.dados_iniciales = {"blancas": 0, "negras": 0}
        self.ganador_tirada_inicial = None
        self.tiempo_inicio_tirada = None
        self.boton_empezar_rect = None
        self.juego_iniciado = False

        self.game_over = False
        self.winner = None
        self.game_over_time = None

        # Dynamic board layout constants
        self.board_edge = int(WIDTH * 0.02)
        self.point_height = int(HEIGHT * 0.4)

        # Define a specific width for the main board area, leaving space for bear-off etc.
        main_board_width_ratio = 0.85  # Let's say the main board takes 85% of the width
        playing_width = int(WIDTH * main_board_width_ratio) - (2 * self.board_edge)

        # We have 12 points and 1 bar. Bar is ~1.5x a point.
        # Total units = 12 + 1.5 = 13.5
        unit_width = playing_width / 13.5
        self.point_width = int(unit_width)
        self.bar_width = int(unit_width * 1.5)

        self.checker_radius = int(self.point_width * 0.4)
        self.selected_point = None
        self.point_rects = [None] * 24
        self.bar_rects = {}
        self.bear_off_rects = {}
        self._calculate_point_rects()
        self._calculate_bar_rects()
        self._calculate_bear_off_rects()
        self.used_dice = []
        self.possible_moves = []
        self.possible_dests = []
        self.selected_source = None  # Can be point index or 'bar'

        self.game = BackgammonGame()
        # self._setup_game() will be called after the initial screens

    def _calculate_bar_rects(self):
        """Calculates the clickable rects for each player's bar."""
        bar_x = self.board_edge + 6 * self.point_width
        self.bar_rects["blancas"] = pygame.Rect(bar_x, 0, self.bar_width, HEIGHT / 2)
        self.bar_rects["negras"] = pygame.Rect(
            bar_x, HEIGHT / 2, self.bar_width, HEIGHT / 2
        )

    def _calculate_bear_off_rects(self):
        """Calculates the clickable rects for each player's bear-off area."""
        # This area is now to the right of the main board
        bear_off_x = (
            self.board_edge + (12 * self.point_width) + self.bar_width + self.board_edge
        )
        bear_off_width = WIDTH - bear_off_x - self.board_edge

        # White's bear-off is top-right
        self.bear_off_rects["blancas"] = pygame.Rect(
            bear_off_x, self.board_edge, bear_off_width, self.point_height
        )

        # Black's bear-off is bottom-right
        self.bear_off_rects["negras"] = pygame.Rect(
            bear_off_x,
            HEIGHT - self.board_edge - self.point_height,
            bear_off_width,
            self.point_height,
        )

    def _setup_game(self):
        """Sets up the players and starts the game."""
        player_configs = [
            {
                "id": "P1",
                "nombre": "Blanco",
                "color": "blancas",
                "direccion": 1,
                "home_points": range(18, 24),
                "entry_point": -1,
            },
            {
                "id": "P2",
                "nombre": "Negro",
                "color": "negras",
                "direccion": -1,
                "home_points": range(0, 6),
                "entry_point": 24,
            },
        ]
        self.game.setup_players(player_configs)
        self.game.start_game(
            primer_jugador_color=self.ganador_tirada_inicial
        )
        # La tirada de dados y la configuración del turno se harán en el bucle principal del juego
        self.game.roll_dice()

    def _calculate_point_rects(self):
        """Calculates the clickable rects for each point and stores them."""
        # i is the visual column from left to right
        for i in range(12):
            # Bottom row
            point_x_bottom = self.board_edge + i * self.point_width
            if i >= 6:
                point_x_bottom += self.bar_width

            # The core indices for the bottom row run from 11 (left) to 0 (right)
            core_idx_bottom = 11 - i
            self.point_rects[core_idx_bottom] = pygame.Rect(
                point_x_bottom,
                HEIGHT - self.board_edge - self.point_height,
                self.point_width,
                self.point_height,
            )

            # Top row
            point_x_top = self.board_edge + i * self.point_width
            if i >= 6:
                point_x_top += self.bar_width

            # The core indices for the top row run from 12 (left) to 23 (right)
            core_idx_top = 12 + i
            self.point_rects[core_idx_top] = pygame.Rect(
                point_x_top, self.board_edge, self.point_width, self.point_height
            )

    def _draw_checkers(self):
        """Draws the checkers on the board based on the game state."""
        checker_colors = {"blancas": COLOR_PIEZA_BLANCA, "negras": COLOR_PIEZA_NEGRA}

        # Highlight selected source
        if self.selected_source is not None:
            if self.selected_source == "bar":
                player_color = self.game.get_current_player().get_color()
                rect = self.bar_rects[player_color]
            else:
                rect = self.point_rects[self.selected_source]
            pygame.draw.rect(self.screen, COLOR_HIGHLIGHT, rect, 4)

        # Draw checkers on points first
        for point_idx, checkers in enumerate(self.game.board.points):
            if not checkers:
                continue

            rect = self.point_rects[point_idx]
            color = checker_colors[checkers[0].get_color()]
            is_top_row = point_idx >= 12
            direction = 1 if is_top_row else -1
            base_y = (
                rect.top + self.checker_radius
                if is_top_row
                else rect.bottom - self.checker_radius
            )

            for i, checker in enumerate(checkers):
                if i >= 5:
                    count_text = self.font.render(str(len(checkers)), True, RED)
                    text_y = base_y + (4 * 2 * self.checker_radius * direction)
                    self.screen.blit(
                        count_text, (rect.centerx - count_text.get_width() / 2, text_y)
                    )
                    break
                center_x = rect.centerx
                center_y = base_y + (i * 2 * self.checker_radius * direction)
                pygame.draw.circle(
                    self.screen, color, (center_x, center_y), self.checker_radius
                )
                pygame.draw.circle(
                    self.screen, COLOR_BORDE_FICHA, (center_x, center_y), self.checker_radius, 2
                )

        # Draw checkers on the bar
        bar_x = self.board_edge + 6 * self.point_width + self.bar_width / 2
        for color_name, checkers in self.game.board.bar.items():
            color = checker_colors[color_name]
            y_pos = (
                HEIGHT / 2 - self.checker_radius
                if color_name == "blancas"
                else HEIGHT / 2 + self.checker_radius
            )
            direction = -1 if color_name == "blancas" else 1
            for i, checker in enumerate(checkers):
                center_y = y_pos + (i * 2 * self.checker_radius * direction)
                pygame.draw.circle(
                    self.screen, color, (bar_x, center_y), self.checker_radius
                )
                pygame.draw.circle(
                    self.screen, COLOR_BORDE_FICHA, (bar_x, center_y), self.checker_radius, 2
                )

        # Draw borne-off checkers count inside the bear-off areas
        white_borne_off = len(self.game.board.get_borne_off("blancas"))
        if white_borne_off > 0:
            white_rect = self.bear_off_rects["blancas"]
            white_text = self.font.render(f"Off: {white_borne_off}", True, COLOR_TEXTO_NEGRO)
            self.screen.blit(
                white_text,
                (
                    white_rect.centerx - white_text.get_width() / 2,
                    white_rect.centery - white_text.get_height() / 2,
                ),
            )

        black_borne_off = len(self.game.board.get_borne_off("negras"))
        if black_borne_off > 0:
            black_rect = self.bear_off_rects["negras"]
            black_text = self.font.render(f"Off: {black_borne_off}", True, COLOR_TEXTO_BLANCO)
            self.screen.blit(
                black_text,
                (
                    black_rect.centerx - black_text.get_width() / 2,
                    black_rect.centery - black_text.get_height() / 2,
                ),
            )

        # Now, draw the highlights on top of everything
        for dest in self.possible_dests:
            if dest == "bear_off":
                player_color = self.game.get_current_player().get_color()
                rect = self.bear_off_rects[player_color]
                pygame.draw.rect(self.screen, COLOR_HIGHLIGHT, rect, 4)
            else:
                rect = self.point_rects[dest]
                pygame.draw.circle(
                    self.screen, COLOR_HIGHLIGHT, rect.center, self.checker_radius * 0.3
                )

    def _draw_game_over_screen(self):
        """Draws the game over screen."""
        # Create a semi-transparent overlay
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))  # Black with alpha
        self.screen.blit(overlay, (0, 0))

        # Display winner message
        winner_text = f"¡Gana el jugador {self.winner.get_nombre()}!"
        text_surface = self.large_font.render(winner_text, True, COLOR_TEXTO_BLANCO)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.screen.blit(text_surface, text_rect)

    def _draw_game_info(self):
        """Displays the current player and dice roll."""
        player = self.game.get_current_player()
        dice = self.game.dice.get_values()

        player_text = f"Turn: {player.get_nombre()} ({player.get_color()})"
        dice_text = f"Dice: {dice[0]}, {dice[1]}" if dice else "Dice: Not rolled"

        player_surface = self.font.render(player_text, True, COLOR_TEXTO_NEGRO)
        dice_surface = self.font.render(dice_text, True, COLOR_TEXTO_NEGRO)

        info_x = self.board_edge + 6 * self.point_width + self.bar_width / 2

        self.screen.blit(
            player_surface, (info_x - player_surface.get_width() / 2, self.board_edge)
        )
        self.screen.blit(
            dice_surface, (info_x - dice_surface.get_width() / 2, self.board_edge + 30)
        )

    def _draw_board(self):
        """
        Draws the static elements of the backgammon board using pre-calculated rects.
        """
        # Dibuja el fondo de la mesa y el marco del tablero
        self.screen.fill(COLOR_FONDO_MESA)
        pygame.draw.rect(
            self.screen, COLOR_FONDO_TABLERO, (0, 0, WIDTH, HEIGHT), self.board_edge * 2
        )

        # Dibuja la barra central
        bar_x = self.board_edge + 6 * self.point_width
        pygame.draw.rect(self.screen, COLOR_FONDO_TABLERO, (bar_x, 0, self.bar_width, HEIGHT))

        # Dibuja las áreas de bear-off
        for color, rect in self.bear_off_rects.items():
            pygame.draw.rect(self.screen, COLOR_BEAR_OFF_BAR, rect)

        # Colores de los triángulos
        color1 = COLOR_TRIANGULO_CLARO
        color2 = COLOR_TRIANGULO_OSCURO

        # Dibuja los triángulos y los números
        for i, rect in enumerate(self.point_rects):
            if rect is None:
                continue

            # Determine color based on visual column
            if i >= 12:
                vis_i = i - 12
            else:
                vis_i = 11 - i
            point_color = (
                color1 if vis_i % 2 != 0 else color2
            )  # Flipped this to match original look

            # Draw triangle
            if i >= 12:  # Top row points down
                pygame.draw.polygon(
                    self.screen,
                    point_color,
                    [rect.topleft, rect.topright, rect.midbottom],
                )
            else:  # Bottom row points up
                pygame.draw.polygon(
                    self.screen,
                    point_color,
                    [rect.bottomleft, rect.bottomright, rect.midtop],
                )

            # Draw number
            ui_number = i + 1
            num_text = self.font.render(str(ui_number), True, COLOR_TEXTO_NEGRO)
            if i >= 12:  # Top row
                self.screen.blit(
                    num_text, (rect.centerx - num_text.get_width() / 2, rect.bottom + 5)
                )
            else:  # Bottom row
                self.screen.blit(
                    num_text, (rect.centerx - num_text.get_width() / 2, rect.top - 25)
                )

    def _get_point_from_pos(self, pos):
        """Converts mouse coordinates to a board point index (0-23)."""
        for i, rect in enumerate(self.point_rects):
            if rect and rect.collidepoint(pos):
                return i
        return None

    def _get_bear_off_from_pos(self, pos):
        """Checks if the mouse click is on a valid bear-off area."""
        player = self.game.get_current_player()
        if self.bear_off_rects[player.get_color()].collidepoint(pos):
            return "bear_off"
        return None

    def _get_possible_dests(self, source):
        """
        Calculates and returns possible destinations for a given source
        based on the current available dice.
        This now dynamically recalculates moves for each die.
        """
        dests = []
        start_point = None if source == "bar" else source
        player = self.game.get_current_player()
        available_dice = self._get_available_dice()

        # We need to check moves for each unique die value
        for die_value in set(available_dice):
            # Generate moves for the current board state and one die
            # Note: _generar_movimientos_posibles returns PasoMovimiento, not OpcionMovimiento
            possible_steps = self.game.board._generar_movimientos_posibles(
                player, die_value, self.game.board
            )
            for paso in possible_steps:
                if paso.desde == start_point:
                    if paso.hasta is None:
                        dests.append("bear_off")
                    else:
                        dests.append(paso.hasta)
        return list(set(dests))

    def _attempt_move(self, source, destination):
        """
        Finds a valid move, applies it, and updates the game state.
        The logic is now simpler as it handles one move at a time.
        """
        player = self.game.get_current_player()
        start_idx = None if source == "bar" else source
        dest_idx = None if destination == "bear_off" else destination
        available_dice = self._get_available_dice()

        # Find which die can make this move
        move_to_apply = None
        used_die = None

        for die_value in sorted(
            list(set(available_dice)), reverse=True
        ):  # Prefer larger dice for ambiguity
            possible_steps = self.game.board._generar_movimientos_posibles(
                player, die_value, self.game.board
            )
            for paso in possible_steps:
                if paso.desde == start_idx and paso.hasta == dest_idx:
                    move_to_apply = paso
                    used_die = die_value
                    break
            if move_to_apply:
                break

        if not move_to_apply:
            print(
                f"ERROR: No valid die found for move from {source} to {destination}. This should not happen."
            )
            self.selected_source = None
            self.possible_dests = []
            return

        # Apply the single move
        self.game.board.aplicar_movimiento(player, [move_to_apply])
        self.used_dice.append(used_die)

        # Reset UI state for the next action in the turn
        self.selected_source = None
        self.possible_dests = []

        # After the move, check if the turn should end
        if not self._get_available_dice() or not self._has_any_legal_moves():
            self._end_turn()

    def _get_current_dice(self):
        """Returns the full list of dice for the current turn, handling doubles."""
        dice = list(self.game.dice.get_values())
        if not dice:
            return []
        if len(dice) == 2 and dice[0] == dice[1]:
            # If some doubles have been used, return the correct remaining number
            return [dice[0]] * 4
        return dice

    def _get_available_dice(self):
        """Returns the dice that have not yet been used this turn."""
        available = self._get_current_dice()
        for die in self.used_dice:
            if die in available:
                available.remove(die)
        return available

    def _has_any_legal_moves(self):
        """Checks if there are any legal moves for any of the available dice."""
        player = self.game.get_current_player()
        available_dice = self._get_available_dice()
        # Test each unique die value. If any of them yield a move, return True.
        for die_value in set(available_dice):
            if self.game.board._generar_movimientos_posibles(
                player, die_value, self.game.board
            ):
                return True
        return False

    def _end_turn(self):
        """Finalizes the current turn and sets up the next one."""
        print("--- Turno finalizado ---")

        if self.game.is_game_over():
            self.game_over = True
            self.winner = self.game.get_current_player()
            self.game_over_time = time.time()
            return

        self.game.next_turn()
        self.game.roll_dice()
        self.used_dice = []
        self.selected_source = None
        self.possible_dests = []
        print(
            f"Nuevo turno para {self.game.get_current_player().get_nombre()} con dados {self.game.dice.get_values()}"
        )

        # At the start of the new turn, immediately check if there are any moves.
        # If not, end the turn right away.
        if not self._has_any_legal_moves():
            print("No hay movimientos legales. Pasando el turno automáticamente.")
            # Give a brief moment for the user to see the dice roll before skipping.
            self._draw_board()
            self._draw_checkers()
            self._draw_game_info()
            pygame.display.flip()
            pygame.time.wait(1500)  # Wait 1.5 seconds
            self._end_turn()

    def _handle_click(self, pos):
        """Handles a mouse click, re-evaluating moves dynamically."""
        player = self.game.get_current_player()
        clicked_point = self._get_point_from_pos(pos)
        clicked_bear_off = self._get_bear_off_from_pos(pos)
        clicked_destination = (
            clicked_point if clicked_point is not None else clicked_bear_off
        )

        # If a source is selected, a click can mean one of three things:
        if self.selected_source is not None:
            # 1. Click on a valid destination: attempt the move
            if clicked_destination in self.possible_dests:
                self._attempt_move(self.selected_source, clicked_destination)
                return
            # 2. Click on the same source: deselect
            elif clicked_point == self.selected_source:
                self.selected_source = None
                self.possible_dests = []
                return
            # 3. Click on another valid source: switch selection
            elif clicked_point is not None and self._is_valid_source(clicked_point):
                self.selected_source = clicked_point
                self.possible_dests = self._get_possible_dests(self.selected_source)
                return
            # 4. Click anywhere else: deselect
            else:
                self.selected_source = None
                self.possible_dests = []
                return

        # If no source is selected, a click can mean:
        # 1. Click on the bar (if checkers are present): select the bar as source
        if self.game.board.jugador_tiene_en_barra(player):
            if self.bar_rects[player.get_color()].collidepoint(pos):
                self.selected_source = "bar"
                self.possible_dests = self._get_possible_dests(self.selected_source)
        # 2. Click on a point with the player's checkers: select the point as source
        elif clicked_point is not None and self._is_valid_source(clicked_point):
            self.selected_source = clicked_point
            self.possible_dests = self._get_possible_dests(self.selected_source)

    def _is_valid_source(self, point_idx):
        """Check if a point is a valid source for a move."""
        player = self.game.get_current_player()
        # Must have checkers of the player's color
        if (
            not self.game.board.points[point_idx]
            or self.game.board.points[point_idx][0].get_color() != player.get_color()
        ):
            return False
        # Must have at least one possible destination
        if not self._get_possible_dests(point_idx):
            return False
        return True

    def _draw_boton_redondeado(self, text, rect, text_color, bg_color, hover_color, radius=20):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = rect.collidepoint(mouse_pos)

        color_actual = hover_color if is_hovered else bg_color

        # Dibuja el rectángulo redondeado
        pygame.draw.rect(self.screen, color_actual, rect, border_radius=radius)

        # Dibuja el texto
        text_surface = self.large_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def _draw_pantalla_seleccion_color(self):
        self.screen.fill(COLOR_FONDO_MESA)
        titulo_surface = self.large_font.render(
            "Bienvenido/a a Backgammon", True, COLOR_TEXTO_NEGRO
        )
        titulo_rect = titulo_surface.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        self.screen.blit(titulo_surface, titulo_rect)

        # Botón Empezar
        empezar_text = "Empezar"
        empezar_surface = self.large_font.render(empezar_text, True, COLOR_TEXTO_BLANCO)
        empezar_rect_inflated = empezar_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2)).inflate(40, 20)
        self.boton_empezar_rect = empezar_rect_inflated

        self._draw_boton_redondeado(
            empezar_text,
            self.boton_empezar_rect,
            COLOR_TEXTO_BLANCO,
            COLOR_FONDO_TABLERO,
            COLOR_BOTON_HOVER,
        )

    def _handle_eventos_seleccion_color(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.boton_empezar_rect and self.boton_empezar_rect.collidepoint(
                event.pos
            ):
                self.estado_juego = TIRADA_INICIAL

    def _draw_pantalla_tirada_inicial(self):
        self.screen.fill(COLOR_FONDO_MESA)
        if not self.ganador_tirada_inicial:
            msg = "Tirando dados..."
        else:
            msg = f"Blancas: {self.dados_iniciales['blancas']} | Negras: {self.dados_iniciales['negras']}"

        texto_surface = self.large_font.render(msg, True, COLOR_TEXTO_NEGRO)
        texto_rect = texto_surface.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        self.screen.blit(texto_surface, texto_rect)

        if self.ganador_tirada_inicial and self.ganador_tirada_inicial != "empate":
            ganador_msg = f"Comienzan las {self.ganador_tirada_inicial}"
            ganador_surface = self.large_font.render(ganador_msg, True, COLOR_TEXTO_NEGRO)
            ganador_rect = ganador_surface.get_rect(
                center=(WIDTH / 2, HEIGHT / 2)
            )
            self.screen.blit(ganador_surface, ganador_rect)

    def _manejar_logica_tirada_inicial(self):
        ahora = time.time()
        # Si no hay una tirada en curso, empezamos una
        if self.tiempo_inicio_tirada is None:
            self.tiempo_inicio_tirada = ahora
            self.dados_iniciales["blancas"] = random.randint(1, 6)
            self.dados_iniciales["negras"] = random.randint(1, 6)

            if self.dados_iniciales["blancas"] > self.dados_iniciales["negras"]:
                self.ganador_tirada_inicial = "blancas"
            elif self.dados_iniciales["negras"] > self.dados_iniciales["blancas"]:
                self.ganador_tirada_inicial = "negras"
            else:
                # Empate, preparamos para re-tirar después de una pausa
                self.ganador_tirada_inicial = "empate"

        # Lógica de transición
        if self.ganador_tirada_inicial:
            # Si hay un ganador, esperamos para mostrar el resultado y luego cambiamos de estado
            if self.ganador_tirada_inicial != "empate":
                if ahora - self.tiempo_inicio_tirada > 2.5:
                    self.estado_juego = JUEGO
                    self._setup_game()
            # Si es un empate, esperamos un segundo y luego reiniciamos la tirada
            elif self.ganador_tirada_inicial == "empate":
                if ahora - self.tiempo_inicio_tirada > 1.0:
                    self.tiempo_inicio_tirada = None # Esto provocará una nueva tirada en el siguiente frame
                    self.ganador_tirada_inicial = None


    def run(self):
        """The main loop of the game."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.estado_juego == SELECCION_COLOR:
                    self._handle_eventos_seleccion_color(event)
                elif self.estado_juego == JUEGO:
                    if self.game_over:
                        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                            running = False
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            self._handle_click(event.pos)

            # --- State-based Drawing and Logic ---
            if self.estado_juego == SELECCION_COLOR:
                self._draw_pantalla_seleccion_color()
            elif self.estado_juego == TIRADA_INICIAL:
                self._manejar_logica_tirada_inicial()
                self._draw_pantalla_tirada_inicial()
            elif self.estado_juego == JUEGO:
                if not self.juego_iniciado:
                    print(
                        f"Inicia el turno para {self.game.get_current_player().get_nombre()} con dados {self.game.dice.get_values()}"
                    )
                    if not self._has_any_legal_moves():
                        self._end_turn()
                    self.juego_iniciado = True

                self.screen.fill(BOARD_COLOR)
                self._draw_board()
                self._draw_checkers()
                self._draw_game_info()
                if self.game_over:
                    self._draw_game_over_screen()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    ui = PygameUI()
    ui.run()
