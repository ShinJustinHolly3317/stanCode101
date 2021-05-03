"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Breakout Game:
At beginning, there are layers of bricks and a ball at the center of window.
Control the ball bouncing by the paddle to destroy all the bricks.
However, if you fail to bounce the ball, the ball falls out of range of the window, you will lose 1 HP.
While run out of HP, Game Over!

--You can change your HP by changing the variable NUM_LIVES!!--

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    playing_game(graphics)


def playing_game(graphics):
    """
    todo: this function shows the animation
    :param graphics: object constructed by BreakoutGraphics
    """
    dx = 0
    dy = 0
    now_lives = NUM_LIVES
    bricks_num = graphics.brick_num
    while now_lives != 0 and bricks_num != 0:
        if dx == 0 and dy == 0 and graphics.ball_is_start:
            dx = graphics.get_x_velocity()
            dy = graphics.get_y_velocity()
        graphics.ball.move(dx, dy)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            dx = -dx
        if graphics.ball.y <= 0:
            dy = -dy

        # Position check that can rebound when hitting paddle
        is_break = False  # can remove only one brick each time
        for i in range(0, 2):
            if is_break:
                break
            for j in range(0, 2):
                now_obj = graphics.window.get_object_at(graphics.ball.x + j * graphics.ball.width, graphics.ball.y + i * graphics.ball.height)
                # when touch paddle
                if now_obj == graphics.paddle and dy > 0:
                    dy = -dy
                    # if ball hit the edge of the paddle, need to reverse x direction
                    if graphics.ball.x + j * graphics.ball.width > graphics.paddle.x + graphics.paddle.width * 0.7 and dx < 0 or graphics.ball.x + j * graphics.ball.width < graphics.paddle.x + graphics.paddle.width * 0.3 and dx > 0:
                        dx = -dx
                # when touch bricks
                elif now_obj is not None and now_obj != graphics.paddle:
                    dy = -dy
                    graphics.window.remove(now_obj)
                    bricks_num -= 1
                    is_break = True
                    break

        # Position check when player don't catch the ball
        if graphics.ball.y >= graphics.paddle.y + graphics.paddle.height:
            now_lives -= 1
            if now_lives != 0:
                graphics.window.remove(graphics.ball)
                dx = 0
                dy = 0
                graphics.reset_ball_paddle_position()
                graphics.window.add(graphics.ball)
            graphics.ball_is_start = False
        pause(FRAME_RATE)

    # Ending display
    if now_lives == 0:
        graphics.window.add(graphics.apology, (graphics.window.width - graphics.apology.width) / 2, graphics.window.height / 2)
    elif bricks_num == 0:
        graphics.window.add(graphics.congrats, (graphics.window.width - graphics.congrats.width) / 2,
                            graphics.window.height / 2)
    graphics.ball_is_start = False
    graphics.end_game = True


if __name__ == '__main__':
    main()
