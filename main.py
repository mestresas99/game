import turtle

# Create and customise the screen
window = turtle.Screen()
window.screensize(canvwidth=400, canvheight=400)
window.bgcolor('black')
window.tracer(0)

# Create and customise the turtle
player = turtle.Turtle()
player.shape('turtle')
player.shapesize(1)
player.color('red')
player.penup()

# Create enemies
enemy = turtle.Turtle()
enemy.shape('circle')
enemy.shapesize(1)
enemy.color('white')
enemy.setposition(60.00,30.00)

# Define the functions to make the turtle movements
def turn_left():
  player.left(10)
  
def turn_right():
  player.right(10)

def forward():
  player.forward(10)

def back():
  player.backward(10)
  
# Create the key bindings
window.listen()

# Scores and puntuation
score = 0

# Main loop which makes the turtle move
while True:
  print(player.pos())
  print(score)
  if player.position() == enemy.position():
    score = score + 10

  if window.onkeypress(turn_left, "Left"):
      turn_left()
  if window.onkeypress(turn_right, "Right"):
      turn_right
  if window.onkeypress(forward, "Up"):
      forward
  if window.onkeypress(back, "Down"):
      back
  window.update()
  
# turtle.done() This line is no longer needed now there's a while True loop