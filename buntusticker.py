#!/usr/bin/env python3

# ==============================================================================
# ====================================================
# ==========================
# Imports
from subprocess import Popen, PIPE
import curses, time
from collections import namedtuple, UserDict, OrderedDict

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
		self.pairs = OrderedDict()
		self.initialized = False
		self.setUpColors()
		self._borderChar = None
	
	@property
	def borderChar(self):
		if self._borderChar == None:
			self._borderChar = self.defaultBorderChar
		return self._borderChar
	
	@property
	def defaultPair(self):
		return ColorPair("default", 1, 1)
	
	@property
	def defaultBorderChar(self):
		return "#"
	
	def addPair(self, colorPair):
		self.pairs[colorPair.name] = colorPair
		return colorPair
	
	def initIfNotInit(self):
		if not self.initialized:
			self.init()
	
	def setUpColors(self):
		pass#TODO
	
	def init(self):
		colorPairId = 1
		self.addPair(self.defaultPair)
		for colorPair in self.pairs.values():
			colorPair.init(colorPairId)
			colorPairId += 1
		self.initialized = True
	
class BuntustickerTheme(CursesColorTheme):
		
	def setUpColors(self):
		self.addPair(ColorPair("main", 17, 11))
		self.addPair(ColorPair("main2", 5, 41))

class Origin(object):
	def __init__(self, lines, cols):
		self.lines = lines
		self.cols = cols

class Window(object):
	
	def __init__(self, lines, cols, originCol, originLine, theme):
		self.lines = lines
		self.cols = cols
		self.origin = Origin(originLine, originCol)
		self.curses = curses.newwin(self.lines, self.cols, self.origin.lines, self.origin.cols)
		self.theme = theme
		
	def refresh(self):
		self.curses.refresh()
		
	def drawBorder(self):
		#TODO: Actually implement border algorithm.
		for col in range(self.origin.cols, self.origin.cols+self.cols):
			self.addString(str(col), "default")
			#self.addString(self.theme.borderChar, "default")
		
	def addString(self, string, colorPairName):
		self.curses.addstr(string, self.theme.pairs[colorPairName].curses)

class Gui(object):
	
	def __init__(self, theme):
		self.theme = theme
	
	def logic(self, stdscr):
		win = Window(20,10, 0, 0, theme=self.theme)
		winB = Window(20,10, 20, 0, theme=self.theme)
		win.addString("test", "main")
		win.drawBorder()
		winB.addString("test", "main")
		stdscr.refresh()
		winB.refresh()
		win.refresh()
	
	def wrapperCallback(self, stdscr):
		self.theme.initIfNotInit()
		stdscr.clear()
		curses.use_default_colors()
		self.logic(stdscr)
		stdscr.getkey()
		
	def run(self):
		curses.wrapper(self.wrapperCallback)
	
if __name__ == "__main__":
	Gui(BuntustickerTheme()).run()
