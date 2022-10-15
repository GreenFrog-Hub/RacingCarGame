from turtle import circle
import pyglet as pyg
import math
import time
import movement
import crashDetection
import car
import trackCreate
import walls

x = 185.0
y = 432.0
rotate = 0.0
xSpeed = 0.0
ySpeed = 0.0
friction = 1.08
velocity = 0.0
steer = 0.0
display = pyg.canvas.Display()
screen = display.get_default_screen()
screen_width = screen.width
screen_height = screen.height

modifyerScaleX = screen_width / 1920
modifyerScaleY = screen_height / 1080
x = x * modifyerScaleX
y = y * modifyerScaleY 



raceTrack = trackCreate.track(screen_width, screen_height, modifyerScaleX, modifyerScaleY)
track = raceTrack.loadTrack()

trackWalls = walls.walls(screen_width, screen_height, modifyerScaleX, modifyerScaleY)
pitch, pixels = trackWalls.loacteWalls()

window = pyg.window.Window(screen.width,screen.height, fullscreen = True)
track.blit(0,0)


preCar = car.carBuild(screen_width, screen_height, modifyerScaleX, modifyerScaleY)
car = preCar.sprite()





keysPressed = []
@window.event
def on_key_press(symbol, modifiers):
    keysPressed.append(symbol)
@window.event
def on_key_release(symbol, modifiers):
    if symbol in keysPressed:
        keysPressed.remove(symbol)

@window.event
def draw(dt):
    global x
    global y
    global rotate
    global xSpeed
    global ySpeed
    global friction
    global velocity
    global steer
    
    window.clear()
    track.blit(0,0)
    player = pyg.sprite.Sprite(car, x , y, subpixel= True)
    player.rotation = math.degrees(rotate)
    player.draw()
    crash = crashDetection.crash(x, y, rotate, xSpeed, ySpeed, pitch, pixels, modifyerScaleX, modifyerScaleY, velocity, steer)
    x, y, rotate, velocity, xSpeed, ySpeed, steer, reset= crash.crashCheck()
    if reset == True or reset == True: 
        player.draw()
        reset = False
        time.sleep(0.75)
    move = movement.movement(dt, x, y, rotate, keysPressed,modifyerScaleX, modifyerScaleY, friction, velocity, xSpeed, ySpeed, steer)
    x, y, rotate, velocity, xSpeed, ySpeed, steer, reset = move.keys()
    player.draw()
    
    

    

pyg.clock.schedule_interval(draw, 1/60)
pyg.app.run()
