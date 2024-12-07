
import turtle
import time
import random
from PIL import Image

# Open the JPG image
img = Image.open(r"C:\Users\asus\Downloads\game\b1.jpg")

# Convert and save it as a GIF
img.save(r"C:\Users\asus\Downloads\game\b1.gif", "GIF")

# Game configuration
delay = 0.1
score = 0
high_score = 0

# Screen setup
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.bgpic(r"C:\Users\asus\Downloads\game\b1.gif")  # Set background image (GIF)
 # Set background image (JPG)
window.setup(width=600, height=600)
window.tracer(0)  # Turns off automatic screen updates

# Snake head using a default shape (square)
head = turtle.Turtle()
head.shape("square")  # Use default shape for snake head
head.color("green")  # Optional: color the snake head
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake body segments with default shape
segments = []

# Food using a custom image (food image is JPG, but not used as a shape)
food = turtle.Turtle()
food.speed(0)
food.shape("circle")  # Use default square shape for food (can’t use JPG directly as a shape)
food.color("red")  # Optional: color the food
food.penup()
food.goto(0, 100)

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to control the snake's movement
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings for arrow keys
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Main game loop
while True:
    window.update()

    # Check for collision with border (walls)
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Reset segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = 0.1
        score_display.clear()
        score_display.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")  # Default body shape (square)
        new_segment.color("lightblue")  # Attractive color for snake body
        new_segment.penup()
        segments.append(new_segment)

        # Increase score
        score += 10
        if score > high_score:
            high_score = score

        delay -= 0.001  # Increase game speed
        score_display.clear()
        score_display.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Move the segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to head position
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            score_display.clear()
            score_display.write(
                f"Score: {score}  High Score: {high_score}",
                align="center",
                font=("Courier", 24, "normal"),
            )

    time.sleep(delay)

window.mainloop()

