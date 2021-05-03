"""
--Justin ver. Breakout--

This program uses 6 classes to create the bricks / ball /  paddle / string 'You are dead'/ string 'Congratulations'.
Control the size / color /  initial position / initial speed of ball, paddle, bricks.
Also do mouse listeners to communicate with system.
A blinking message click to start as a prologue.
A keyboard to enter players' name while it will show on the scoreboard, which is at the end of th game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
KEYBOARD_OFFSET = 100  # Vertical offset of the keyboard from window top (in pixels).
INPUT_TEXT = 4         # Vertical offset of the input text box from window top (by a certain ratio).


INITIAL_Y_SPEED = 3    # Initial vertical speed for the ball. 7
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.

BRICK_COLOR = ['beige', 'bisque', 'burlywood', 'chocolate', 'darkred']


class StartingGraphics:
    """
    A blinking message tells player should be ready for the game.
    Only construct, not window.add() this message.
    """
    def __init__(self):
        self.prologue = GLabel('Click to Start')
        self.prologue.font = 'Courier-10-bold'
        # switch that control this object only display at the beginning of the game
        self.is_prologue = True

        # Create a white plate to simulate blinking animation
        # self.blank = GRect(self.prologue.width + 100, self.prologue.height + 100)
        # self.blank.color = 'gray'


class EndingGraphics(StartingGraphics):
    """
    This class shows the message:
    If player destroy all the bricks, show 'Congratulations'
    If player lose all his or her lives, show 'You are dead!!!'
    Only construct, not window.add() this message.
    """
    def __init__(self):
        self.congrats = GLabel('Congratulations!!!')
        self.congrats.font = 'Courier-10-bold'

        self.apology = GLabel('You are dead!!!')
        self.apology.font = 'Courier-10-bold'
        super().__init__()


class BreakoutGraphics(EndingGraphics):
    """
    This class construct the instances of ball, paddle, bricks by entering the parameters.
    Only create instances when call the constructor, not window.add() those instances.
    will window.add() by a method: show_objs
    """
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING, num_lives = 3,
                 title='Breakout'):
        # call text of EndingGraphics & StartingGraphics
        super().__init__()

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width)/2, y=self.window.height - paddle_offset)
        self.paddle.filled = True
        # self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius, x=window_width/2 - ball_radius, y=window_height/2 - ball_radius)
        self.ball.filled = True
        # self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.ball_is_start = False

        # Draw bricks
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.brick = GRect(brick_width, brick_height, x=0, y=brick_offset)
        self.brick.filled = True
        self.now_brick_num = 1
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_num = brick_cols * brick_rows  # cannot be modified

        # Player's info
        self.player_info = PlayerInfo(num_lives)

        # Name input, for the scoreboard
        self.name_list = None
        self.name_output = []

        # Score Board
        self.score_board = ScoreBoard(self.window)

        # Initialize our mouse listeners
        # 2 switches variables control whether it's it can be played or not, if game over, cannot trigger mouse listener
        # also control it can now be mousemoved or mouseclicked
        self.is_start_game = False  # switch variable
        self.end_game = False       # switch variable
        onmouseclicked(self.start_game)
        onmousemoved(self.mouse_hover)

        # prologue blinking
        while self.is_prologue:
            # self.window.add(self.blank, self.prologue.x, self.prologue.y)
            self.window.add(self.prologue, (self.window.width - self.prologue.width) / 2, self.window.height / 2)
            pause(500)
            self.window.remove(self.prologue)
            pause(500)

    # Method: When mouse clicked, switch to next stage of this game
    def start_game(self, event):
        # click to start page
        if self.is_prologue:
            self.is_prologue = False
            self.window.remove(self.prologue)
            self.name_list = NameList(self.window)
            self.name_list.text_cursor()
        # enter name page
        elif not self.is_prologue and self.name_list.is_name_input:
            self.name_list.enter_name(event)
            if not self.name_list.is_name_input:
                self.name_output = self.name_list.get_name()
                self.show_objs(self.brick_rows, self.brick_cols)
        # game page
        elif not self.ball_is_start and not self.is_prologue and not self.name_list.is_name_input and not self.end_game:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED
            self.ball_is_start = True
        # scoreboard page
        elif self.end_game:
            self.window.clear()
            self.score_board.print_ranking(self.name_list.name, self.player_info.score)

    # control ball / bricks / paddle /player_info instances display
    def show_objs(self, brick_rows, brick_cols):
        self.window.add(self.paddle)
        self.window.add(self.ball)
        self.now_brick_num = self.bricks_duplicate(brick_rows, brick_cols)
        self.window.add(self.player_info.score_show, self.player_info.score_show.width / 3, self.window.height - self.player_info.score_show.height * 0.6)
        self.window.add(self.player_info.hp_show, self.window.width - self.player_info.hp_show.width * 1.5, self.window.height - self.player_info.hp_show.height * 0.6)

    # getter: get the value of x velocity
    def get_x_velocity(self):
        return self.__dx

    # getter: get the value of y velocity
    def get_y_velocity(self):
        return self.__dy

    # Method: control paddle position when mousemoved
    def mouse_hover(self, event):
        if self.ball_is_start:
            self.paddle.x = event.x - self.paddle.width/2
            if self.paddle.x < 0:
                self.paddle.x = 0
            if self.paddle.x + self.paddle.width > self.window.width:
                self.paddle.x = self.window.width - self.paddle.width

    # Method: create layers of bricks
    def bricks_duplicate(self, row, col):
        brick_height = self.brick_spacing
        for i in range(0, row):
            for j in range(0, col):
                self.brick = GRect(self.brick.width, self.brick.height, x=(self.brick.width + self.brick_spacing) * j, y=brick_height)
                self.brick.filled = True

                # Control colors of bricks
                # if 0 <= i < 2:
                #     self.brick.fill_color = 'beige'
                #     self.brick.color = 'beige'
                # elif 2 <= i < 4:
                #     self.brick.fill_color = 'bisque'
                #     self.brick.color = 'bisque'
                # elif 4 <= i < 6:
                #     self.brick.fill_color = 'burlywood'
                #     self.brick.color = 'burlywood'
                # elif 6 <= i < 8:
                #     self.brick.fill_color = 'chocolate'
                #     self.brick.color = 'chocolate'
                # elif 8 <= i < 10:
                #     self.brick.fill_color = 'darkred'
                #     self.brick.color = 'darkred'
                color_num = i // 2
                self.brick.fill_color = BRICK_COLOR[color_num]
                self.brick.color = BRICK_COLOR[color_num]

                self.window.add(self.brick)
            brick_height += self.brick.height + self.brick_spacing
        return row * col

    def reset_ball_paddle_position(self):
        """
        todo: each round, center the position of ball/ paddle.
        """
        self.ball.x = self.window.width / 2 - self.ball.width / 2
        self.ball.y = self.window.height / 2 - self.ball.width / 2
        self.paddle.x = (self.window.width - self.paddle.width) / 2


class NameList(BreakoutGraphics):
    """
    This class create the text input box and the keyboard that player can enter names.
    """
    def __init__(self, window):
        self.window = window
        self.is_name_input = True
        self.name = []
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_ '

        # Create title
        self.input_title = GLabel('Please enter your name')
        self.input_title.font = 'courier-20'
        self.input_title.color = 'white'
        self.input_title_block = GRect(self.window.width, self.input_title.height * 1.3)
        self.input_title_block.color = 'burlywood'
        self.input_title_block.filled = True
        self.input_title_block.fill_color = 'burlywood'
        self.window.add(self.input_title_block)
        self.window.add(self.input_title, (self.window.width - self.input_title.width) / 2, self.input_title.height*1.3)

        # create keyboard
        for i in range(0, 5):
            for j in range(0, 13):
                self.alphabet_brick = GRect(self.window.width / 13, self.window.width / 13)
                self.alphabet_in_brick = GLabel(self.alphabet[j + i*13])
                self.alphabet_in_brick.font = 'courier-20'
                self.window.add(self.alphabet_brick, self.window.width / 13 * j, (self.window.width / 13 + 5) * i + KEYBOARD_OFFSET)
                self.window.add(self.alphabet_in_brick, self.window.width / 13 * j + (self.alphabet_brick.width  - self.alphabet_in_brick.width)/2, (self.window.width / 13 + 5) * i + self.alphabet_brick.height + KEYBOARD_OFFSET)
        self.enter_key = GRect(self.window.width / 13 * 2, self.window.width / 10)
        self.alphabet_enter = GLabel('Enter')
        self.alphabet_enter.font = 'courier-15'
        self.window.add(self.enter_key, self.window.width / 13 * 11, (self.window.width / 13 + 5) * 5 + KEYBOARD_OFFSET)
        self.window.add(self.alphabet_enter, self.window.width / 13 * 11 + (self.enter_key.width - self.alphabet_enter.width) / 2,
                        (self.window.width / 13 + 5) * 5 + self.enter_key.height * 0.7 + KEYBOARD_OFFSET)

        self.name_input = GLabel('')
        self.name_input.font = 'courier-20'
        self.window.add(self.name_input, 0, self.name_input.height*4)
        self.typing = True
        # self.text_cursor(self.typing)

    def enter_name(self, event):
        now_label = self.window.get_object_at(event.x, event.y)
        if now_label is not None:
            mid_x = now_label.x + now_label.width / 2
            mid_y = now_label.y + now_label.height / 2
            # When clicked on the GRect, re-position to the GLabel of that key
            if now_label.__class__.__name__ != 'GLabel':
                now_label = self.window.get_object_at(mid_x, mid_y)
            if now_label.text == 'Enter':
                self.window.clear()
                self.typing = False
                self.is_name_input = False
                self.name.append(self.name_input.text)
                return
            self.name_input.text += now_label.text

    def text_cursor(self):
        cursor = GLabel('|')
        cursor.font = 'courier-20'
        while self.typing:
            self.window.add(cursor, self.name_input.width + 1, self.name_input.height * 4)
            pause(500)
            self.window.remove(cursor)
            pause(500)

    # getter: get the list of players' name
    def get_name(self):
        return self.name

    # @property
    # def test(self):
    #     return self.alphabet


class PlayerInfo(BreakoutGraphics):
    """
    Show the Score and HP when in the playing game stage
    """
    def __init__(self, num_lives):
        self.score = 0
        self.score_show = GLabel(f'Score: {self.score}')
        self.score_show.font = 'courier-15'
        self.now_lives = num_lives
        self.hp_show = GLabel(f'HP: {self.now_lives}')
        self.hp_show.font = 'courier-15'


class ScoreBoard(BreakoutGraphics):
    """
    This class display the score of top 10 palyers
    """
    def __init__(self, window):
        self.window = window
        self.ranking = None

    # parameter name should be a list, show all the players' score, but I haven't finish the 'play again' function
    # so there will be only one name in it...
    def print_ranking(self, name, score):
        for i in range(1, 10):
            self.ranking = GLabel('')
            self.ranking.font = 'courier-15'
            if len(name) >= i:
                self.ranking.text = f'{i}. {name[i - 1]}: {score}'
            else:
                self.ranking.text = f'{i}. _ _ _ _ _'
            self.window.add(self.ranking, self.window.width * 0.3, (self.ranking.height + BRICK_OFFSET * i) + BRICK_OFFSET)


if __name__ == '__main__':
    # namelist = NameList()
    pass

