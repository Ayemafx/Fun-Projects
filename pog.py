import turtle #lets u do graphics
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #speed up our game a bit

# Score A
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() #T for class name
paddle_a.speed(0) #sets the speed to max possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle() #T for class name
paddle_b.speed(0) #sets the speed to max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle() #T for class name
ball.speed(0) #sets the speed to max possible speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
penn = turtle.Turtle()
penn.speed(0)
penn.color("red")
penn.penup()
penn.hideturtle()
penn.goto(0, 260)
penn.write("Player A: 0, Player B:0", align="center", font=("Courier", 18, "normal"))

#Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    minus_y = paddle_a.ycor()
    minus_y += -20
    paddle_a.sety(minus_y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    minus_y = paddle_b.ycor()
    minus_y += -20
    paddle_b.sety(minus_y)


#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Boder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        penn.clear()
        penn.write("Player A: {}, Player B:{}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        penn.clear()
        penn.write("Player A: {}, Player B:{}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1