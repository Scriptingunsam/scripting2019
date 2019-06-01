#!/usr/bin/python
# -*- coding: latin-1 -*-
# C5-Scr Manuel Jofre Poza TP2
import maya.cmds as mc
import maya.mel as mel
import os

estaCarpeta = os.path.abspath(__file__).split('.')[0] + '.bmp'

topShelf = mel.eval('$nul = $gShelfTopLevel')
currentShelf = mc.tabLayout(topShelf, q=1, st=1)
mc.shelfButton(parent=currentShelf, annotation='AutoRetopo', i=estaCarpeta, command='import AutoRetopo\nreload(AutoRetopo)' )