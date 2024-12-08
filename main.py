import pgzrun
from random import randint

TITLE="Alien Game"

WIDTH=500
HEIGHT=500

message=""

alien=Actor('Alien')

def draw():
    screen.clear()
    screen.fill(color=(0,128,0))
    alien.draw()
    screen.draw.text(message, center=(400, 10), fontsize=30)

def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, WIDTH-50) 

def on_mouse_down(pos):
    #print("Hello World")
    global message
    if alien.collidepoint(pos):
        message= "Good Shot!"
        place
    else:
        message= "You missed"




place_alien()
pgzrun.go()