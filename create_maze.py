#! /usr/bin/env python

from mcpi import minecraft
mc = minecraft.Minecraft.create()
position = mc.player. getTilePos()

x = position.x
y = position.y
z = position.z

f = open("maze1.txt", "r")
data = f.read().split("\n")

w = int(data[0])
h = int (data[1])

maze = []

for i in xrange(h):
    maze.append([])
    for j in xrange(int(w)):
        maze[i].append(data[i+2][j])

for i in xrange(h):
    for j in xrange(int(h)):
        mc.setBlock(x + i, y, z + j, 5, 2)
