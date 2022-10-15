import pyglet as pyg
import math



class crash:
    def __init__(self, x, y, rotation, xSpeed, ySpeed, pitch, pixels, modX, modY, velocity, steer):
        self.modX = modX
        self.modY = modY
        self.x = x
        self.y = y
        self.steer = steer
        self.velocity = velocity
        self.rotation = rotation
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.pitch = pitch
        self.pixels = pixels
        self.Px = self.x # x origin
        self.Py = self.y # y orgin
        self.xColl1 = (self.x + 10) * self.modX
        self.yColl1 = (self.y + 17) * self.modY
        
        self.xColl2 = (self.x - 10) * self.modX
        self.yColl2 = (self.y + 17) * self.modY

        self.xColl3 = (self.x + 10) * self.modX
        self.yColl3 = (self.y - 17) * self.modY

        self.xColl4 = (self.x - 10) * self.modX
        self.yColl4 = (self.y - 17) * self.modY

    def crashCheck(self):
        self.CollxTP1 = (self.xColl1 - self.Px)*math.cos(self.rotation) + (self.yColl1 - self.Py)* math.sin(self.rotation) + self.Px
        self.CollyTP1 = (self.Px - self.xColl1)*math.sin(self.rotation) + (self.yColl1 - self.Py)* math.cos(self.rotation) + self.Py

        self.CollxTP2 = (self.xColl2 - self.Px)*math.cos(self.rotation) + (self.yColl2 - self.Py)* math.sin(self.rotation) + self.Px
        self.CollyTP2 = (self.Px - self.xColl2)*math.sin(self.rotation) + (self.yColl2 - self.Py)* math.cos(self.rotation) + self.Py

        self.CollxTP3 = (self.xColl3 - self.Px)*math.cos(self.rotation) + (self.yColl3 - self.Py)* math.sin(self.rotation) + self.Px
        self.CollyTP3 = (self.Px - self.xColl3)*math.sin(self.rotation) + (self.yColl3 - self.Py)* math.cos(self.rotation) + self.Py

        self.CollxTP4 = (self.xColl4 - self.Px)*math.cos(self.rotation) + (self.yColl4 - self.Py)* math.sin(self.rotation) + self.Px
        self.CollyTP4 = (self.Px - self.xColl4)*math.sin(self.rotation) + (self.yColl4 - self.Py)* math.cos(self.rotation) + self.Py
        data1 = self.pixels[self.pitch * int(self.CollyTP1) + int(self.CollxTP1)]
        data2 = self.pixels[self.pitch * int(self.CollyTP2) + int(self.CollxTP2)]
        data3 = self.pixels[self.pitch * int(self.CollyTP3) + int(self.CollxTP3)]
        data4 = self.pixels[self.pitch * int(self.CollyTP4) + int(self.CollxTP4)]
        if data1 == 0:
            self.x = 185 * self.modX
            self.y = 432 * self.modY
            self.steer = 0
            self.velocity = 0
            self.xSpeed = 0
            self.ySpeed = 0
            self.rotation = 0
            return self.x, self.y, self.rotation, self.velocity, self.xSpeed, self.ySpeed, self.steer, True
        elif data2 == 0:
            self.x = 185 * self.modX
            self.y = 432 * self.modY
            self.steer = 0
            self.velocity = 0
            self.xSpeed = 0
            self.ySpeed = 0
            self.rotation = 0
            return self.x, self.y, self.rotation, self.velocity, self.xSpeed, self.ySpeed, self.steer, True
        elif data3 == 0:
            self.x = 185 * self.modX
            self.y = 432 * self.modY
            self.steer = 0
            self.velocity = 0
            self.xSpeed = 0
            self.ySpeed = 0
            self.rotation = 0
            return self.x, self.y, self.rotation, self.velocity, self.xSpeed, self.ySpeed, self.steer, True
        elif data4 == 0:
            self.x = 185 * self.modX
            self.y = 432 * self.modY
            self.steer = 0
            self.velocity = 0
            self.xSpeed = 0
            self.ySpeed = 0
            self.rotation = 0
            return self.x, self.y, self.rotation, self.velocity, self.xSpeed, self.ySpeed, self.steer, True
        else:
            return self.x, self.y, self.rotation, self.velocity, self.xSpeed, self.ySpeed, self.steer, False