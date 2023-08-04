from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")

#Tracer: Draws the different portion of the game without showing the animation
screen.tracer(0) 

#Create a snake
snake = Snake()
#create food
food = Food()
#create scoreboard object
board = Scoreboard()

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
    
    #Detect collision with food using distance method
    if snake.head.distance(food) < 15:
        board.update_score()
        snake.extend()
        food.refresh()
    
    #Detect collision with wall 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        board.reset()
        snake.reset_snake()
    
    #Detect collision with tail
    #if head collides with any segment in the tail then trigger game over sequence
    for seg in snake.body[1:]:
        if snake.head.distance(seg) < 10: 
            board.reset()
            snake.reset_snake()


screen.exitonclick()

