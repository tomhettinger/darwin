import sys

import pygame
from pygame.locals import *

from Environment import Environment, IDEAL_RGB
from Creature import WIDTH as CREATURE_WIDTH
from Creature import HEIGHT as CREATURE_HEIGHT

GREEN_COLOR = pygame.Color(0, 180, 64)
IDEAL_COLOR = pygame.Color(*IDEAL_RGB)
CREATURE_SPACING = CREATURE_WIDTH * 1.5
POP_DIM = 20
POPULATION_SIZE = POP_DIM * POP_DIM
CYCLE_LIMIT = 600

class Window:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.paused = True
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Darwin')

        # Make the environment and creatures
        self.environment = Environment(initialPopSize=POPULATION_SIZE, cycleLimit=CYCLE_LIMIT)

        # Set up the 'initial generation' surface
        self.initialGenerationSurface = pygame.Surface((POP_DIM*CREATURE_SPACING, POP_DIM*CREATURE_SPACING))
        self.initialGenerationSurface.fill(IDEAL_COLOR)
        self.initialFont = pygame.font.Font(None, 24)
        self.initialText = self.initialFont.render("Generation 0", 1, (10, 10, 10))
        self.initialCreatureSurfaceList = self.create_empty_surfaces()
        self.update_creatures(creatureSurfaceList=self.initialCreatureSurfaceList)

        # Set up the 'current population' surface
        self.populationSurface = pygame.Surface((POP_DIM*CREATURE_SPACING, POP_DIM*CREATURE_SPACING))
        self.populationSurface.fill(IDEAL_COLOR)
        self.cycleFont = pygame.font.Font(None, 24)
        self.creatureSurfaceList = self.create_empty_surfaces()


    def create_empty_surfaces(self):
        """Make a set of empty surfaces equal to the number of creatures and 
        return them as a list."""
        surfaceList = []
        for i in range(POPULATION_SIZE):
            surfaceList.append(pygame.Surface((CREATURE_WIDTH, CREATURE_HEIGHT)))
        return surfaceList


    def update_creatures(self, creatureSurfaceList=None):
        """Draw creature pixels onto the surfaces."""
        if creatureSurfaceList is None:
            creatureSurfaceList = self.creatureSurfaceList
        for i, creature in enumerate(self.environment.population):
            pygame.surfarray.blit_array(creatureSurfaceList[i], creature.RGB)


    def refresh_creature_display(self, popSurface, creatureSurfaceList):
        """Refresh the display of the surfaces."""
        for i in range(POPULATION_SIZE):
            x = (i / POP_DIM) * CREATURE_SPACING + (CREATURE_SPACING/4)
            y = (i % POP_DIM) * CREATURE_SPACING + (CREATURE_SPACING/4)
            popSurface.blit(creatureSurfaceList[i], (x,y))


    def main_loop(self):
        fpsClock = pygame.time.Clock()

        while True:
            # React to Events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))
                    elif event.key == K_SPACE:
                        self.paused = not self.paused

            # Evolve population by one generation
            if not self.paused:
                self.environment.evolve_one_generation()

            if self.environment.cycle % 5 == 0:
                self.cycleText = self.cycleFont.render("Generation %d" % self.environment.cycle, 1, (10, 10, 10))
                self.update_creatures()

            # Draw and refresh various layers
            self.screen.fill(GREEN_COLOR)

            self.refresh_creature_display(self.initialGenerationSurface, self.initialCreatureSurfaceList)
            self.screen.blit(self.initialGenerationSurface, (100, 200))
            self.screen.blit(self.initialText, (100, 180))
            
            self.refresh_creature_display(self.populationSurface, self.creatureSurfaceList)
            self.screen.blit(self.populationSurface, (400, 200))
            self.screen.blit(self.cycleText, (400, 180))

            pygame.display.update()
            fpsClock.tick(60)