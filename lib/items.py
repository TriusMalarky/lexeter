from lib.core import *


class stone(core):
    def __init__(self,debug):
        self.internalID = 'item-stone'
        self.name = 'stone'
        self.quality = 0
        self.debug = debug
        self.rDebug

class branch(core):
    def __init__(self,debug):
        self.internalID = 'item-branch'
        self.name = 'branch'
        self.quality = 0
        self.debug = debug
        self.rDebug

class scrapmetal(core):
    def __init__(self,debug):
        self.internalID = 'item-scrapmetal'
        self.name = 'metal scrap'
        self.quality = 0
        self.debug = debug
        self.rDebug

class egg(core):
    def __init__(self,debug):
        self.internalID = 'item-egg'
        self.name = 'egg'
        self.quality = 2
        self.debug = debug
        self.rDebug

class shinystone(core):
    def __init__(self,debug):
        self.internalID = 'item-shinystone'
        self.name = 'shiny stone'
        self.quality = 1
        self.debug = debug
        self.rDebug()

class diamond(core):
    def __init__(self,debug):
        self.internalID = 'item-diamond'
        self.name = 'diamond'
        self.quality = 3
        self.debug = debug
        self.rDebug()

class ruby(core):
    def __init__(self,debug):
        self.internalID = 'item-ruby'
        self.name = 'ruby'
        self.quality = 3
        self.debug = debug
        self.rDebug()

class sapphire(core):
    def __init__(self,debug):
        self.internalID = 'item-sapphire'
        self.name = 'sapphire'
        self.quality = 3
        self.debug = debug
        self.rDebug()

class emerald(core):
    def __init__(self,debug):
        self.internalID = 'item-emerald'
        self.name = 'emerald'
        self.quality = 3
        self.debug = debug
        self.rDebug()

class opal(core):
    def __init__(self,debug):
        self.internalID = 'item-opal'
        self.name = 'opal'
        self.quality = 3
        self.debug = debug
        self.rDebug()

class excalibur(core):
    def __init__(self,debug):
        self.internalID='item-excalibur'
        self.name = 'Excalibur'
        self.quality = 4
        self.debug = debug
        self.rDebug()

class item(core):
    def __init__(self,world):
        self.debug = world.debug
        self.rDebug()
        self.qualities = {
            0 : "trash",
            1 : "common",
            2 : "useful",
            3 : "treasure",
            4 : "impossible"
        }
        self.trash = [
            'stone',
            'branch',
            'scrapmetal'
        ]
        self.common = [
            'shinystone'
        ]
        self.useful = [
            'egg'
        ]
        self.treasure = [
            'diamond',
            'ruby',
            'sapphire',
            'emerald',
            'opal'
        ]
        self.impossible = [
            'excalibur'
        ]
        self.full = self.trash + self.common + self.useful + self.treasure + self.impossible
        self.stone = stone(self.debug)
        self.branch = branch(self.debug)
        self.scrapmetal = scrapmetal(self.debug)
        self.egg = egg(self.debug)
        self.shinystone = shinystone(self.debug)
        self.diamond = diamond(self.debug)
        self.excalibur = excalibur(self.debug)
        self.ruby = ruby(self.debug)
        self.sapphire = sapphire(self.debug)
        self.emerald = emerald(self.debug)
        self.opal = opal(self.debug)

