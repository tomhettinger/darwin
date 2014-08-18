#!/usr/bin/env python
"""
Documentation
"""
#from Tkinter import *

from Environment import Environment


#class GUI:
#    def __init__(self):
#        pass


#def main():
#    root = Tk()
#    root.title("Inkling")
#    myGUI = GUI(root)
#    root.resizeable(False, False)
#    root.mainloop()


def test():
    petriDish = Environment(initialPopSize=40, cycleLimit=1000)
    petriDish.run()
    petriDish.end()
    print 'Done'

if __name__ == "__main__":
    test()
