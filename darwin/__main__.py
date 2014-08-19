#!/usr/bin/env python
"""
Documentation
"""
import time

from Environment import Environment


def test():
    petriDish = Environment(initialPopSize=60, cycleLimit=1000)
    t0 = time.time()
    petriDish.run()
    t1 = time.time()
    #petriDish.end()
    print 'Done', t1-t0


def test2():
    petriDish = Environment(initialPopSize=40, cycleLimit=1000)

    from Creature import Creature
    import calculations

    x = Creature(petriDish, 0)
    y = Creature(petriDish, 0)

    print x.RGB
    print y.RGB

    t0 = time.time()
    for i in range(10000):
        diff = calculations.image_difference(x.RGB, y.RGB)
    t1 = time.time()
    print t1-t0

    t0 = time.time()
    for i in range(10000):
        diff = calculations.fast_image_difference(x.RGB, y.RGB)
    t1 = time.time()
    print t1-t0


if __name__ == "__main__":
    test()
