from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")

#Tracer: Draws the different portion of the game without showing the animation
screen.tracer(0) 

#Create a snake
snake = Snake()

#listing for keystrokes 
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    #Moves all three segments foward 
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()

