import turtle
import math

#Setup
wn = turtle.Screen()
wn.title("Niels Bohr")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Nucleus
nucleus = turtle.Turtle()
nucleus.speed(0)
nucleus.shape("circle")
nucleus.color("red")
nucleus.shapesize(stretch_len=1.75, stretch_wid=1.75)
nucleus.penup()
nucleus.goto(0,0)

#Electrons
class Electrons:
   
    def __init__(self, x, y):
        self.i = 2
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color("#348ceb")
        self.turtle.setx(x)
        self.turtle.sety(y)
        self.turtle.pendown()
        self.turtle.pensize(1)
        self.turtle.pencolor("white")
        self.turtle.speed(1)    

    def move_bg(self):
        self.turtle.forward(4)
        self.turtle.left(1)

    def move(self):
        self.turtle.forward(2)
        self.turtle.left(1)
   
    def move_op(self):
        self.turtle.left(1)
        self.turtle.backward(2)

    def electron_energy(self):
        self.i = 1

    def electron_energy_rv(self):
        self.i = 2

# Electron Defining
electron1 = Electrons(0, -110)
electron2 = Electrons(0, 110)

electron3 = Electrons(0, -220)
electron3.turtle.shapesize(stretch_len=1.5,stretch_wid=1.5)
electron3.turtle.color("#3452eb")

#Keyboard Binding
wn.listen()
wn.onkeypress(electron3.electron_energy, "w")
wn.onkeypress(electron3.electron_energy_rv, "s")

#Main Animation Loop
while True:
    wn.update()
    electron2.move_op()
    electron3.move_bg()
    if electron3.i > 1:
        electron1.turtle.showturtle()
        electron3.turtle.hideturtle()
        electron3.move_bg()
        electron1.move()
    elif electron3.i == 1:
        electron3.turtle.showturtle()
        electron1.turtle.hideturtle()
        electron1.move()
        electron3.move_bg()
