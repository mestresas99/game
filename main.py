import turtle

# Create and customise the screen
window = turtle.Screen()
window.bgcolor('black')
window.tracer(0)

# Create and customise the turtle
player = turtle.Turtle()
player.shape('turtle')
player.color('red')
player.penup()

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

# Main loop which makes the turtle move forward contiunously, forever
while True:
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