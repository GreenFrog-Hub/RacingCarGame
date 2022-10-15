import pyglet as pg
from PIL import Image
import filePath
class carBuild:
    def __init__(self, width, height, modX, modY):
        self.width = width
        self.height = height
        self.preCar = Image.open(filePath.resource_path("preCar.png"))
        self.preCarWidth, self.preCarHeigh = self.preCar.size
        self.modX, self.modY = modX, modY
        self.newcar = self.preCar.resize((int(self.preCarWidth*self.modX), int(self.preCarHeigh*self.modY)))
        self.newcar.save("car.png")
        
    def sprite(self):
        self.car1 = pg.image.load(filePath.resource_path("Car.png"))
        self.car1.anchor_x = self.car1.width // 2
        self.car1.anchor_y = self.car1.height // 2
        return self.car1



