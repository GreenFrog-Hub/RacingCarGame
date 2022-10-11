import pyglet as pyg
from PIL import Image

class track:
    def __init__(self, width, height, modX, modY):
        self.width = width
        self.height = height
        self.display = pyg.canvas.Display()
        self.screen = self.display.get_default_screen()
        self.preTrack = Image.open("track2.png")
        self.preTrackWidth, self.preTrackHeigh = self.preTrack.size
        self.modX, self.modY = modX, modY
        self.newTrack = self.preTrack.resize((int(self.preTrackWidth*self.modX), int(self.preTrackHeigh*self.modY)))
        self.newTrack.save("track.png")
    def loadTrack(self):
        self.track = pyg.image.load("track.png")
        return self.track
