'''
1.0 Jedi Training (17pts)  Name: Caleb Little


1. Define Forking (1pt): 
Creating a copy of a repo to your own remote repo
2. Define Cloning (1pt): 
'downloading' the remote repo onto your local device
3. Define Branching (1pt):
making a copy of code you are working that you can test away from the main file
4. Define Committing (1pt): 
creating a hard save of your code that you can revert to in the future
5. Define Merging (1pt): 
Overwriting your main file with the code written in your test branches
6. Define Pushing (1pt):
Uploading your updated local repo to the remote repo
7. Define Pull Request (1pt):
A pull request asks the owner of the organization to review your code and potentially merge it back into the upstream remot repo

8. TUTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''


import turtle

tina = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("black")

tina.speed(13)

tina.color('#cecee2')
tina.begin_fill()
tina.pu()
tina.goto(0, -150)
tina.pd()
tina.circle(150)
tina.end_fill()
tina.pu()
tina.color('#13135a')
tina.goto(0, -135)
tina.begin_fill()
tina.pd()
tina.circle(135)
tina.end_fill()

tina.color('#070741')
tina.pu()
tina.goto(0, -90)
tina.begin_fill()
tina.pd()
tina.circle(30)
tina.end_fill()

tina.pu()
tina.goto(50, -45)
tina.begin_fill()
tina.pd()
tina.circle(30)
tina.end_fill()

tina.pu()
tina.goto(-50, -45)
tina.begin_fill()
tina.pd()
tina.circle(30)
tina.end_fill()

tina.color("silver")
tina.pu()
tina.goto(0, -15)
tina.begin_fill()
tina.pd()
tina.circle(15)
tina.end_fill()
tina.pu()


# hour marks
def tick(x=0.0, y=0.0):
    tina.pu()
    tina.goto(x, y)
    tina.begin_fill()
    tina.pd()
    tina.fd(5)
    tina.rt(90)
    tina.fd(30)
    tina.rt(90)
    tina.fd(5)
    tina.rt(90)
    tina.fd(30)
    tina.lt(60)
    tina.end_fill()


tina.color('#d8ede6')
tick(0, 130)
tick(43.3, 86.6)
tina.rt(180)
tick(86.6, 43.3)
tick(130, 0)

tick(86.6, -43.3)
tina.rt(180)
tick(43.3, -86.6)
tick(0, -130)

tick(-43.3, -86.6)
tina.rt(180)
tick(-86.6, -43.3)
tick(-130, 0)

tick(-86.6, 43.3)
tina.rt(180)
tick(-43.3, 86.6)

# second hand
tina.pu()
tina.goto(0, -10)
tina.pensize(5)
tina.pd()
tina.circle(10)
tina.pensize(1)
tina.pu()
tina.goto(0, 0)
tina.begin_fill()
tina.color('#cecee2')
tina.pd()
tina.rt(34)
tina.lt(45)
tina.fd(120)
tina.lt(90)
tina.fd(2)
tina.lt(90)
tina.fd(120)
tina.lt(90)
tina.fd(2)
tina.end_fill()
tina.pu()

# minute hand
tina.goto(0, 0)
tina.begin_fill()
tina.pd()
tina.rt(60)
tina.rt(45)
tina.fd(10)
tina.lt(45)
tina.fd(80)
tina.lt(45)
tina.fd(10)
tina.rt(45)
tina.fd(25)
tina.rt(180)
tina.fd(25)
tina.rt(45)
tina.fd(10)
tina.lt(45)
tina.fd(80)
tina.lt(45)
tina.fd(10)
tina.end_fill()
tina.pu()

tina.lt(135)
tina.fd(5)
tina.color("white")
tina.begin_fill()
tina.pd()
tina.rt(90)
tina.fd(3)
tina.lt(90)
tina.fd(75)
tina.lt(90)
tina.fd(6)
tina.lt(90)
tina.fd(75)
tina.lt(90)
tina.fd(6)
tina.end_fill()
tina.pu()

# hour hand
tina.goto(0, 0)
tina.color('#cecee2')
tina.begin_fill()
tina.pd()
tina.rt(180)
tina.rt(45)
tina.fd(8)
tina.lt(45)
tina.fd(60)
tina.lt(45)
tina.fd(8)
tina.rt(45)
tina.fd(18)
tina.rt(180)
tina.fd(18)
tina.rt(45)
tina.fd(8)
tina.lt(45)
tina.fd(60)
tina.lt(45)
tina.fd(8)
tina.end_fill()
tina.pu()

tina.lt(135)
tina.fd(5)
tina.color("white")
tina.begin_fill()
tina.pd()
tina.rt(90)
tina.fd(2)
tina.lt(90)
tina.fd(50)
tina.lt(90)
tina.fd(4)
tina.lt(90)
tina.fd(50)
tina.lt(90)
tina.fd(4)
tina.end_fill()
tina.pu()

tina.rt(130)
tina.goto(-175, -200)
tina.write("Caleb Little", font=("Arial", 20, "normal"))
tina.ht()
turtle.exitonclick()
