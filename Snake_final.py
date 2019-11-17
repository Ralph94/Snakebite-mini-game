import turtle

import time

import random

import winsound

delay = 0.1


# score

score = 0

high_score = 0

# set up screen

wn = turtle.Screen()

wn.title("Snakebite mini game by Rafa94")

wn.bgpic("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/sand2.gif")

wn.bgcolor("tan")

wn.setup(width=600, height=600)

wn.tracer(0)
# Adding images
wn.register_shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/snake2.gif")
wn.register_shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/snake_right.gif")
wn.register_shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/snake_up.gif")
wn.register_shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/snake_down.gif")
wn.register_shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/mice2.gif")
wn.register_shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/mice.gif")
wn.register_shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/mice3.gif")

# snake head

head = turtle.Turtle()

head.speed(0)

head.shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/snake2.gif")

head.color("black")

head.penup()

head.goto(0, 0)

head.direction = "stop"

# obstacle

obstacle = turtle.Turtle()

obstacle.speed(0)

obstacle.shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/mice2.gif")

obstacle.color("red")

obstacle.penup()

obstacle.goto(1000, 1000)

# snake food

food = turtle.Turtle()

food.speed(0)

food.shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/mice.gif")

food.color("yellow", "orange")

food.penup()

food.goto(0, 100)



food2 = turtle.Turtle()

food2.speed(0)

food2.shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/mice3.gif")

food2.color("yellow", "black")

food2.penup()

food2.goto(0, -150)



segments = []

# pen
pen = turtle.Turtle()

pen.speed(0)

pen.shape("square")

pen.color("black")

pen.penup()

pen.ht()

pen.goto(0, 260)

pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 20, "normal"))



# functions

def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/snake_up.gif")


def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/snake_down.gif")


def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/snake2.gif")


def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.shape("C:/Users/Rafael Perez/PycharmProjects/snake_game/venv/snake_right.gif")


def move():
    if head.direction == "up":
        y = head.ycor()

        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()

        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()

        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()

        head.setx(x + 20)


# keyboard bindings

wn.listen()

wn.onkeypress(go_up, "Up")

wn.onkeypress(go_down, "Down")

wn.onkeypress(go_left, "Left")

wn.onkeypress(go_right, "Right")

# main game loop

while True:

    wn.update()
    winsound.PlaySound("C:/Users/Rafael Perez/PycharmProjects/snake_gamevenv/bite_sound.wav", winsound.SND_ASYNC)



    # check for collision with border and snake

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:

        time.sleep(0.5)

        head.goto(0, 0)

        head.direction = "stop"




        # hide segments

        for segment in segments:
            segment.goto(1000, 1000)

        # clear segments list

        segments.clear()

        # reset score

        score = 0

        # reset delay

        delay = 0.1

        # update the score display

        pen.clear()

        pen.write("Score: {}  High Score {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))


    # check for a collision with the food and snake

    if head.distance(food) < 15:# Basically saying if our snake head distance to our food is greater then 20
        # Move food to random spot on screen

        x = random.randint(-290, 290)

        y = random.randint(-290, 290)

        food.goto(x, y)# Move to xcor and ycor side of the screen
        winsound.PlaySound("C:/Users/Rafael Perez/PycharmProjects/snake_gamevenv/bite_sound.wav", winsound.SND_ASYNC)
        # Shorten the delay

        delay -= 0.001

        # Increase the score

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()

        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

        # add segment 2

        new_segment = turtle.Turtle()

        new_segment.speed(0)

        new_segment.shape("square")

        new_segment.color("black")

        new_segment.penup()

        segments.append(new_segment)




    if head.distance(food2) < 15:  # Basically saying if our snake head distance to our food is greater then 20

        # Move food to random spot on screen

        x = random.randint(-290, 290)

        y = random.randint(-290, 290)

        food2.goto(x, y)  # Move to xcor and ycor side of the screen
        winsound.PlaySound("C:/Users/Rafael Perez/PycharmProjects/snake_gamevenv/bite_sound.wav", winsound.SND_ASYNC)
        # Shorten the delay

        delay -= 0.001

        # Increase the score

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))



        # add segment

        new_segment = turtle.Turtle()

        new_segment.speed(0)

        new_segment.shape("square")

        new_segment.color("black")

        new_segment.penup()

        segments.append(new_segment)



        # spawn obstacle and make it move

        def follow_head():

            obstacle.setheading(obstacle.towards(head))

            if score > 200:
                obstacle.forward(0.5)

                wn.ontimer(follow_head, 20)


        if score >= 100:# Once your score 100 points an enemy will appear!

            obstacle.goto(head.xcor() + 100, head.ycor() - 100)#Will either appear on the left or right side of the screen

        else:

            obstacle.goto(1000, 1000)

        if score >= 200:
            follow_head()

    if head.distance(obstacle) < 20:

        time.sleep(0.5)

        head.goto(0, 0)

        head.direction = "stop"

        # hide segments

        for segment in segments:
            segment.goto(1000, 1000)

        # clear segments list

        segments.clear()

        # reset score

        score = 0

        # reset delay

        delay = 0.1

        # update the score display

        pen.clear()# Using pur .clear function so the score board wont write over its self

        pen.write("Score: {}  High Score {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

    # move end segments with head

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()

        y = segments[index - 1].ycor()

        segments[index].goto(x, y)

    # move segment 0 to where the head is

    if len(segments) > 0:
        x = head.xcor()

        y = head.ycor()

        segments[0].goto(x, y)

    move()

    # check for head collision with body

    for segment in segments:

        if segment.distance(head) < 20:

            time.sleep(0.5)

            head.goto(0, 0)

            head.direction = "stop"

            # hide segments

            for segment in segments:
                segment.goto(1000, 1000)

            # clear segments list

            segments.clear()

            # reset score

            score = 0

            # reset delay

            delay = 0.1

            # update the score display

            pen.clear()

            pen.write("Score: {}  High Score {}".format(score, high_score), align="center",font=("Courier", 20, "normal"))



    time.sleep(delay)


wn.mainloop()