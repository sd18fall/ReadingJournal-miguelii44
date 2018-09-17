import turtle
import math

# Create the world, and a turtle to put in it
t = turtle.Turtle()
# Get moving, turtle!
def square(t, length):  # for part 2 of 4.3, you will add another parameter to this function
    """Draw a square using Turtle t."""

    for i in range(4):
        t.fd(length)
        t.lt(90)

def leg(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0/n
    leg(t, n, length, angle)

def arch(t, r, angle):
    archlength = 2 * math.pi * r * abs(angle) / 360
    n = int(archlength/4) + 1
    steps = archlength / n
    angle = float(angle) / n
    t.lt(steps/2)
    leg(t, n, steps, angle)
    t.rt(angle/4)

def circle(t, r):
    arch(t, r, 360)

if __name__ == '__main__':
    bob = turtle.Turtle()
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)



# Wait for the user to close the window
turtle.mainloop()
