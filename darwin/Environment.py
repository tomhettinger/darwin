"""
The Environment class is the environment that the creatures live in.  An instance contains the 
creatures themselves, as well as the rules and conditions that the creatures must survive in.
"""
import itertools
import threading
from random import choice, shuffle

from Creature import Creature

DEATHRATE = 20  # absolute in number of creatures


class CreateCreatureThread(threading.Thread):
    def __init__(self, environment, parent, newName):
        threading.Thread.__init__(self)
        self.parent = parent
        self.newName = newName
        self.environment = environment

    def run(self):
        newCreature = self.parent.split(name=self.newName)
        __ = newCreature.get_fitness()
        self.environment.population.append(newCreature)


class Environment:
    """A 'box' of Creatures. Creatures can reproduce 
    (sometimes with a partner), get rewards, and die."""


    def __init__(self, initialPopSize=50, cycleLimit=100):
        self.cycleLimit = cycleLimit        # max number of cycles to run the simulation
        self.cycle = 0                      # current cycle
        self.idealColor = [128, 0, 128]     # the color that keeps things alive
        self.create_ideal()                 # make a creature of just this color
        self.sequence = itertools.count()   # generator for naming new creatures
        self.population = []                # list of creatures currently living in the environment
        self.populate(initialPopSize)


    def __str__(self):
        return 'Current Cycle:%d   Current Size:%d ' % (self.cycle, len(self.population))


    def create_ideal(self):
        """Create a creature of a single ideal color."""
        self.idealCreature = Creature(self, self.cycle, name='ideal')
        self.idealCreature.set_to_color(self.idealColor)


    def draw_ideal(self):
        """Draw an ideal creature using this environment's ideal color."""
        self.idealCreature.save_image(fileName='./images/ideal.png')


    def populate(self, popSize):
        """Fill the Environment with a given number of Creatures."""
        for i in range(popSize):
            thisName = "creature_%06d" % next(self.sequence)
            newCreature = Creature(self, self.cycle, name=thisName)
            self.population.append(newCreature)


    def kill(self):
        """Kill the weakest DEATHRATE Creatures.  This is the first step in the simulation."""
        self.population.sort(key=lambda creature: creature.get_fitness())  # sort by fitness
        del self.population[:DEATHRATE]
        

    def spawn(self):
        """Have the existing Creatures randomly reproduce to fill the DEATHRATE empty slots. 
        This is the second step in the simulation generation cycle."""
        parents = range(len(self.population))
        shuffle(parents)
        threads = []
        for i in range(DEATHRATE):
            newThread = CreateCreatureThread(environment=self, parent=self.population[parents[i]], newName="creature_%06d" % next(self.sequence))
            threads.append(newThread)
            newThread.start()
        for t in threads:
            t.join()
            

    def run(self):
        """Run the simulation. Cycle through kill() and spawn() until we reach 
        the cycle limit."""
        while self.cycle < self.cycleLimit:
            # Draw initial conditions
            #if self.cycle == 0:
            #    self.draw_ideal()
            #    for creature in self.population:
            #        creature.save_image('./images/initial/%s.png' % creature.name)

            # Status update
            if self.cycle % 100 == 0:
                print 'Cycle %d' % self.cycle
            #    for creature in self.population:
            #        print creature.name, creature.fitness

            self.kill()
            self.spawn()
            self.cycle += 1


    def end(self):
        """Draw Creatures and remove from memory."""
        print 'making images'
        print 'Cycle %d' % self.cycle
        for creature in self.population:
            print creature.name, creature.fitness
            creature.save_image('./images/final/%s.png' % creature.name)
