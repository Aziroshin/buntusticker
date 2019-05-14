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
		
	@property
	def curses(self):
		return curses.color_pair(self.id)
		
		
class CursesColorTheme(object):
	
	def __init__(self):
		self.pairs = {}
		self.initialized = False
	
	def addPair(self, colorPair):
		self.pairs[colorPair.name] = colorPair
		return colorPair
	
	def initIfNotInit(self):
		if not self.initialized:
			self.init()
	
	def init(self):
		colorPairId = 1
		for colorPair in self.pairs.values():
			colorPair.init(colorPairId)
			colorPairId += 1
		self.initialized = True
	
class BuntuStickerTheme(CursesColorTheme):
	
	def __init__(self):
		super().__init__()
		self.addPair(ColorPair("fg", 60, 40))
		self.addPair(ColorPair("bg", 52, 20))

class Gui(object):
	
	def __init__(self, theme):
		self.theme = theme
	
	def wrapperCallback(self, stdscr):
		self.theme.initIfNotInit()
		stdscr.clear()
		curses.use_default_colors()
		stdscr.box()
		stdscr.addstr("test", self.theme.pairs["fg"].curses)
		stdscr.getkey()
		stdscr.refresh()
		
	def run(self):
		curses.wrapper(self.wrapperCallback)
		
Gui(BuntuStickerTheme()).run()
