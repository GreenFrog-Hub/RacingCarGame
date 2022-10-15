import pyglet as pyg
from PIL import Image
import filePath
class walls:
    def __init__(self, width, height, modX, modY):
        self.width = width
        self.height = height
        self.display = pyg.canvas.Display()
        self.screen = self.display.get_default_screen()
        self.preTrack = Image.open(filePath.resource_path("BW.png"))
        self.preTrackWidth, self.preTrackHeigh = self.preTrack.size
        self.modX, self.modY = modX, modY
        self.newTrack = self.preTrack.resize((int(self.preTrackWidth*self.modX), int(self.preTrackHeigh*self.modY)))
        self.newTrack.save("BW1.png")
    def loacteWalls(self):
        self.trackWalls = pyg.image.load(filePath.resource_path("BW1.png"))
        self.rawimage = self.trackWalls.get_image_data()
        self.data = None
        self.format = 'L'
        self.pitch = self.rawimage.width * len(self.format)
        self.pixels = self.rawimage.get_data(self.format, self.pitch)
        self.bitPattern = []
        return self.pitch, self.pixels