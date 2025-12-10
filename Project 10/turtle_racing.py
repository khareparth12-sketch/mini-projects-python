import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'skyblue', 'lightgreen', 'pink', 'yellow', 'brown', 'black', 'purple', 'coral', 'cornsilk']

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race!")

def get_number_of_racers():
    racers = 0
    while True:
        print("How many Turtles will participate in the race?")
        racers = input()
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Not a numeric value... Try Again!!!")
            continue

        if 2<=racers<=10:
            return racers
        else:
            print("Number of participants can be from 2-10 only.")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH//(len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT//2-10:
                return colors[turtles.index(racer)]

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"Congrats {winner} Turtle! You Win!")
time.sleep(5)