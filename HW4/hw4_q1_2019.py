"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2019
hw4_q1_2019.py - Recursice fern with turtle
"""

import turtle

pen = turtle.Turtle()
mywin = turtle.Screen()
pen.color('blue')
pen.width(3)


""""
Tree code is only in this file for reference.
It is not needed fr solving the assignment!!!
"""

def tree(n,l):
    if n==0 or l<2:
        return
    pen.forward(l)
    pen.left(45)
    tree(n-1, l/2)
    pen.right(90)
    tree(n-1, l/2)
    pen.left(45)
    pen.backward(l)

#tree(30,100)
# mywin.exitonclick()

def fern(n,l):
    if n==0 or l<2:
        return

    pen.left(5) # slight curve

    pen.forward(l / 3) # moves 1/3 distance 'l'
    pen.left(45) # left branch foundation - set direction
    fern(n-1, l/3) # recursion, reducing arguments 'n' and 'l' in order to eventually end recursion loop

    pen.right(45) # back to "straight" position
    pen.forward(l / 3)
    pen.right(45) # right branch foundation - set direction
    fern(n - 1, l / 3) # recursion, reducing arguments 'n' and 'l' in order to eventually end recursion loop

    pen.left(45) # back to "straight" position
    fern(n - 1,l)

    pen.backward(l * 2 / 3)
    pen.right(5) # reset pen direction position

fern(5,100)
mywin.exitonclick()
