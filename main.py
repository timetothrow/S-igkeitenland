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
from World import *


def main():

    #################################
    #            variables          #
    #################################

    mc = minecraft.Minecraft.create()
    hansel = mc.player
    triggers = []

    #################################
    #          create world         #
    #################################

    # surface
    create_ground(mc)
    create_craggy_mountains(mc)
    create_forest(mc)
    create_corn_candy_mountains(mc)
    create_river(mc)
    create_ice_cream_hills(mc)
    create_lollipop_forest(mc)
    create_cane_candy_forest(mc)
    create_oreos(mc)
    create_cupcake_village(mc)
    create_coke_tower(mc)

    # underground
    create_mazes(mc)
    create_elevators(mc)
    create_mobs(mc)

    ###################################
    #          main game loop         #
    ###################################

    # move player to the initial position
    # TODO set init pos
    hansel.setTilePos(100, 100, 100)

    # loop
    while True:
        for i in xrange(len(triggers)):
            if triggers[i].condition():
                triggers[i].action()


if __name__ == "__main__":
    main()
