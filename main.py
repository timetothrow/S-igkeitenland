#! /usr/bin/env python
# coding=utf-8

"""
                Project Minecraft - Süßigkeitenland
    Course : English for Computer Science 
    Team   : 1 
    Group  : CD
    Members:    Nguyen Cong Dat,    Duong Thanh HUng
                Huynh Vinh Long,    Le Hong Thang
    Due day: --/06/2017 
    
"""

from mcpi import minecraft
from utility import *
from World import *

mc = minecraft.Minecraft.create()
hansel = mc.player
triggers = []


def main():
    global triggers

    #################################
    #          create world         #
    #################################

    # surface
    create_ground()
    create_craggy_mountains()
    create_forest()
    create_corn_candy_mountains()
    create_river()
    create_ice_cream_hills()
    create_lollipop_forest()
    create_cane_candy_forest()
    create_oreos()
    create_cupcake_village()
    create_coke_tower()

    # underground
    create_mazes()
    create_elevators()
    create_mobs()

    ###################################
    #          main game loop         #
    ###################################

    # move player to the initial position
    # TODO set init pos
    hansel.setTilePos(100, 100, 100)

    while True:
        for i in xrange(len(triggers)):
            if triggers[i].condition():
                triggers[i].action()


if __name__ == "__main__":
    main()
