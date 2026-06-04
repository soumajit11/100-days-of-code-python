import turtle as t
import random as rd

tim = t.Turtle()
tim.shape("turtle")
tim.color("DarkBlue")
# for _ in range(4):
#     tim.fd(100)
#     tim.right(90)

# for _ in range(10):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.fd(50)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     tim.color(rd.choice(colours))
#     draw_shape(shape_side_n)

# directions = [0, 90, 180, 270]
# tim.pensize(10)
tim.speed("fastest")

t.colormode(255)

def random_colour():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    colour = (r, g, b)
    return colour

# for _ in range(200):
#     tim.color(random_colour())
#     tim.fd(25)
#     tim.setheading(rd.choice(directions))

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap )

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()