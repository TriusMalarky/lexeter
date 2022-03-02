
from lib.core import *
from lib.action import *
from lib.core import core
from lib.darkroom import *
import random
from lib.biome import *
from lib.items import *
import string

# subclass responselog for logging player's responses
class responselog(core):
    def __init__(self):
        self.internalID='player-response-log'
    

class player(core):
    def __init__(self,age,them,world,debug):
        self.them=them;self.debug = debug;self.internalID='player-instance';self.rDebug()
        self.hp=50;self.rLog=responselog()
        self.them.act.speak("What is your name?\n")
        self.name=input("")
        self.them.act.speak(self.name+", eh?")
        self.them.act.speak("Well, have a fun adventure.");print("");print("")
        self.instance=age;self.age=age
        self.inventory = []
        self.act=playerAct(self,world)

class wmap(core):
    def __init__(self,world):
        self.debug=world.debug
        self.internalID='world-map'
        self.rDebug()
        
class world(core):
    def __init__(self, age, them, zones, debug, item, recipes, constructs, lexeter):
        self.debug=debug;self.them=them;self.zones=zones
        self.lexeter = lexeter
        self.internalID = 'reality-instance'
        self.rDebug()
        self.them.act.speak("Hmmmmm . . .")
        self.them.act.speak("There's nothing here.")
        if self.lexeter.seedable:
            if input("[#`~<,>_r-kal]: Do you want to add your input?\n(yes or no): ") == 'yes':
                self.seed = input("[#`~<,>_r-kal]: What kind of world do you want?\n(input seed): ")
            else:
                self.seed = ''.join(random.choice(string.digits) for i in range(16))
        else:
            self.seed = ''.join(random.choice(string.digits) for i in range(16))
        random.seed(self.seed)
        print(random.randint(0,100))
        self.them.act.speak("Give me a minute.")
        self.time = 45+(age*5)
        self.instance = age
        self.age = 0
        self.player = player(age,them,self,debug)
        self.characters = characters()
        self.characterlist = []
        self.item = item
        self.recipes = recipes
        self.constructs = constructs

        self.luck = 3
        self.luckAttempts = 0

        self.map = wmap(self)
        self.map.darkroom = darkroom(self)
        self.map.route = {'darkroom': []}
        self.map.list = ['darkroom']
        for i in range(3):
            zone = random.choice(self.zones)
            room = str(zone+'_'+str(i))
            self.map.route['darkroom'].append(room);self.map.route[room] = ['darkroom']
            self.map.list.append(room)
            exec('self.map.'+room+'='+zone+'(self)')
        self.player.room = 'darkroom'



# subclass characters for saving each individual character
class characters(core):
    def __init__(self):
        self.internalID='character-list'

class them():
    def __init__(self):
        self.name="#`~<,>_r-kal"
        self.internalID='__ignore__'
        self.act = actGod(self.name)


class Lexeter(core):
    def __init__(self):
        self.debug = False
        self.internalID = 'lexeter'
        self.rDebug()
        self.them = them()
        self.instances = 1
        self.seedable = True
        self.zones = ['pond', 'marble', 'terracotta', 'brickfloor', 'fractured', 'cave', 'canopy', 'cavern', 'shack']
        self.achievements = []
        self.item = Item(self)
        self.recipes = Recipes(self)
        self.constructs = Constructs(self)

        #graphics


        # config
        self.config_fullscreen = True
        self.config_framesPerSecond = 60


        # Game Rules
        self.death = True
        self.sound = True
        self.luck = True
        self.crafting = True
        self.friction = True
        self.time = True
        self.items = True
        self.shade = True


        self.fishing = False
        self.farming = False
        self.orange = False
        self.swim = False

        self.world = world(self.instances, self.them, self.zones, self.debug, self.item, self.recipes, self.constructs, self)


