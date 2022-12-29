import math
import pyglet as pg
import time

class movement:
    def __init__(self, dt ,x, y, rotation, keysPressed,modX, modY, friction, velocity, xSpeed, ySpeed, steer):
        self.modX = modX
        self.modY = modY
        self.keysPressed = keysPressed
        self.dt = dt
        self.rotation = rotation
        self.steer = steer
        self.o = math.sin(self.rotation*math.pi/180)
        self.a = math.cos(self.rotation*math.pi/180)
        self.friction = friction
        self.velocity = velocity
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.x = x
        self.y = y
    

    def keys(self):
        self.xSpeed += self.velocity * math.sin(self.rotation)
        self.ySpeed += self.velocity * math.cos(self.rotation)
        self.rotation += (self.velocity/1.3 * self.steer)
        self.xSpeed = self.xSpeed / self.friction
        self.ySpeed = self.ySpeed / self.friction
        if self.velocity > 0:
            self.velocity = self.velocity / self.friction
        elif self.velocity <= 0:
            self.velocity = 0
        self.x += self.xSpeed
        self.y += self.ySpeed
        if pg.window.key.W in self.keysPressed:
            movement.forward(self)
            
        if pg.window.key.D in self.keysPressed and self.velocity > 0 and self.steer < 0.3:
            self.steer += 0.01
        elif pg.window.key.D in self.keysPressed and self.velocity > 0 and self.steer > 0.3:
            self.steer = 0.3

        if pg.window.key.A in self.keysPressed and self.velocity > 0 and self.steer > -0.3:
            self.steer -= 0.01
        elif pg.window.key.A in self.keysPressed and self.velocity > 0 and self.steer < -0.3:
            self.steer = -0.3

        if pg.window.key.D not in self.keysPressed and self.steer > 0.0:
            self.steer -= 0.01
        if pg.window.key.A not in self.keysPressed and self.steer < 0.0:
            self.steer += 0.01

        if pg.window.key.W not in self.keysPressed and self.velocity > 0:
            movement.slow(self)
        elif pg.window.key.S in self.keysPressed and self.velocity > 0:
            movement.handBreak(self)
        elif pg.window.key.R in self.keysPressed:
            movement.reset(self)
            return self.x, self.y, self.rotation, self.velocity, self.xSpeed, self.ySpeed, self.steer, True
        return self.x, self.y, self.rotation, self.velocity, self.xSpeed, self.ySpeed, self.steer, False

    def forward(self):
        self.velocity += 0.05

    def slow(self):
        if self.velocity > 0:
            self.velocity -= 0.05


    def handBreak(self):
        self.velocity = self.velocity / 10

    def reset(self):
        self.x = 185 * self.modX
        self.y = 432 * self.modY
        self.steer = 0
        self.velocity = 0
        self.xSpeed = 0
        self.ySpeed = 0
        self.rotation = 0
    
    def swap(self, HideTrack):
        self.HideTrack = HideTrack
        if pg.window.key.H in self.keysPressed and self.HideTrack == False:
            time.sleep(0.15)
            self.HideTrack = True
        elif pg.window.key.H in self.keysPressed and self.HideTrack == True:
            time.sleep(0.15)
            self.HideTrack = False
        
        return self.HideTrack
