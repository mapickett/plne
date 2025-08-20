from colorgram import extract
import random

class Palette:

    def __init__(self, filename, number_of_colors):
        self.palette = []
        colors = extract(filename, number_of_colors)
        for item in colors:
            rbg = (item.rgb.r, item.rgb.g, item.rgb.b)
            self.palette.append(rbg)

    def get_color(self):
        return random.choice(self.palette)