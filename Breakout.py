######################################################################
# Name: Derec
# Collaborators (if any):
# Section leader's name: Dash
# Generative AI transcript (if used):
# List of extensions made (if any):
######################################################################

"""
This program (once you have finished it) implements the Breakout game
"""

from pgl import GWindow, GOval, GRect, GLabel
import random

# Constants
GWINDOW_WIDTH = 360           # Width of the graphics window
GWINDOW_HEIGHT = 600          # Height of the graphics window
N_ROWS = 10                      # Number of brick rows
N_COLS = 10                   # Number of brick columns
BRICK_ASPECT_RATIO = 4 / 1    # Width to height ratio of a brick
BRICK_TO_BALL_RATIO = 3 / 1   # Ratio of brick width to ball size
BRICK_TO_PADDLE_RATIO = 2 / 3 # Ratio of brick to paddle width
BRICK_SEP = 2                 # Separation between bricks (in pixels)
TOP_FRACTION = 0.1            # Fraction of window above bricks
BOTTOM_FRACTION = 0.05        # Fraction of window below paddle
N_BALLS = 3                   # Number of balls (lives) in a game
TIME_STEP = 20                # Time step in milliseconds
INITIAL_Y_VELOCITY = 3.0      # Starting y velocity downwards
MIN_X_VELOCITY = 1.0          # Minimum random x velocity
MAX_X_VELOCITY = 3.0          # Maximum random x velocity

# Derived Constants
BRICK_WIDTH = (GWINDOW_WIDTH - (N_COLS + 1) * BRICK_SEP) / N_COLS
BRICK_HEIGHT = BRICK_WIDTH / BRICK_ASPECT_RATIO
PADDLE_WIDTH = BRICK_WIDTH / BRICK_TO_PADDLE_RATIO
PADDLE_HEIGHT = BRICK_HEIGHT / BRICK_TO_PADDLE_RATIO
PADDLE_Y = (1 - BOTTOM_FRACTION) * GWINDOW_HEIGHT - PADDLE_HEIGHT
BALL_DIAMETER = BRICK_WIDTH / BRICK_TO_BALL_RATIO


# Function: breakout
def breakout():
    """The main program for the Breakout game."""
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    yvalue = (GWINDOW_HEIGHT * TOP_FRACTION)
    gw.moving = False
    gw.failcounter = 0
    gw.totalbricks = N_COLS * N_ROWS

    #create bricks
    for row in range(N_ROWS):
        xvalue = 0
        xvalue += BRICK_SEP

        #determines brick color
        for col in range(N_COLS): 
            if row < N_ROWS * 0.2:  
                color = "Red"
            elif row < N_ROWS * 0.4: 
                color = "Orange"
            elif row < N_ROWS * 0.6: 
                color = "Green"                
            elif row < N_ROWS * 0.8:  
                color = "Cyan"
            else:  
                color = "Blue"

            box = GRect(xvalue, yvalue, BRICK_WIDTH, BRICK_HEIGHT)
            box.set_color(color)
            box.set_filled(True)
            gw.add(box) #creates boxes
            xvalue += BRICK_WIDTH
            xvalue += BRICK_SEP
        yvalue += BRICK_HEIGHT
        yvalue += BRICK_SEP

    #create paddle & movement
    paddle = GRect((GWINDOW_WIDTH / 2) - PADDLE_WIDTH / 2, GWINDOW_HEIGHT - BOTTOM_FRACTION * GWINDOW_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT) #sets paddle at middle
    paddle.set_color("Black")
    paddle.set_filled(True)
    gw.add(paddle)
    def mousemove(event):
        paddlex = event.get_x()
        if paddlex > GWINDOW_WIDTH - (PADDLE_WIDTH / 2):
            paddlex = GWINDOW_WIDTH - (PADDLE_WIDTH / 2)
        elif paddlex < (PADDLE_WIDTH / 2):
            paddlex = PADDLE_WIDTH / 2
        paddle.set_location(paddlex - (PADDLE_WIDTH / 2), PADDLE_Y)

    #create ball
    gw.ball = GOval(GWINDOW_WIDTH / 2 - BALL_DIAMETER / 2, GWINDOW_HEIGHT / 2, BALL_DIAMETER, BALL_DIAMETER)
    gw.ball.set_color("Black")
    gw.ball.set_filled(True)
    gw.add(gw.ball)
    gw.vx = random.uniform(MIN_X_VELOCITY, MAX_X_VELOCITY)
    if random.uniform(0,1) < 0.5:
        gw.vx = -gw.vx
    gw.vy = INITIAL_Y_VELOCITY

    #creating ball/finding when the ball hits an object
    def get_colliding_object(): 
        ballx = gw.ball.get_x()
        bally = gw.ball.get_y()
        blockhit = gw.get_element_at(ballx, bally)
        if blockhit == None:
            blockhit = gw.get_element_at(ballx + BALL_DIAMETER, bally)
        if blockhit == None:
            blockhit = gw.get_element_at(ballx, bally + BALL_DIAMETER)
        if blockhit == None:
            blockhit = gw.get_element_at(ballx + BALL_DIAMETER, bally + BALL_DIAMETER)
        if blockhit:
            if blockhit == paddle:
                gw.vy = -gw.vy
            else: 
                gw.vy = -gw.vy
                gw.remove(blockhit)
                gw.totalbricks -= 1

    #setting velocity/ball movement
    def mousedown(event):
        if gw.moving == False and gw.failcounter < N_BALLS:
            gw.moving = True
            ballx = gw.ball.get_x()
            bally = gw.ball.get_y()
            gw.vy = INITIAL_Y_VELOCITY  
            while gw.moving == True and gw.totalbricks > 0:
                bally = bally + gw.vy
                ballx = ballx + gw.vx
                gw.ball.set_location(ballx, bally)
                if bally <= 0:
                    gw.vy = -1 * gw.vy
                if ballx <= 0 or ballx >= GWINDOW_WIDTH - BALL_DIAMETER:
                    gw.vx = -1 * gw.vx
                if bally >= GWINDOW_HEIGHT - BALL_DIAMETER:
                    gw.vy = 0
                    gw.moving = False
                    gw.failcounter += 1
                    gw.remove(gw.ball)
                    if gw.failcounter < N_BALLS:
                        gw.ball = GOval(GWINDOW_WIDTH / 2 - BALL_DIAMETER / 2, GWINDOW_HEIGHT / 2, BALL_DIAMETER, BALL_DIAMETER)
                        gw.ball.set_color("Black")
                        gw.ball.set_filled(True)
                        gw.add(gw.ball)
                get_colliding_object()
                gw.pause(TIME_STEP)
        if gw.totalbricks == 0: #Sets win message
            winlabel = GLabel("You win!", 30, 300)
            winlabel.set_font("italic bold 80px 'times new roman'")
            gw.add(winlabel)
        if gw.failcounter == N_BALLS: #Sets lose message
            losslabel = GLabel("You lose :(", 0, 300)
            losslabel.set_font("italic bold 80px 'times new roman'")
            gw.add(losslabel)
    gw.add_event_listener("mousemove", mousemove)
    gw.add_event_listener("mousedown", mousedown)



# Startup code
if __name__ == "__main__":
    breakout()