import math
import pyglet as py
import numpy
numpy
class sight:
    def __init__(self, carX, carY, carRota,bitImg, pitch ,angle):
        self.isStraight = False
        self.carX = int(carX)
        self.carY = int(carY)
        self.carRota = carRota*math.pi/180
        self.bitImag = bitImg
        self.pitch = pitch
        self.angle = angle + self.carRota




    def degree90(self):
        self.y = self.carY
        for self.iPos in range(self.carX, 1920):
            self.wallPoint = self.bitImag[self.pitch * int(self.y) + int(self.iPos)]            
            if self.wallPoint == 0:
                self.line = py.shapes.Circle(self.iPos, self.carY, 3,color=(255,0,0))
                self.line.draw()
                break
        for self.iNeg in range(self.carX, 0,-1):
            self.wallPoint = self.bitImag[self.pitch * int(self.y) + int(self.iNeg)]
            if self.wallPoint == 0:        
                self.line = py.shapes.Circle(self.iNeg, self.carY, 3,color=(255,0,0))
                self.line.draw()
                break
        return



    def degree0(self):
        self.x = self.carX
        for self.iPos in range(self.carY, 1080):
            self.wallPoint = self.bitImag[self.pitch * int(self.iPos) + int(self.x)]    
            if self.wallPoint == 0:
                self.line = py.shapes.Circle(self.x, self.iPos, 3,color=(255,0,0))
                self.line.draw()
                break
        for self.iNeg in range(self.carY, 0,-1):
            self.wallPoint = self.bitImag[self.pitch * int(self.iNeg) + int(self.x)]
            if self.wallPoint == 0:
                self.line = py.shapes.Circle(self.x, self.iNeg, 3,color=(255,0,0))
                self.line.draw()
                break
        return

    def angled(self):
        self.slope = math.tan(self.angle*math.pi/180)
        self.c = self.carY-(self.carX*self.slope)
        for self.iPos in range(self.carX,1920):
            self.y = (self.slope * self.iPos) + self.c
            self.wallPoint = self.bitImag[self.pitch * int(self.y) + int(self.iPos)]
            if self.wallPoint == 0:
                self.line = py.shapes.Circle(self.iPos, self.y, 3,color=(255,0,0))
                self.line.draw()
                break
        for self.iNeg in range(self.carX,0, -1):
            self.y = (self.slope * self.iNeg) + self.c
            self.wallPoint = self.bitImag[self.pitch * int(self.y) + int(self.iNeg)]
            if self.wallPoint == 0:
                self.line = py.shapes.Circle(self.iNeg, self.y, 3,color=(255,0,0))
                self.line.draw()
                break
        self.slope = math.tan(self.angle*math.pi/180)
        self.slope = self.slope *-1
        self.c = self.carY-(self.carX*self.slope)
        for self.iPos in range(self.carX,1920):
            self.y = (self.slope * self.iPos) + self.c
            self.wallPoint = self.bitImag[self.pitch * int(self.y) + int(self.iPos)]
            if self.wallPoint == 0:
                self.line = py.shapes.Circle(self.iPos, self.y, 3,color=(255,0,0))
                self.line.draw()
                break
        for self.iNeg in range(self.carX,0, -1):
            self.y = (self.slope * self.iNeg) + self.c
            self.wallPoint = self.bitImag[self.pitch * int(self.y) + int(self.iNeg)]
            if self.wallPoint == 0:
                self.line = py.shapes.Circle(self.iNeg, self.y, 3,color=(255,0,0))
                self.line.draw()
                break
        return




    def line(self):
        if abs(self.angle) == 90:
            sight.degree90(self)
            return
        elif self.angle == 0:
            sight.degree0(self)
            return
        else:
            sight.angled(self)
            return
        
        
        
    
    
    
    