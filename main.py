from turtle import Turtle, Screen
import random

# t = Turtle(shape="turtle")
s = Screen()

"""Eveent listen methods of turtle practical"""
# def move_forward():
#     t.forward(10)

# def move_backward():
#     t.backward(10)

# def counter_clock():
#     t.left(10)
#     # move_forward()
#     # move_backward()

# def anti_counter_clock():
#     t.right(10)
#     # move_forward()
#     # move_backward()

# def cls_scr():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()

# s.listen()
# s.onkey(key = 'w', fun=move_forward)
# s.onkey(key = 's', fun=move_backward)
# s.onkey(key = 'a', fun=counter_clock)
# s.onkey(key = 'd', fun=anti_counter_clock)
# s.onkey(key = 'c', fun=cls_scr)

"""Turtle race using differetn methods"""
is_race_on = False
s.setup(width = 500, height = 400)
user_bet = s.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "orange", "purple", "blue", "black"]
directions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=directions[index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You have won.The winning color is {winning_turtle}.")
            else:
                print(f"You have lost.The winning color is {winning_turtle}.")
        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance) 

s.exitonclick()


