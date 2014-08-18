"""
The Creature class is a 8x8 pixel RGB image.  The Creature can reproduce
asexually with some mutations to its colors.
"""
import copy

import Image
import numpy as np

WIDTH = 8
HEIGHT = 8


class Creature:

    def __init__(self, environment, birthcycle, name='creature_default'):
        self.name = name
        self.environment = environment
        imarray = np.random.rand(WIDTH, HEIGHT, 3) * 255
        self.RGB = imarray.astype('uint8')
        self.birthdate = birthcycle
        self.fitness = self.check_fitness()


    def __str__(self):
        return 'Name:%s   Born:%d   Fitness:%.7f' % (self.name, self.birthdate, self.fitness)


    def draw(self):
        """Draw the image and show it."""
        im = Image.fromarray(self.RGB).convert('RGBA')
        im.show()


    def save_image(self, fileName=None):
        """Draw the image and save to disk."""
        print np.mean(self.RGB)
        im = Image.fromarray(self.RGB).convert('RGBA')
        if fileName is not None:
            im.save(fileName, "PNG")
        else:
            im.save('temp.png', "PNG")


    def set_name(self, newValue):
        self.name = newValue


    def set_birthdate(self, newValue):
        self.birthdate = newValue


    def set_fitness(self, newValue):
        self.fitness = newValue


    def set_to_color(self, targetRGB):
        """Set the entire image to a singel color."""
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self.RGB[x][y] = targetRGB


    def check_fitness(self):
        """Use the environment's ideal color to check fitness and return
        a value.  Value is based on the sum of the difference in RGB values."""
        totalDiff = 0
        for x in range(WIDTH):
            for y in range(HEIGHT):
                squareDiffs = [(self.RGB[x][y][band] - self.environment.idealColor[band])**2 for band in range(3)]
                pixelDistance = np.sqrt(sum(squareDiffs))
                totalDiff += pixelDistance
        fitness = -totalDiff       # control the sensitivity of difference here
        return fitness


    def mutate(self, freq=0.125):
        """Get a new random RGB value for pixels.  The fraction of affected pixels
        is equal to the freq of mutation."""
        mutationCount = int(HEIGHT*WIDTH*freq)
        #np.random.seed()
        for i in range(mutationCount):
            x, y = np.random.randint(0, HEIGHT), np.random.randint(0, WIDTH)
            self.RGB[x][y] = np.random.randint(0, 255, 3)


    def split(self, environment, cycle, name=None):
        newCreature = Creature(environment, cycle, name)
        newCreature.RGB = self.RGB.copy()
        newCreature.mutate()
        newCreature.set_fitness(newCreature.check_fitness())
        return newCreature
