import turtle
import math
def draw_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        draw_edge(t, length, depth - 1)
        t.right(60)
        draw_edge(t, length, depth - 1)
        t.left(120)
        draw_edge(t, length, depth - 1)
        t.right(60)
        draw_edge(t, length, depth - 1)

def draw_polygon(t, num_sides, side_length, depth):
    angle = 360 / num_sides
    for _ in range(num_sides):
        draw_edge(t, side_length, depth)
        t.right(angle)

def main():
    num_sides = int(input("Enter number of sides (≥3): "))
    side_length = int(input("Enter side length (e.g. 200): "))
    depth = int(input("Enter recursion depth (0–6): "))

    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.color("cyan")

    t.penup()
    t.goto(-side_length // 2, side_length // 2)
    t.pendown()

    draw_polygon(t, num_sides, side_length, depth)

    turtle.done()

if __name__ == "__main__":
    main()
