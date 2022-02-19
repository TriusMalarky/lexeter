try:
    from lib.action import act
except ModuleNotFoundError:
    log = open('save/log.txt', 'a')
    print("Warning! darkroom module unable to find action module.")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    log.write("!! Darkroom Module unable to find Action Module !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()
except ImportError:
    log = open('save/log.txt', 'a')
    print("Warning! darkroom module had issues importing action module.")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    log.write("!! Darkroom Module issues importing Action Module !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()

try:
    from lib.core import *
except ModuleNotFoundError:
    log = open('save/log.txt', 'a')
    print("Warning! darkroom module unable to find core module.")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    log.write("!! Darkroom Module unable to find Core Module !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()
except ImportError:
    log = open('save/log.txt', 'a')
    print("Warning! darkroom module had issues importing Core module.")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    log.write("!! Darkroom Module issues importing Core Module !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()

try:
    import random
except ModuleNotFoundError:
    log = open('save/log.txt', 'a')
    print("Warning! darkroom module unable to find builtin module(s).")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    print("This involves one or more of Python's built-in modules. Consider reinstalling Python.")
    log.write("!! Darkroom Module unable to find Builtin Module(s) !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()
except ImportError:
    log = open('save/log.txt', 'a')
    print("Warning! darkroom module had issues importing builtin module(s).")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    print("This involves one or more of Python's built-in modules. Consider reinstalling Python.")
    log.write("!! Darkroom Module unable to import Builtin Module(s) !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()



class shade(core):
    def __init__(self, name, world):
        try:
            self.name = name
            world.characterlist.append(self.name)
            self.internalID = 'character-shade-'+self.name
            self.world = world
            self.debug = self.world.debug
            self.rDebug()
            self.room = 'darkroom'
            self.hp = 15
            self.act = act(self.name,self.world)
            self.age = 0
            self.tickCount = random.randrange(1,5)
            self.prefer = prefer()

            if self.name == 'mek':
                self.prefer.fruit = 'orange'
                self.week = 5
            elif self.name == 'geoflib':
                self.prefer.fruit = 'pineapple'
                self.week = 4
        except:
            log = open('save/log.txt', 'a')
            print("Warning! Issue initializing shade" + name + ".")
            print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
            log.write("!! Darkroom Module unable to initialize character-shade-" + name + " !!")
            _ = input("Enter anything to exit Lexeter: ")
            log.write("|| Closing Lexeter ||\n")
            log.close()
            quit()

    def tick(self, world):
        self.age += 1
        self.tickCount += 1
        if self.tickCount == self.week: self.tickCount=1
        if self.tickCount == 1:
            lines = [
                'heya, stranger!','im a shade, not a ghost. theres a difference.',
                'waddup, '+world.player.name+'?','evening!',
                'i cannae find ma lunch!', 'i like ' + self.prefer.fruit + 's. my brother doesnt.',
                'ah, the darkness. so refreshing.','blegh! just got a bug in my mouth!',
                'have ya talked to my twin?','tha rats here, they make quite the racket!',
                'not a big fan of moths. how bout you?','ever been to paris?']
            self.act.speak(random.choice(lines), self.room)
        elif self.tickCount == 2:
            pass # ask
        elif self.tickCount == 3:
            pass #nothing/atk
        elif self.tickCount == 4:
            pass #possiblemove
        
        
class darkroom(core):
    def __init__(self, world):
        try:
            self.world = world
            self.internalID = 'room-darkroom'
            self.debug = self.world.debug
            self.rDebug()
            world.characters.geoflib = shade('geoflib', world)
            world.characters.mek = shade('mek', world)
            self.descriptions = [
                "It's incredibly dark.",
                "There's not much here.",
                "Where'd everything go?"
            ]
            self.loot = []
            self.buildings = []
        except:
            log = open('save/log.txt', 'a')
            print("Warning! Issue initializing darkroom.")
            print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
            log.write("!! Darkroom Module unable to initialize room-darkroom !!")
            _ = input("Enter anything to exit Lexeter: ")
            log.write("|| Closing Lexeter ||\n")
            log.close()
            quit()

