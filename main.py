from turtle import Turtle, Screen
import turtle as t
import random
#import colorgram

timmy = Turtle()
screen = Screen()

t.colormode(255)
timmy.speed(10)

###How to extract a color tuple from an image:

# colors = colorgram.extract("image.jpg", 444)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#print(rgb_colors)

color_list = [(183, 162, 134), (125, 92, 73), (81, 93, 115), (148, 161, 179), (177, 153, 162), (208, 206, 140), (29, 35, 48), (117, 83, 95), (52, 24, 32), (148, 168, 154), (47, 26, 20), (85, 105, 90), (157, 152, 69), (105, 37, 49), (24, 33, 30), (50, 58, 91), (163, 110, 102), (210, 180, 190), (112, 40, 33), (156, 110, 120), (111, 123, 152), (215, 181, 175), (182, 188, 207), (108, 142, 114), (176, 201, 187), (70, 71, 38), (103, 137, 145), (54, 69, 60), (165, 201, 211), (42, 74, 76), (205, 211, 39)]


timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


#timmy.width(10)

# def draw_circle(x, y):
#     for _ in range(15):
#         timmy.color(random.choice(color_list))
#         timmy.penup()
#         timmy.goto(x, y)
#         x += 50
#         timmy.pendown()
#         timmy.circle(5)
#

# draw_circle(-350, -300)
# draw_circle(-350, -250)
# draw_circle(-350, -200)
# draw_circle(-350, -150)
# draw_circle(-350, -100)
# draw_circle(-350, -50)
# draw_circle(-350, 0)
# draw_circle(-350, 50)
# draw_circle(-350, 100)
# draw_circle(-350, 150)
# draw_circle(-350, 200)
# draw_circle(-350, 250)
# draw_circle(-350, 300)


screen.exitonclick()
