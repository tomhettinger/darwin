"""
The Environment class is the environment that the creatures live in.  An instance contains the 
creatures themselves, as well as the rules and conditions that the creatures must survive in.
"""
import itertools
from random import choice, shuffle

from Creature import Creature

DEATHRATE = 20  # absolute in number of creatures


class Environment:
    """A 'box' of Creatures. Creatures can reproduce 
    (sometimes with a partner), get rewards, and die."""


    def __init__(self, initialPopSize=50, cycleLimit=100):
        self.cycleLimit = cycleLimit        # max number of cycles to run the simulation
        self.cycle = 0                      # current cycle
        self.idealColor = [128, 0, 128]     # the color that keeps things alive
        self.sequence = itertools.count()   # generator for naming new creatures
        self.population = []                # list of creatures currently living in the environment
        self.populate(initialPopSize)


    def __str__(self):
        return 'Current Cycle:%d   Current Size:%d ' % (self.cycle, len(self.population))


    def draw_ideal(self):
        """Draw an ideal creature using this environment's ideal color."""
        idealCreature = Creature(self, self.cycle, name='ideal')
        idealCreature.set_to_color(self.idealColor)
        idealCreature.save_image(fileName='./images/ideal.png')
        del idealCreature


    def populate(self, popSize):
        """Fill the Environment with a given number of Creatures."""
        for i in range(popSize):
            thisName = "creature_%06d" % next(self.sequence)
            newCreature = Creature(self, self.cycle, name=thisName)
            self.population.append(newCreature)


    def kill(self):
        """Kill the weakest DEATHRATE Creatures.  This is the first step in the simulation."""
        self.population.sort(key=lambda creature: creature.fitness)  # sort by fitness
        del self.population[:DEATHRATE]
        

    def spawn(self):
        """Have the existing Creatures randomly reproduce to fill the DEATHRATE empty slots. 
        This is the second step in the simulation generation cycle."""
        parents = range(len(self.population))
        shuffle(parents)
        for i in range(DEATHRATE):
            newName = "creature_%06d" % next(self.sequence)
            newCreature = self.population[parents[i]].split(self, self.cycle, name=newName)
            self.population.append(newCreature)


    def run(self):
        """Run the simulation. Cycle through kill() and spawn() until we reach 
        the cycle limit."""
        while self.cycle < self.cycleLimit:
            # Draw initial conditions
            if self.cycle == 0:
                self.draw_ideal()
                for creature in self.population:
                    creature.save_image('./images/initial/%s.png' % creature.name)

            # Status update
            if self.cycle % 100 == 0:
                print 'Cycle %d' % self.cycle
                for creature in self.population:
                    print creature.name, creature.fitness

            self.kill()
            self.spawn()
            self.cycle += 1


    def end(self):
        """Draw Creatures and remove from memory."""
        print 'making images'
        print 'Cycle %d' % self.cycle
        print len(self.population)
        print self.population[0].name, sum(self.population[0].RGB)
        print self.population[-1].name, sum(self.population[-1].RGB)
        for creature in self.population:
            print creature.name, creature.fitness
            creature.save_image('./images/final/%s.png' % creature.name)
