"""
    Provide common utilities for program
"""
from mcpi import minecraft

######################################
#         Important variables        #
######################################

mc = minecraft.Minecraft.create()
hansel = mc.player
pos = hansel.getPos()
tilePos = hansel.getTilePos()
triggers = []

######################################
#              Constants             #
######################################

ground_height = 0
number_of_floor = 3
