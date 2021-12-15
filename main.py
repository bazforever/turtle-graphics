
import turtle

from math import cos, sin
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")
mySpirograph = turtle.Turtle()
mySpirograph.hideturtle()
mySpirograph.speed(0)
mySpirograph.pensize(2)
myPen = turtle.Turtle()
myPen.speed(0)
myPen.pensize(3)
myPen.color("#FFFF55")
R = 125
r = 75
d = 125
angle = 0
myPen.penup()
myPen.goto(R - r+d, 0)
myPen.pendown()
theta = 0.2
steps = int(6*3.14/theta)
for t in range(0, steps):
    mySpirograph.clear()













































































