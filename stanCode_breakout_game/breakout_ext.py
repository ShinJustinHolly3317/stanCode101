"""
--Justin ver. Breakout--

There are 4 stages:
1. Click to start:
    a blinking string, click to start
2. Enter Your name
    you can enter your name here, but still WIP.
    haven't finish the <-backspace function
3. play to clear all the bricks
    There are layers of bricks and a ball at the center of window.
    Control the ball bouncing by the paddle to destroy all the bricks.
    However, if you fail to bounce the ball, the ball falls out of range of the window, you will lose 1 HP.
    While run out of HP, Game Over!
4. show the scoreboard
    After end of the game, your score will show on the scoreboard ranking!!

--You can change your HP by changing the variable NUM_LIVES!!--

"""

from campy.gui.events.timer import pause
from breakoutgraphics_ext import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics(num_lives=NUM_LIVES)
    playing_game(graphics)


def playing_game(graphics):
    """
    todo: this function shows the animation
    :param graphics: object constructed by BreakoutGraphics
    """
    dx = 0
    dy = 0
    while graphics.player_info.now_lives != 0 and graphics.now_brick_num != 0:
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
                if now_obj == graphics.paddle and dy > 0:
                    dy = -dy
                    # if ball hit the edge of the paddle, need to reverse x direction
                    if graphics.ball.x + j * graphics.ball.width > graphics.paddle.x + graphics.paddle.width * 0.8 and dx < 0 or graphics.ball.x + j * graphics.ball.width < graphics.paddle.x + graphics.paddle.width * 0.2 and dx > 0:
                        dx = -dx

                # When hitting a brick, score + 1!!
                elif now_obj is not None and now_obj != graphics.paddle and now_obj != graphics.player_info.score_show and now_obj != graphics.player_info.hp_show:
                    dy = -dy
                    graphics.window.remove(now_obj)
                    graphics.now_brick_num -= 1
                    graphics.player_info.score += 1
                    graphics.player_info.score_show.text = f'Score: {graphics.player_info.score}'
                    is_break = True
                    break

        # Position check when player don't catch the ball, hp - 1!!
        if graphics.ball.y >= graphics.paddle.y + graphics.paddle.height:
            graphics.player_info.now_lives -= 1
            graphics.player_info.hp_show.text = f'HP: {graphics.player_info.now_lives}'
            if graphics.player_info.now_lives != 0:
                graphics.window.remove(graphics.ball)
                dx = 0
                dy = 0
                graphics.reset_ball_paddle_position()
                graphics.window.add(graphics.ball)
            graphics.ball_is_start = False
        pause(FRAME_RATE)

    # Ending display
    if graphics.player_info.now_lives == 0:
        graphics.window.add(graphics.apology, (graphics.window.width - graphics.apology.width) / 2, graphics.window.height / 2)
    elif graphics.now_brick_num == 0:
        graphics.window.add(graphics.congrats, (graphics.window.width - graphics.congrats.width) / 2,
                            graphics.window.height / 2)
    graphics.ball_is_start = False
    graphics.end_game = True


if __name__ == '__main__':
    main()
