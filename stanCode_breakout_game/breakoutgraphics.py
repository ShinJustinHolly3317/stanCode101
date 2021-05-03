"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program uses 2 classes to create the bricks / ball /  paddle / string 'You are dead'/ string 'Congratulations'.
Control the size / color /  initial position / initial speed of ball, paddle, bricks.
Also do mouse listeners to communicate with system.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
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

INITIAL_Y_SPEED = 3    # Initial vertical speed for the ball. 7
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.

BRICK_COLOR = ['beige', 'bisque', 'burlywood', 'chocolate', 'darkred']


class EndingGraphics:
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


class BreakoutGraphics(EndingGraphics):
    """
    This class construct the instances of ball, paddle, bricks by entering the parameters.
    """
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        # get EndingGraphics parameter, but do not window.add()
        super().__init__()

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width)/2, y=self.window.height - PADDLE_OFFSET)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius, x=window_width/2 - ball_radius, y=window_height/2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.ball_is_start = False

        # Draw bricks
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.brick = GRect(brick_width, brick_height, x=0, y=brick_offset)
        self.brick.filled = True
        self.brick_num = self.bricks_duplicate(brick_rows, brick_cols)

        # Initialize our mouse listeners
        # 2 switches variables control whether it's it can be played or not, if game over, cannot trigger mouse listener
        # also control it can now be mousemoved or mouseclicked
        self.is_start_game = False  # switch variable
        self.end_game = False       # switch variable
        onmouseclicked(self.start_game)
        onmousemoved(self.mouse_hover)

    # Method: When mouse clicked, give a random x velocity
    def start_game(self, event):
        if not self.ball_is_start:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED
            self.ball_is_start = True

    # getter: get the value of x velocity
    def get_x_velocity(self):
        return self.__dx

    # getter: get the value of y velocity
    def get_y_velocity(self):
        return self.__dy

    # Method: control paddle position when mousemoved
    def mouse_hover(self, event):
        if self.ball_is_start and not self.end_game:
            self.paddle.x = event.x - self.paddle.width/2
            if self.paddle.x < 0:
                self.paddle.x = 0
            if self.paddle.x + self.paddle.width > self.window.width:
                self.paddle.x = self.window.width - self.paddle.width

    # Method: create layers of bricks
    def bricks_duplicate(self, row, col):
        """
        :param row: number of the rows of bricks, can be changed if player enter another number
        :param col: number of the rows of bricks, can be changed if player enter another number
        :return: number how many bricks in this game
        """
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



