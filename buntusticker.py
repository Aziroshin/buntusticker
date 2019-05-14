#!/usr/bin/env python3

# ==============================================================================
# ====================================================
# ==========================
# Imports
from subprocess import Popen, PIPE
import curses, time
from collections import namedtuple, UserDict

ColorPairCodes = namedtuple("ColorPairCodes", ["fg", "bg"])

class ColorPair(object):
	
	def __init__(self, name, fgColor, bgColor):
		self.name = name
		self.fgColor = fgColor
		self.bgColor = bgColor
		
	def init(self, pairId):
		self.id = pairId
		curses.init_pair(self.id, self.fgColor, self.bgColor)
		
		
class CursesColorTheme(object):
	
	def __init__(self):
		self.pairs = {}
	
	def addPair(self, colorPair):
		self.pairs[colorPair.name] = colorPair
		return colorPair
		
	def init(self):
		colorPairId = 1
		for colorPair in self.pairs.values():
			colorPair.init(colorPairId)
			colorPairId += 1
	
class BuntuStickerTheme(CursesColorTheme):
	
	def __init__(self, init=False):
		super().__init__()
		self.addPair(ColorPair("fg", 60, 40))
		self.addPair(ColorPair("bg", 52, 20))
		if init:
			self.initColorPairs()

class Gui(object):
	
	def __init__(self, theme):
		self.theme = theme
		
	def setUpColors(self):
		for i in range(0, curses.COLORS):
			curses.init_pair()
	
	def wrapperCallback(self, stdscr):
		self.theme.init()
		stdscr.clear()
		curses.start_color()
		curses.use_default_colors()
		stdscr.box()
		stdscr.addstr("test")
		stdscr.getkey()
		stdscr.refresh()
		
	def run(self):
		curses.wrapper(self.wrapperCallback)
		
Gui(BuntuStickerTheme()).run()
