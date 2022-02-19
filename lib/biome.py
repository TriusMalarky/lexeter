try:
    from lib.core import *
except ModuleNotFoundError:
    log = open('save/log.txt', 'a')
    print("Warning! biome module unable to find core module.")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    log.write("!! Biome Module unable to find Core Module !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()
except ImportError:
    log = open('save/log.txt', 'a')
    print("Warning! biome module had issues importing Core module.")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    log.write("!! Biome Module issues importing Core Module !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()

try:
    import random
except ModuleNotFoundError:
    log = open('save/log.txt', 'a')
    print("Warning! biome module unable to find builtin module(s).")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    print("This involves one or more of Python's built-in modules. Consider reinstalling Python.")
    log.write("!! Action Module unable to find Builtin Module(s) !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()
except ImportError:
    log = open('save/log.txt', 'a')
    print("Warning! biome module had issues importing builtin module(s).")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    print("This involves one or more of Python's built-in modules. Consider reinstalling Python.")
    log.write("!! Action Module unable to import Builtin Module(s) !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()


class corebiome(core):
    def __init__(self):
        self.internalID = 'biome-core'
        self.buildings = []

    def genList(self, trash, common, useful, treasure, impossible):
        trash = trash * 10
        common =  common * 8
        useful = useful * 6
        treasure = treasure * 4
        impossible = impossible * 2
        list = []
        for i in range(trash):
            list.append(random.choice(self.world.item.trash))
        for i in range(common):
            list.append(random.choice(self.world.item.common))
        for i in range(useful):
            list.append(random.choice(self.world.item.useful))
        for i in range(treasure):
            list.append(random.choice(self.world.item.treasure))
        for i in range(impossible):
            list.append(random.choice(self.world.item.impossible))
        return list

    def loottable(self, quality):
        self.world.luckAttempts += 1
        trashMin = 0 + self.world.luck
        commonMin = 0 + (self.world.luck * 5)
        usefulMin = 0 + (self.world.luck * 10)
        treasureMin = 0 + (self.world.luck * 15)
        impossibleMin = 0 + (self.world.luck * 20)
        trashMax = trashMin + 110 - (self.world.luck * 10)
        commonMax = commonMin + 60 - (self.world.luck * 5)
        usefulMax = usefulMin + 40 + (self.world.luck * 5)
        treasureMax = treasureMin + (self.world.luck * 7)
        impossibleMax = impossibleMin + self.world.luck
        trashVar = random.randint(trashMin, trashMax)
        commonVar = random.randint(commonMin, commonMax)
        usefulVar = random.randint(usefulMin, usefulMax)
        treasureVar = random.randint(treasureMin, treasureMax)
        impossibleVar = random.randint(impossibleMin, impossibleMax)

        if quality == 0:
            listy = self.genList(trashVar * 5, commonVar * 4, usefulVar * 3, treasureVar * 2, impossibleVar)
        elif quality == 1:
            listy = self.genList(trashVar * 4, commonVar * 5, usefulVar * 4, treasureVar * 3, impossibleVar)
        elif quality == 2:
            listy = self.genList(trashVar * 3, commonVar * 4, usefulVar * 5, treasureVar * 3, impossibleVar)
        elif quality == 3:
            listy = self.genList(trashVar * 2, commonVar * 3, usefulVar * 4, treasureVar * 5, impossibleVar * 2)
        elif quality == 4:
            listy = self.genList(trashVar, commonVar * 2, usefulVar * 3, treasureVar * 4, impossibleVar * 3)
        loot = []
        for i in range(1, random.randint(1, 5)):
            loot.append(random.choice(listy))
        return loot

def roomlootquality(world):
    return random.randint(0, 2 + (world.luck // 5))


class pond(corebiome):
    def __init__(self, world):
        self.world = world
        self.internalID = 'biome-pond'
        self.descriptions=[
            'A sapphire blue pool sits in the center of the room, surrounded and filled by small flora. The air is refreshing.',
            'White cobblestones surround a deep blue pond. The room feels slightly mystical.'
        ]
        self.loot = self.loottable(roomlootquality(world))
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'pond'


class marble(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-marble'
        self.descriptions = [
            'Your footsteps clack on the marbled flooring. The gold engravings on the pillars surrounding you make the room feel regal.'
        ]
        self.loot = self.loottable(roomlootquality(world) + 1)
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'marble'


class terracotta(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-terracotta'
        self.descriptions = [
            'The floors and wall appear to be made of smashed, repurposed planter pots.'
        ]
        self.loot = self.loottable(roomlootquality(world))
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'terracotta'


class brickfloor(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-brickfloor'
        self.descriptions = [
            'For some reason, whoever built this room thought red bricks for a floor and paisley wallpaper would look cool.'
        ]
        self.loot = self.loottable(roomlootquality(world))
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'brick floor'


class fractured(corebiome):
    def __init__(self, world):
        self.world = world
        self.internalID = 'biome-fractured'
        self.descriptions = [
            'You have no idea what this room actually looks like.',
            "It appears you're inside of a kaleidoscope."
        ]
        self.loot = self.loottable(roomlootquality(world))
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'fractured'


class cave(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-cave'
        self.descriptions = [
            "Drip. Drip. Drip. It's a cave, all right."
        ]
        self.loot = self.loottable(roomlootquality(world))
        self.loot.append('stone')
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'cave'


class canopy(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-canopy'
        self.descriptions = [
            "It's not exactly obvious how a subsection of a rainforest ended up here, but it's best not to question it."
        ]
        self.loot = self.loottable(roomlootquality())
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'canopy'


class cavern(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-cavern'
        self.descriptions = [
            "You look up and wonder where the top is. Then you look into a hole and wonder where the bottom is."
        ]
        self.loot = self.loottable(roomlootquality(world))
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'cavern'


class shack(corebiome):
    def __init__(self, world):
        self.world = world
        self.internalID = 'biome-shack'
        self.descriptions = [
            "There is a clearing inside a forest . . . with an old cabin in the middle."
        ]
        self.loot = self.loottable(roomlootquality())
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'shack'