#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from collections import OrderedDict
from buntusticker import Gui, BuntustickerTheme, ColorPair

class ColorTestTheme(BuntustickerTheme):
	
	def setUpColors(self):
			for fgCode in range(1, 16):
				for bgCode in range(1,255):
					self.addPair(ColorPair(str(fgCode)+"+"+str(bgCode), fgCode, bgCode))

class ColorTestGui(Gui):
	
	def logic(self, stdscr):
		for pairName in self.theme.pairs.keys():
			stdscr.addstr(pairName, self.theme.pairs[pairName].curses)

ColorTestGui(ColorTestTheme()).run()
