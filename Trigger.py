# coding=utf-8

from math import sqrt
from utility import *


class Trigger(object):
    """Base class for other blocks can trigger an event"""

    def __init__(self, x, y, z, d, block_type, material=0):
        # set values
        self.x = x
        self.y = y
        self.z = z
        self.d = d
        self.block_type = block_type
        self.material = material

        # add self to triggers list
        triggers.append(self)

    def distance(self):
        """distance between self and hansel"""
        return sqrt((self.x - hansel.x) ** 2 + (self.y - hansel.y) ** 2 + (self.z - hansel.z) ** 2)

    def condition(self):
        """condition for action to happen"""
        if mc.getBlock() != self.block_type:
            self.__del__()

        if self.distance() < self.d:
            return True
        return False

    def action(self):
        # TODO remove self from triggers when finish; some remain
        pass

    def __del__(self):
        triggers.remove(self)


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
