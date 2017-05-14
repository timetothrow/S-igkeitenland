# coding=utf-8

from math import sqrt
from utility import *
import main


class Trigger(object):
    """Base class for other blocks can trigger an event"""

    def __init__(self, x, y, z, d, block_type, material=0):
        self.x = x
        self.y = y
        self.z = z
        self.d = d
        self.block_type = block_type
        self.material = material

    def distance(self, hansel):
        return sqrt((self.x - hansel.x) ** 2 + (self.y - hansel.y) ** 2 + (self.z - hansel.z) ** 2)

    def condition(self):
        if self.distance(main.hansel) < self.d and main.mc.getBlock() == self.block_type:
            return True
        return False

    def action(self):
        pass


#################################################
#          The trap leads to the maze           #
#################################################

class FallToMaze(Trigger):
    """This will open a hole under Hansel and he 
    will fall into the lowest level of the maze"""

    def __init__(self):
        super(FallToMaze, self).__init__(100, 100, 100, 2, 0)

    def action(self):
        # TODO make a hole under hansel
        pass


################################################
#              Traps in the maze               #
################################################


################################################
#                 Final trap                   #
################################################
