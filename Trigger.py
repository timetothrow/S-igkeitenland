# coding=utf-8

from math import sqrt
from utility import *
import main


class Trigger(object):
    """Base class for other blocks can trigger an event"""

    def __init__(self, x , y , z, block_type, material, d):
        self.x = x
        self.y = y
        self.z = z
        self.block_type = block_type
        self.material = material
        self.d = d

    def distance(self, hansel):
        return sqrt((self.x - hansel.x)**2 + (self.y - hansel.y)**2 + (self.z - hansel.z)**2)

    def condition(self):
        if self.distance(main.hansel) < self.d and main.mc.getBlock() == self.block_type:
            return True
        return False

    def action(self):
        pass


# TODO add more classes
