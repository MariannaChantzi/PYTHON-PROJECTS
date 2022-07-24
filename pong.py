# Pong Game

import turtle
import winsound

def pong_game(player_left, player_right, points_to_win, dif_lvl, dif_incr):

    # Screen
    wn = turtle.Screen()
    wn.title("Pong game!")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Left Paddle
    paddle_left = turtle.Turtle()
    paddle_left.speed(0)
    paddle_left.shape("square")
    paddle_left.color("white")
    paddle_left.shapesize(stretch_wid = 5, stretch_len = 1)
    paddle_left.penup()
    paddle_left.goto(-350,0)

    # Right Paddle
    paddle_right = turtle.Turtle()
    paddle_right.speed(0)
    paddle_right.shape("square")
    paddle_right.color("white")
    paddle_right.shapesize(stretch_wid = 5, stretch_len = 1)
    paddle_right.penup()
    paddle_right.goto(350,0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)

    # difficulty level increase if another round is played
    ball.dx = 0.8 + dif_incr
    ball.dy = 0.8 + dif_incr

    # Pen 1
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Player {}: 0  Player {}: 0".format(player_left,player_right), align = "center", font = ('Courier', 24, "normal"))

    #Pen 2
    pen2 = turtle.Turtle()
    pen2.speed(0)
    pen2.color("white")
    pen2.penup()
    pen2.hideturtle()
    pen2.goto(-320, 240)
    pen2.write("Difficulty level: {}".format(dif_lvl), align = "center", font = ('Courier', 10, "normal"))

    # Scores
    score_player_left = 0
    score_player_right = 0

    # Functions
    def paddle_left_up():
        y = paddle_left.ycor()
        y += 20
        paddle_left.sety(y)

    def paddle_left_down():
        y = paddle_left.ycor()
        y -= 20
        paddle_left.sety(y)

    def paddle_right_up():
        y = paddle_right.ycor()
        y += 20
        paddle_right.sety(y)

    def paddle_right_down():
        y = paddle_right.ycor()
        y -= 20
        paddle_right.sety(y)

    # Keyboard Binding
    wn.listen()
    wn.onkeypress(paddle_left_up, "w")
    wn.onkeypress(paddle_left_down, "s")
    wn.onkeypress(paddle_right_up, "Up")
    wn.onkeypress(paddle_right_down, "Down")

    # Main Game Loop
    while True:
        wn.update()

        # Ball Movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            score_player_left += 1
            pen.clear()
            pen.write("Player {}: {}  Player {}: {}".format(player_left,score_player_left,player_right,score_player_right), align = "center", font = ('Courier', 24, "normal"))


        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            score_player_right += 1
            pen.clear()
            pen.write("Player {}: {}  Player {}: {}".format(player_left,score_player_left,player_right,score_player_right), align = "center", font = ('Courier', 24, "normal"))

        # Paddle-Ball Collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and ((ball.ycor() < paddle_right.ycor() + 40) and (ball.ycor() > paddle_right.ycor() - 40)):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and ((ball.ycor() < paddle_left.ycor() + 40) and (ball.ycor() > paddle_left.ycor() - 40)):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if score_player_left == points_to_win or score_player_right == points_to_win:
            break

    # Final Screen Message
    wn.clear()
    wn.bgcolor("black")
    wn.tracer(0)

    pen.goto(0,100)
    if score_player_left < score_player_right:
        pen.write("Player {} has won!!!".format(player_right), align = "center", font = ('Courier', 24, "normal"))
    else:
        pen.write("Player {} has won!!!".format(player_left), align = "center", font = ('Courier', 24, "normal"))

    while True:
        answer = wn.textinput("Play another round?", "Type quit or continue")
        if answer.lower().startswith('q'):
            quit()
        elif answer.lower().startswith('c'):
            wn.clear()
            dif_lvl = dif_lvl + 1
            dif_incr = dif_incr + 0.2
            pong_game(player_left, player_right, points_to_win, dif_lvl, dif_incr)
        else:
            wn.textinput("Wrong input!", "Type quit or continue")
            continue


# First Screen
wn = turtle.Screen()
wn.title("Pong game!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

player_left = wn.textinput("Player A", "Insert name")
if player_left == '':
    player_left = 'A'
player_right = wn.textinput("Player B", "Insert name")
if player_right == '':
    player_right = 'B'
points_to_win = wn.textinput("Points to win", "Insert number")
if points_to_win == '':
    points_to_win = '2'
points_to_win = int(points_to_win)

dif_lvl = 1
dif_incr = 0
pong_game(player_left, player_right, points_to_win, dif_lvl, dif_incr)
