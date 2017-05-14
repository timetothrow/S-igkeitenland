#! /usr/bin/env python
# coding=utf-8

from utility import *

##################################################
#                   surface                      #
##################################################


def create_ground(mc):
    """clear sky and create ground"""

    # ground
    # TODO select material
    mc.setBlocks(127, ground_height, 127, -128, -64, -128, 1)

    # air
    mc.setBlocks(127, 63, 127, -128, ground_height, -128, 0)


def create_mountain(mc):
    """create a mountain"""
    pass


def create_craggy_mountains(mc):
    """create tall mountains surround map"""
    pass


def create_tree(mc):
    """create one tree"""
    pass


def create_forest(mc):
    """ create a forest at the south of the map"""
    pass


def create_corn_mountain(mc):
    """create a corn candy mountain"""
    pass


def create_corn_candy_mountains(mc):
    """ create a forest at the south of the map"""
    pass


def create_river(mc):
    """create a chocolate river"""
    pass


def create_hill(mc):
    """create an ice-cream hill"""


def create_ice_cream_hills(mc):
    """create ice cream hills at the west of the map"""


def create_lollipop(mc):
    """create a lollipop"""


def create_lollipop_forest(mc):
    """create a lollipop forest at the south of the map"""


def create_cane_candy(mc):
    """create a cane candy"""


def create_cane_candy_forest(mc):
    """create cane candy forest at the north of the map"""


def create_oreo(mc):
    """create a oreo"""


def create_oreos(mc):
    """create oreos at the east of the map"""


def create_cupcake_village(mc):
    """create cupcake village at the center of the map"""


def create_coke_tower(mc):
    """create_coke_tower at the north of the village"""


####################################
#          underground             #
####################################


def create_maze_floor(mc, floor):
    """
            create a floor of the maze
        file structure:
        length, width, height of maze
        x, y, z position of first block of maze
        # #  #  #####   ...
        # ##  #  ########...
        # = block
        :r
    """

    # load data from file to array
    f = open("./data/mazes/maze" + str(floor) + ".txt", "r")
    maze_map = f.read(mc).split("\n")
    l, w, h = maze_map.pop(0).split(mc)
    x, y, z = maze_map.pop(0).split(mc)

    # create maze
    for i in xrange(l):
        for j in xrange(w):
            # TODO more type of block
            block_type = 2 if maze_map[i][j] == '#' else 0
            for k in xrange(h):
                mc.setBlock(x + i, y + k, z + j, block_type)


def create_mazes(mc):
    """create floors of the maze"""
    for i in xrange(number_of_floor):
        create_maze_floor(mc, i)


def create_elevator(mc):
    """create a elevator"""


def create_elevators(mc):
    """create elevators connecting floors of maze"""


def create_mobs(mc):
    """create mobs all over the maze"""
