from turtle import Turtle, Screen
import time 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = list()
        self.fill_segments()
        self.head = self.body[0]

    #function used to intit body :
    #list of body parts 
    def fill_segments(self):
        for i in range(3):
            new_turtle = Turtle(shape = "square")
            new_turtle.fillcolor("white")
            new_turtle.penup()
            new_turtle.goto(i*-20,0)
            self.body.append(new_turtle)

    #function used to move the body uses the init list
    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)

        self.body[0].forward(MOVE_DISTANCE)
    
    def up(self):
        #Don't want movement backwards
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)