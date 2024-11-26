import turtle
import time

# Create screen
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("black")
sc.setup(width=1000, height=600)
sc.tracer(0)

# Flag to control the game state
game_started = False

# Game Start Screen
def start_game_screen():
    global game_started

    # Display start screen
    sc.clear()
    sc.bgcolor("black")
    message = turtle.Turtle()
    message.color("white")
    message.penup()
    message.hideturtle()

    # Display "PONG" in large font
    message.goto(0, 50)
    message.write("PONG", align="center", font=("Courier", 50, "bold"))

    # Display instructions
    message.goto(0, -50)
    message.write("Press Space to Start", align="center", font=("Courier", 24, "normal"))

    # Function to start the game when space is pressed
    def start_game():
        global game_started
        game_started = True
        message.clear()

    sc.listen()
    sc.onkeypress(start_game, "space")

    # Wait until the player presses space to proceed
    while not game_started:
        sc.update()

start_game_screen()

# Midline divider
divider = turtle.Turtle()
divider.color("white")
divider.penup()
divider.hideturtle()
divider.goto(0, 300)
divider.setheading(270)
for _ in range(30):
    if _ % 2 == 0:
        divider.pendown()
    else:
        divider.penup()
    divider.forward(20)

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=1)
left_pad.penup()
left_pad.goto(-450, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=1)
right_pad.penup()
right_pad.goto(450, 0)

# Ball
hit_ball = turtle.Turtle()
hit_ball.speed(0)
hit_ball.shape("circle")
hit_ball.color("red")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 6  # Starting speed (higher for faster gameplay)
hit_ball.dy = 6

# Scores
left_player = 0
right_player = 0

# Score display
left_score_display = turtle.Turtle()
left_score_display.speed(0)
left_score_display.color("white")
left_score_display.penup()
left_score_display.hideturtle()
left_score_display.goto(-200, 250)
left_score_display.write("0", align="center", font=("Courier", 36, "bold"))

right_score_display = turtle.Turtle()
right_score_display.speed(0)
right_score_display.color("white")
right_score_display.penup()
right_score_display.hideturtle()
right_score_display.goto(200, 250)
right_score_display.write("0", align="center", font=("Courier", 36, "bold"))

# Functions to move paddles
def paddleaup():
    y = left_pad.ycor()
    if y < 250:
        y += 30
        left_pad.sety(y)


def paddleadown():
    y = left_pad.ycor()
    if y > -240:
        y -= 30
        left_pad.sety(y)


def paddlebup():
    y = right_pad.ycor()
    if y < 250:
        y += 30
        right_pad.sety(y)


def paddlebdown():
    y = right_pad.ycor()
    if y > -240:
        y -= 30
        right_pad.sety(y)


# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

# Update score
def update_score():
    left_score_display.clear()
    right_score_display.clear()
    left_score_display.write(f"{left_player}", align="center", font=("Courier", 36, "bold"))
    right_score_display.write(f"{right_player}", align="center", font=("Courier", 36, "bold"))

# Main game loop
while True:
    sc.update()
    time.sleep(0.01)

    # Move the ball
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Ball collision with top and bottom walls
    if hit_ball.ycor() > 290 or hit_ball.ycor() < -290:
        hit_ball.dy *= -1

    # Ball goes out of bounds (score update)
    if hit_ball.xcor() > 490:
        left_player += 1
        update_score()
        hit_ball.goto(0, 0)
        hit_ball.dx = -6  # Reset speed after scoring
        hit_ball.dy = 6

    if hit_ball.xcor() < -490:
        right_player += 1
        update_score()
        hit_ball.goto(0, 0)
        hit_ball.dx = 6  # Reset speed after scoring
        hit_ball.dy = 6

    # Ball collision with paddles
    if (440 > hit_ball.xcor() > 430) and (right_pad.ycor() - 60 < hit_ball.ycor() < right_pad.ycor() + 60):
        hit_ball.dx *= -1
        hit_ball.dx *= 1.1  # Increase ball speed after hit

    if (-440 < hit_ball.xcor() < -430) and (left_pad.ycor() - 60 < hit_ball.ycor() < left_pad.ycor() + 60):
        hit_ball.dx *= -1
        hit_ball.dx *= 1.1  # Increase ball speed after hit
