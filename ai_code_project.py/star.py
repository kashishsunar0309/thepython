import turtle
import math

def draw_star_with_corner_symbols(size, signature="KASHISH"):
    t = turtle.Turtle()
    t.speed(3)
    t.color("black")

    # Calculate the 5 star tip positions
    cx, cy = 0, 0
    corners = []
    for i in range(5):
        angle = math.radians(90 + i * 72)
        x = cx + size * math.cos(angle)
        y = cy + size * math.sin(angle)
        corners.append((x, y))

    # Draw the star
    order = [0, 2, 4, 1, 3, 0]
    t.penup()
    t.goto(corners[order[0]])
    t.pendown()
    for i in order[1:]:
        t.goto(corners[i])

    # ── Equal size for ALL symbols and name ───────────────
    sym_font_size = int(size / 10)   # one size used everywhere

    # Symbols at corners (cyan)
    symbols = ["π", "√", "Δ", "∞", "Σ"]
    offset = size * 0.12

    t.color("cyan")
    for i, (pos, sym) in enumerate(zip(corners, symbols)):
        angle = math.radians(90 + i * 72)
        ox = pos[0] + offset * math.cos(angle)
        oy = pos[1] + offset * math.sin(angle)
        t.penup()
        t.goto(ox, oy)
        t.write(sym, align="center", font=("Arial", sym_font_size, "bold"))

    # ── Name in the CENTER (same font size as symbols) ────
    t.color("gold")
    t.penup()
    t.goto(0, -(sym_font_size // 2))   # vertically centered
    t.write(signature, align="center", font=("Arial", sym_font_size, "bold"))

    turtle.done()

draw_star_with_corner_symbols(200, signature="Kashish")