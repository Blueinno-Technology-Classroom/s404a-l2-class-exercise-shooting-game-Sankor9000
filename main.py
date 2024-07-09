import pgzrun
import random

WIDTH = 720
HEIGHT = 480

target1 = Actor("target_red1")
target1.right = WIDTH
target1.bottom = HEIGHT
target1.top = 0
target1.left = 0

duck2 = Actor("duck_brown")
duck2.right = WIDTH
duck2.bottom = HEIGHT
duck2.top = 0
duck2.left = 0

cursor = Actor("crosshair_outline_small")
rifle = Actor("rifle")

score = 0

def update():
    target1.x += 5
    if target1.left >= WIDTH:
        target1.right = 0
    duck2.x += 5
    if duck2.left >= WIDTH:
        duck2.right = 0

def on_mouse_move(pos):
    cursor.pos = pos
    rifle.left = pos [0]
    rifle.top = pos [1]

def on_mouse_down(pos):
    global score
    if cursor.colliderect(target1):
        target1.right = 0
        target1.y = random.randint(0, HEIGHT)
        score += 5
    elif cursor.colliderect(duck2):
        duck2.right = 0
        duck2.y = random.randint(0, HEIGHT)
        score += 5
        

def draw():
    screen.clear()
    target1.draw()
    duck2.draw()
    cursor.draw()
    rifle.draw()
    screen.draw.text(str(score), (10,10), fontsize=50, color='blue')


pgzrun.go()