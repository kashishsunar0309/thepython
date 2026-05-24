import turtle
import math
import colorsys
import time

# --- Screen Setup ---
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Tara & Kalam")

# --- Heart Turtle ---
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.colormode(1)

# --- Heart Function ---
def heart(t_param, scale=15):
    x = 16 * (math.sin(t_param)) ** 3
    y = (13 * math.cos(t_param)
         - 5 * math.cos(2 * t_param)
         - 2 * math.cos(3 * t_param)
         - math.cos(4 * t_param))
    return x * scale, y * scale

# --- Draw Heart ---
points = []
steps = 200

for i in range(steps):
    t_param = i * (2 * math.pi / steps)
    points.append(heart(t_param))

h = 0.0

for (x, y) in points:
    t.penup()
    t.goto(0, 0)
    t.pendown()
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    h += 0.01
    t.goto(x, y)
    t.penup()
    t.goto(x, y)
    t.dot(10)

# --- Slow Motion Name Writer (whole word at once, no splitting) ---
def write_slow_motion(text, x, y, color):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.speed(1)
    writer.color(color)

    # write each character one by one using screen font trick
    current_x = x
    for char in text:
        writer.goto(current_x, y)
        writer.write(char, font=("Comic Sans MS", 30, "bold"))
        # Comic Sans MS gives human handwritten feel
        # measure char width precisely to avoid gaps
        if char in ('i', 'l', 'I', '1', 'j'):
            current_x += 18   # narrow letters
        elif char in ('m', 'w', 'W', 'M'):
            current_x += 38   # wide letters
        else:
            current_x += 28   # normal letters
        time.sleep(0.3)       # pause between each letter = slow motion feel
        screen.update()

# --- Write "Tara" on top left ---
write_slow_motion("MOTHER", -160, 240, "red")

# --- Write "Kalam" on top right ---
write_slow_motion("FATHER", 55, 240, "red")

turtle.done()