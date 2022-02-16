import pickle
import os
import inspect
import random

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

class core(): # <-- core class, all other classes should inherit this
    def __init__(self):
        self.internalID='core-parent'
    def __str__(self): # <-- core function for displaying all relevant members of a given class instance
        attr = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
        ar=[]
        for _ in [a for a in attr if not(a[0].startswith('__')) and not(a[0].startswith('internal'))]:
            ar.append(_)
        return str(ar)
    def rDebug(self):
        if self.debug:
            print("Debug: " + self.internalID)
            print(" ++ "+ str(self))

class prefer(core): # <-- dummy class
    def __init(self):
        self.internalID='character-preference'


def save(lexeter):
    lexMem=inspect.getmembers(lexeter,lambda a:not(inspect.isroutine(a))) # <-- Not sure if this is necessary, the save function only worked right after I added this though . . .
    loc=open('save\\lexeter.txt','wb')
    pickle.dump(lexeter,loc)
    # Unused function for saving each individual class instance. Ignore.
    #for lexMemEntry in [a for a in lexMem if not(a[0].startswith('__') and not (a[0].startswith('internal'))]:
        #loc=open('save\\'++'.txt','wb')
        #pickle.dump(lexMemEntry,loc)

    
def load():
    savefile=open('save\\lexeter.txt','rb') # <-- open save file in readable binary for pickle
    return pickle.load(savefile) # <-- returning loaded save state class instance

def lex_init():
    if os.path.exists('save\\lexeter.txt'):
        lexet = load()
        random.seed = lexet.world.seed
        return lexet # <-- returning the loaded save state class instance
    else:
        open('save\\lexeter.txt','w')
        from lib.player import Lexeter
        lexet = Lexeter()
        save(lexet) # <-- saving the save state instance
        return lexet # <-- returning the newly created save state






def tick(lexeter,world):
    for _ in world.characterlist:
        exec('world.characters.'+_.lower()+'.tick(world)')
    world.player.act.playeraction()
    save(lexeter) # save on every tick
    tick(lexeter,world)
from lib.core import *
import random


class corebiome(core):
    def __init__(self):
        self.internalID = 'biome-core'
        self.buildings = []

    def genList(self,trash,common,useful,treasure,impossible):
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
        if quality == 0:
            list = self.genList(99,15,7,3,1)
        elif quality == 1:
            list = self.genList(20,70,10,3,1)
        elif quality == 2:
            list = self.genList(5,10,30,3,1)
        elif quality == 3:
            list = self.genList(15,10,5,20,1)
        elif quality == 4:
            list = self.genList(1,2,3,4,5)
        loot = []
        for i in range(1,random.randint(1,5)):
            loot.append(random.choice(list))
        return loot


class pond(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-pond'
        self.descriptions=[
            'A sapphire blue pool sits in the center of the room, surrounded and filled by small flora. The air is refreshing.',
            'White cobblestones surround a deep blue pond. The room feels slightly mystical.'
        ]
        self.loot = self.loottable(2)
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
        self.loot = self.loottable(2)
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
        self.loot = self.loottable(2)
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
        self.loot = self.loottable(0)
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
        self.loot = self.loottable(3)
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
        self.loot = self.loottable(1)
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
        self.loot = self.loottable(1)
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
        self.loot = self.loottable(1)
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'cavern'


class shack(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-shack'
        self.descriptions = [
            "There is a clearing inside a forest . . . with an old cabin in the middle."
        ]
        self.loot = self.loottable(1)
        self.debug = world.debug
        self.rDebug()
        self.buildings = ['null']
        self.name = 'shack'from lib.action import act
from lib.core import *
import random

from lib.core import core


class shade(core):
    def __init__(self,name,world):
        self.name=name
        world.characterlist.append(self.name)
        self.internalID='character-shade-'+self.name
        self.world=world
        self.debug=self.world.debug
        self.rDebug()
        self.room='darkroom'
        self.hp=15
        self.act = act(self.name,self.world)
        self.age=0
        self.tickCount=random.randrange(1,5)
        self.prefer=prefer()

        if self.name=='mek':
            self.prefer.fruit='orange'
            self.week = 5
        elif self.name=='geoflib':
            self.prefer.fruit='pineapple'
            self.week = 4
    def tick(self,world):
        self.age+=1;self.tickCount+=1
        if self.tickCount==self.week: self.tickCount=1
        if self.tickCount==1:
            lines=[
                'heya, stranger!','im a shade, not a ghost. theres a difference.',
                'waddup, '+world.player.name+'?','evening!',
                'i cannae find ma lunch!', 'i like '+self.prefer.fruit+'s. my brother doesnt.',
                'ah, the darkness. so refreshing.','blegh! just got a bug in my mouth!',
                'have ya talked to my twin?','tha rats here, they make quite the racket!',
                'not a big fan of moths. how bout you?','ever been to paris?']
            self.act.speak(random.choice(lines),self.room)
        elif self.tickCount==2:
            pass # ask
        elif self.tickCount==3:
            pass #nothing/atk
        elif self.tickCount==4:
            pass #possiblemove
        
        
class darkroom(core):
    def __init__(self,world):
        self.world=world
        self.internalID='room-darkroom'
        self.debug=self.world.debug
        self.rDebug()
        world.characters.geoflib=shade('geoflib',world)
        world.characters.mek=shade('mek',world)
        self.descriptions = [
            "It's incredibly dark.",
            "There's not much here.",
            "Where'd everything go?"
        ]
        self.loot = []
        self.buildings = []
from lib.core import *
import random
from lib.biome import *
from lib.items import *
import time


class act(core):
    def __init__(self, name, world):
        self.name = name
        self.world = world
        self.internalID = self.name+'-action-library'
        self.debug = self.world.debug;self.rDebug()

    def speak(self, text, room):
        if room == self.world.player.room:
            print("[" + self.name + "] says: " + text)

    def ask(self, text, qID, room):
        if room == self.world.player.room:
            response=input("[" + self.name + "] asks: " + text + '\n')
            exec("self.world.player.rLog." + qID + "=response")


class actGod(core):

    def __init__(self, name):
        self.name = name
        self.internalID = '__ignore__'

    def speak(self,text):
        print("[" + self.name + "] : " + text)


class playerAct(core):
    def __init__(self, player, world):
        self.internalID = 'player-action-library'
        self.player = player;self.world = world
        self.array = {
            'moveTo': '.m',
            'moveAlias': 'move',
            'help:': '.h',
            'helpAlias': 'help',
            'inspect': '.i',
            'inspectAlias': 'inspect',
            'wait': '.w',
            'waitAlias': 'wait',
            'scream': 'scream',
            'pickup': '.p',
            'pickupAlias': 'pickup',
            'pickAlias': 'pick',
            'interact': '.in',
            'interactAlias': 'interact',
            'inventory': '.inv',
            'invenAlias': 'inventory',
            'invAlias': 'inv',
            'craft': '.c',
            'craftalias': 'craft',
            'build': '.b',
            'buildAlias': 'build',
            "drop": ".d",
            "dropalias": "drop"
                    }

        self.helparray = [
            'Help: Shows help screen. | .h, help',
            'Move: Move to another room. | .m, move',
            "Pickup: Pick an item up. | .p, pick, pickup",
            "Drop: Drop an item you don't want. | .d, drop",
            "Craft: Turn your items into another item. | .c, craft, .b, build",
            "Interact: Interact with an object. | .in, interact",
            'Inspect: Look at the current room and its contents. | .i, inspect',
            'Inventory: Take inventory, see what you have in your pockets. | .inv, inv, inventory',
            'Wait: Waste a moment. | .w, wait'
        ]
        self.logAnswers = {
            ".m": "(.m) Moved to location: ",
            "move": "(move) Moved to location: ",
            ".h": "(.h) Asked for Help.",
            "help": "(help) Asked for Help.",
            ".p": "(.p) Picked up item: ",
            "pick": "(pick) Picked up item: ",
            "pickup": "(pick) Picked up item: ",
            "scream": "Invoked the horrors of the night.",
            ".w": "(.w) Waited a moment.",
            "wait": "(wait) Waited a moment.",
            ".in": "(.in) Interacted with: ",
            "interact": "(interact) Interacted with: ",
            ".inv": "(.inv) Accessed Inventory.",
            "inventory": "(inventory) Accessed Inventory.",
            ".c": "(.c) Crafted:",
            ".b": "(.b) Crafted:",
            "build": "(build) Crafted:",
            "craft": "(craft) Crafted:",
            ".i": "(.i) Inspected:",
            "inspect": "(inspect) Inspected: ",
            ".d": "(.d) Dropped: ",
            "drop": "(drop) Dropped: "
        }
        self.debug = self.world.debug
        self.rDebug()

    def __log(self, message):
        log = open('save/log.txt', 'a')
        try:
            log.write("[" + str(time.ctime(time.time())) + "] " + str(self.logAnswers[message]))
        except:
            log.write("[" + str(time.ctime(time.time())) + "] " + "Unknown Command:\n")
            log.write(" - " + message)
        finally:
            log.write("\n")

    def __sublog(self, message):
        log = open('save/log.txt', 'a')
        try:
            log.write(" - " + message)
        except:
            pass
        finally:
            log.write("\n")

    def playeraction(self):
        resp = input(": ")
        found = False
        for item in self.array:
            if resp == self.array[item]:
                found = True
                self.__log(resp)
                exec("self." + item.lower() + "()")
        if found == False:
            print("That's not a possible action. Try again, or use '.h' or 'help' to see the help screen.")
            self.playeraction()

    def help(self):
        clearConsole()
        for i in self.helparray:
            print(' - ' + i)

    def helpalias(self):
        self.help()

    def moveto(self):
        clearConsole()
        self.rDebug()
        self.player.rDebug()
        self.world.rDebug()
        self.world.map.rDebug()
        print('Where would you like to go?')
        room = self.player.room
        print(room)
        if int(len(self.world.map.route[room])) < 3: # if there are less than 3 zones
            ind = len(self.world.map.route) # gets length of map
            zone = str(random.choice(self.world.zones))
            newzone = str(zone + "_" + str(ind))
            self.world.map.route[newzone] = []
            self.world.map.route[self.player.room].append(newzone)
            self.world.map.route[newzone].append(self.player.room)
            exec("self.world.map." + newzone + "=" + zone + "(self.world)")
            self.__sublog(newzone)
        for i in self.world.map.route[self.player.room]:
            print(" - [" + self.world.map.route[self.player.room].index(i) + "] " + i)

        def movetoloop(self): # <- define loop
            newloc = input(": ")
            if newloc in self.world.map.route[self.player.room]:
                self.player.room = newloc
                print("Moving to " + newloc)
            else:
                print("That's not an option, try again.")
                movetoloop(self)
        movetoloop(self) # <- run loop

        # Run inspection of room
        roomtitle = self.world.player.room
        room = getattr(self.world.map, roomtitle)
        clearConsole()
        print(random.choice(room.descriptions))

    def inspect(self):
        clearConsole()
        roomtitle = self.world.player.room
        room = getattr(self.world.map, roomtitle)
        list = []
        for i in room.loot:
            list.append(i)
        print("What do you want to inspect?")
        for i in list:
            print(" - [" + str(list.index(i)) + "] " + i)
        print(" - [R] Room")
        print(" - [i] Look at an item in your inventory (inventory)")
        print(" - [x] Cancel")
        list.append('cancel')
        list.append('room')
        list.append('inventory')
        def invLoop(self, world):
            choice = input(": ")
            if choice in world.player.inventory:
                item = getattr(world.item, choice)
                print(random.choice(item.descriptions))
                self.__sublog(item.name)
            else:
                invLoop(world)
        def loop(self, world, list):
            choice = input(": ")
            if choice in list:
                if choice == 'room':
                    print(random.choice(room.descriptions))
                    self.__sublog(self.player.room)
                elif choice == 'inventory':
                    clearConsole()
                    print("Inspect an item in inventory:")
                    self.inventory()
                    invLoop(self, world)
                elif choice == 'cancel':
                    self.__sublog('cancel')
                    pass
                else:
                    item = getattr(world.item, choice)
                    print(random.choice(item.descriptions))
                    self.__sublog(item.name)
            elif choice.upper() == "X":
                self.__sublog('cancel')
                pass
            elif choice.upper() == "R":
                print(random.choice(room.descriptions))
                self.__sublog(self.player.room)
            elif choice.upper() == "I":
                clearConsole()
                print("Inspect an item in inventory:")
                self.inventory()
                invLoop(self, world)
            elif choice.isnumeric():
                try:
                    item = getattr(world.item, list[int(choice)])
                    print(random.choice(item.descriptions))
                    self.__sublog(item.name)
                except:
                    print("That's not an option. Try again.")
                    self.__sublog('Invalid Index')
            else:
                self.__sublog('Invalid Option')
                print("That's not an option. Try again.")
                loop(self, world, list)
        loop(self, self.world, list)

    def movealias(self):
        self.moveto()

    def inspectalias(self):
        self.inspect()

    def wait(self):
        clearConsole()
        array = [
            'You stand about aimlessly.',
            'You wait as if you have all the time in the world.',
            'You waste a few minutes.'
        ]
        print(random.choice(array))

    def waitalias(self):
        self.wait()

    def scream(self):
        clearConsole()
        print("Something screams with you.")
        self.world.lexeter.achievements.append('scream')

    def pickup(self):
        clearConsole()
        roomTitle = self.world.player.room
        room = getattr(self.world.map, roomTitle)
        if hasattr(room,'loot'):
            if len(room.loot) > 0:
                print("What do you want to pick up?")
                print(' - all')
                for i in room.loot:
                    print(" - [" + str(room.loot.index(i)) + "] " + getattr(self.world.item, i).name)
                print(" - [x] Cancel")
                choice = input(": ")

                def loop(choice, room):
                    if choice == 'all':
                        self.__sublog('all')
                        for i in room.loot:
                            print("You picked up " + getattr(self.world.item, i).name)
                            self.__sublog(i)
                        self.player.inventory = self.player.inventory + room.loot
                        room.loot = []
                    elif choice in 'cancel' or choice.upper() == 'X':
                        self.__sublog('cancel')
                    elif choice in room.loot:
                        room.loot.remove(choice)
                        self.player.inventory.append(choice)
                        print("You picked up " + choice)
                        self.__sublog(choice)
                    elif choice.isnumeric():
                        self.player.inventory.append(room.loot[int(choice)])
                        print("You picked up " + room.loot[int(choice)])
                        self.__sublog(room.loot[int(choice)])
                        room.loot.remove(room.loot[int(choice)])
                    else:
                        self.__sublog('Invalid Selection')
                        print("That's not an option, try again.")
                        loop(input(": "),room)
                loop(choice,room)
            else:
                self.__sublog('Nothing to pick up')
                print("There's nothing here.")
        else:
            self.__sublog('Nothing to pick up')
            print("There's nothing here.")

    def pickupalias(self):
        self.pickup()

    def pickalias(self):
        self.pickup()

    def interact(self):
        print("This Function is not available right now. Try again later.")
        self.__sublog("notavailable")

    def interactalias(self):
        self.interact()

    def inventory(self):
        clearConsole()
        print("You have:")
        inv = self.world.player.inventory
        itemList = {}
        itemList.update(self.world.item.dict)
        for i in inv:
            itemList[i] += 1
        popList = []
        for i in itemList:
            if itemList[i] == 0:
                popList.append(i)
        for i in popList:
            itemList.pop(i)
        for i in itemList:
            print(" - " + str(itemList[i]) + "x " + getattr(self.world.item, i).name)

    def invenalias(self):
        self.inventory()

    def invalias(self):
        self.inventory()

    def craft(self):
        craftables = []
        for i in self.world.recipes.full:
            if all(x in self.player.inventory for x in getattr(self.world.recipes, i).ingredients) and getattr(self.world.recipes, i).station in getattr(self.world.map, self.player.room).buildings:
                craftables.append(i)
        if len(craftables) == 0:
            print("You are unable to craft anything.")
            self.__sublog('Unable to craft')
        else:
            print("What would you like to craft?")
            for i in craftables:
                print(" - [" + str(craftables.index(i)) + "] " + i)
            print(" - [x] Cancel")

            def loop(self, craftables):
                choice = input(": ")
                if choice in craftables:
                    self.player.inventory.append(choice)
                    for i in getattr(self.world.recipes, choice).ingredients:
                        self.player.inventory.remove(i)
                    print("You crafted " + getattr(self.world.item, choice).name + "!")
                    self.__sublog(getattr(self.world.item, choice).name)
                elif choice.upper() == 'X' or choice.upper() == "CANCEL":
                    self.__sublog('Cancel')
                elif choice.isnumeric():
                    self.player.inventory.append(craftables[int(choice)])
                    for i in getattr(self.world.recipes, craftables[int(choice)]).ingredients:
                        self.player.inventory.remove(i)
                    print("You crafted " + getattr(self.world.item, craftables[int(choice)]).name + "!")
                    self.__sublog(getattr(self.world.item, craftables[int(choice)]).name)
                else:
                    print("That's not an option, sorry.")
                    loop(self, craftables)
            loop(self, craftables)


    def craftalias(self):
        self.craft()

    def build(self):
        craftables = []
        for i in self.world.constructs.full:
            if all(x in self.player.inventory for x in getattr(self.world.constructs, i).ingredients):
                craftables.append(i)
        if len(craftables) == 0:
            self.__sublog('Unable to build')
            print("You are unable to build anything.")
        else:
            print("What would you like to build?")
            for i in craftables:
                print(" - [" + str(craftables.index(i)) + "] " + i)
            print(" - [x] Cancel")

            def loop(self, craftables):
                choice = input(": ")
                if choice in craftables:
                    getattr(self.world.map,self.player.room).buildings.append(choice)
                    for i in getattr(self.world.constructs, choice).ingredients:
                        self.player.inventory.remove(i)
                    print("You built a " + getattr(self.world.constructs, choice).name + "!")
                    self.__sublog(getattr(self.world.constructs, choice).name)
                elif choice.upper() == 'X' or choice.upper() == "CANCEL":
                    self.__sublog('Cancel')
                elif choice.isnumeric():
                    getattr(self.world.map,self.player.room).buildings.append(choice)
                    for i in getattr(self.world.constructs, craftables[int(choice)]).ingredients:
                        self.player.inventory.remove(i)
                    print("You built a " + getattr(self.world.constructs, craftables[int(choice)]).name + "!")
                    self.__sublog(getattr(self.world.constructs, craftables[int(choice)]).name)
                else:
                    loop(self, craftables)

            loop(self, craftables)

    def buildalias(self):
        self.build()

    def drop(self):
        pass

    def dropalias(self):
        self.drop()from lib.core import *


class Stone(core):
    def __init__(self, debug):
        self.internalID = 'item-stone'
        self.name = 'stone'
        self.quality = 0
        self.descriptions = [
            "Well, it's a rock. What did you expect?",
            "It's a grey stone.",
            "Looks like it might be a chunk of granite.",
            "It might not be granite after all."
        ]
        self.debug = debug
        self.rDebug


class Branch(core):
    def __init__(self, debug):
        self.internalID = 'item-branch'
        self.name = 'branch'
        self.quality = 0
        self.descriptions = [
            "It's just a stick, but it's cool nonetheless.",
            "Why have a sword when you can have this stick?",
            "En garde!",
            "You can face any danger with this, as long as that danger is largely imaginary.",
            "You don't have a dog, unfortunately.",
            "Where's a dog when you need one?",
            "It's a muddy twig."
        ]
        self.debug = debug
        self.rDebug


class Scrapmetal(core):
    def __init__(self, debug):
        self.internalID = 'item-scrapmetal'
        self.name = 'metal scrap'
        self.quality = 0
        self.descriptions = [
            "Several pieces of metal. A hallmark of many survival games.",
            "You're pretty sure none of this is actually useable without the correct tools and training, but somehow things will work out. They always do.",
            "How do you use this?",
            "Don't cut yourself, it's sharp.",
            "Maybe if you found a way to melt it, you could . . . never mind, you're not a blacksmith.",
            "A bunch of junk from various metal things.",
            "Bottlecaps, wires, a doorknob and a steel plate glove that is conveniently dented in a way that you can't wear it.",
            "Why in the world is this here?"
        ]
        self.debug = debug
        self.rDebug


class Egg(core):
    def __init__(self, debug):
        self.internalID = 'item-egg'
        self.name = 'egg'
        self.quality = 2
        self.descriptions = [
            "It's an egg.",
            "Scrambled, overeasy, sunny side up, hardboiled . . .",
            "It probably won't hatch into anything, it looks just like an average chicken egg from the supermarket.",
            "Breakfast is served! Well, once you find a frying pan.",
            "Tasty."
        ]
        self.debug = debug
        self.rDebug


class Potato(core):
    def __init__(self,debug):
        self.internalID = 'item-potato'
        self.name = 'potato'
        self.quality = 2
        self.descriptions = [
            "Boil it, mash it, stick it in a stew.",
            "The Irish lived on these for a while.",
            "A Russian's favorite beverage. Well, almost.",
            "All the nutrients in one spud.",
            "Idaho grown, of course.",
            "So many possibilities in one small package."
        ]
        self.debug = debug
        self.rDebug


class Shinystone(core):
    def __init__(self,debug):
        self.internalID = 'item-shinystone'
        self.name = 'shiny stone'
        self.quality = 1
        self.descriptions = [
            "It's an oddly shiny stone. Interesting, but not worth much.",
            "Sparkly.",
            "It's so close to mundane, and yet so far."
        ]
        self.debug = debug
        self.rDebug()


class Diamond(core):
    def __init__(self,debug):
        self.internalID = 'item-diamond'
        self.name = 'diamond'
        self.quality = 3
        self.descriptions = [
            "You cannot afford ford . . . this overpriced rock.",
            "There's no way you can make tools out of this.",
            "Hilariously valuable, for almost no reason.",
            "It's not rare, really.",
            "Or is it cubic zirconia?",
            "Just a thumb-sized chunk of diamond.",
            "It's a lot larger than most you've seen."
        ]
        self.debug = debug
        self.rDebug()


class Ruby(core):
    def __init__(self,debug):
        self.internalID = 'item-ruby'
        self.name = 'ruby'
        self.quality = 3
        self.descriptions = [
            "A blood red jewel. ",
            "This would go really good with gold on like, a necklace or something.",
            "Evil magic scepter material.",
            "It's the color of, well, rubies."
        ]
        self.debug = debug
        self.rDebug()


class Sapphire(core):
    def __init__(self,debug):
        self.internalID = 'item-sapphire'
        self.name = 'sapphire'
        self.quality = 3
        self.descriptions = [
            "A deep, deep blue stone.",
            "A refreshingly blue color.",
            "Ice magic, baby!"
        ]
        self.debug = debug
        self.rDebug()


class Emerald(core):
    def __init__(self,debug):
        self.internalID = 'item-emerald'
        self.name = 'emerald'
        self.quality = 3
        self.descriptions = [
            "Hmmmmmmm . . .",
            "If it were cut, it'd likely be a square.",
            "A beautiful shade of green.",
            "It's a big one.",
            "You wonder what this'd go for."
        ]
        self.debug = debug
        self.rDebug()


class Opal(core):
    def __init__(self,debug):
        self.internalID = 'item-opal'
        self.name = 'opal'
        self.quality = 3
        self.descriptions = [
            "Shiny!",
            "It's a kaleidoscope, but a rock!",
            "All the colors in one stone."
        ]
        self.debug = debug
        self.rDebug()


class Twine(core):
    def __init__(self,debug):
        self.internalID = 'item-twine'
        self.name = 'twine'
        self.quality = 1
        self.descriptions = [
            "A simple length of string."
        ]
        self.debug = debug
        self.rDebug()


class Excalibur(core):
    def __init__(self,debug):
        self.internalID = 'item-excalibur'
        self.name = 'Excalibur'
        self.quality = 4
        self.descriptions = [
            "An arbitrarily powerful sword.",
            "Did this come from the stone, or the lake?",
            "It feels like you don't deserve to hold it."
        ]
        self.debug = debug
        self.rDebug()


class Crudespear(core):
    def __init__(self,debug):
        self.internalID = 'item-crudespear'
        self.name = 'crude spear'
        self.quality = 1
        self.descriptions = [
            "An incredibly simple weapon.",
            "It's like a sharpened stick, but sharper."
        ]
        self.debug = debug
        self.rDebug()


class Slingshot(core):
    def __init__(self, debug):
        self.internalID = 'item-slingshot'
        self.name = 'slingshot'
        self.quality = 1
        self.descriptions = [
            "Pew Pew!",
            "What's the shiniest thing you can stick in it?",
            "Some guy is gonna get shot . . ."
        ]
        self.debug = debug
        self.rDebug()


class Breakfast(core):
    def __init__(self, debug):
        self.internalID = 'item-breakfast'
        self.name = 'eggs and hashbrowns'
        self.quality = 1
        self.descriptions = [
            "It's breakfast, all right.",
            "Got any boy scout pepper?",
            "It looks . . . edible."
        ]
        self.debug = debug
        self.rDebug()


class Mud(core):
    def __init__(self, debug):
        self.internalID = 'item-mud'
        self.name = 'fistful of mud'
        self.quality = 0
        self.descriptions = [
            "Muddy."
        ]
        self.debug = debug
        self.rDebug()


class Brick(core):
    def __init__(self, debug):
        self.internalID = 'item-brick'
        self.name = 'brick'
        self.quality = 0
        self.descriptions = [
            "Don't throw it at people.",
            "What kind of brick?",
            "A brick is just a brick."
        ]
        self.debug = debug
        self.rDebug()


class Clay(core):
    def __init__(self, debug):
        self.internalID = 'item-clay'
        self.name = 'ball of clay'
        self.quality = 0
        self.descriptions = [
            "Why is it so darn hard to find?",
            "you could probably make something with this.",
            "The possibilities are nearly endless.",
            "Reality can be whatever you want.",
            "Make a snake!"
        ]
        self.debug = debug
        self.rDebug()


class Charcoal(core):
    def __init__(self, debug):
        self.internalID = 'item-charcoal'
        self.name = 'hunk of charcoal'
        self.quality = 0
        self.descriptions = [
            "You could draw with it!",
            "Because you couldn't find any coal.",
            "It's wood that was cooked so that it can be used to cook other things."
        ]
        self.debug = debug
        self.rDebug()


class Meat(core):
    def __init__(self, debug):
        self.internalID = 'item-meat'
        self.name = 'raw meat'
        self.quality = 1
        self.descriptions = [
            "Wash your hands.",
            "It's flippin RAW.",
            "Cook it first."
        ]
        self.debug = debug
        self.rDebug()


class Wood(core):
    def __init__(self, debug):
        self.internalID = 'item-wood'
        self.name = 'chunk of wood'
        self.quality = 1
        self.descriptions = [
            "Watch out for splinters.",
            "The ever-important core of survival games."
        ]
        self.debug = debug
        self.rDebug()


class Dinowhistle(core):
    def __init__(self, debug):
        self.internalID = 'item-dinowhistle'
        self.name = 'dinosaur whistle'
        self.quality = 4
        self.descriptions = [
            "Tame those dinosaurs."
        ]
        self.debug = debug
        self.rDebug()


class Berry(core):
    def __init__(self, debug):
        self.internalID = 'item-berry'
        self.name = 'berry'
        self.quality = 2
        self.descriptions = [
            "An incredibly generic berry."
        ]
        self.debug = debug
        self.rDebug()


class Axe(core):
    def __init__(self, debug):
        self.internalID = 'item-axe'
        self.name = 'axe'
        self.quality = 5
        self.descriptions = [
            "Chop Chop!",
            "Heeeeere's Johnny!",
            "Paul Bunyan's favorite tool.",
            "And my bow!"
        ]
        self.debug = debug
        self.rDebug()


class Wrench(core):
    def __init__(self, debug):
        self.internalID = 'item-wrench'
        self.name = 'wrench'
        self.quality = 3
        self.descriptions = [
            "Can we fix it?",
            "At least it's not a hammer."
        ]
        self.debug = debug
        self.rDebug()


class Ironore(core):
    def __init__(self, debug):
        self.internalID = 'item-ironore'
        self.name = 'iron ore'
        self.quality = 1
        self.descriptions = [
            "Good ol' bog iron ore."
        ]
        self.debug = debug
        self.rDebug()


class Molteniron(core):
    def __init__(self, debug):
        self.internalID = 'item-molteniron'
        self.name = 'molten iron'
        self.quality = 1
        self.descriptions = [
            "You really shouldn't be holding liquid metal.",
            "Hot! Hot! Hot!",
            "Hot enough to, well, burn your skin off."
        ]
        self.debug = debug
        self.rDebug()


class Snailshell(core):
    def __init__(self, debug):
        self.internalID = 'item-snailshell'
        self.name = 'snailshell'
        self.quality = 0
        self.descriptions = [
            "It's the shell of a snail."
        ]
        self.debug = debug
        self.rDebug()


class Toyplane(core):
    def __init__(self, debug):
        self.internalID = 'item-toyplane'
        self.name = 'toy plane'
        self.quality = 0
        self.descriptions = [
            "It's a small toy plane."
        ]
        self.debug = debug
        self.rDebug()


class Spatula(core):
    def __init__(self, debug):
        self.internalID = 'item-spatula'
        self.name = 'spatula'
        self.quality = 0
        self.descriptions = [
            "It's a latch-a-splat.",
            "Spatoola."
        ]
        self.debug = debug
        self.rDebug()


class Sunglasses(core):
    def __init__(self, debug):
        self.internalID = 'item-sunglasses'
        self.name = 'sunglasses'
        self.quality = 0
        self.descriptions = [
            "I wear them at night.",
            "I'm not just cool, I'm crispy.",
            "How's it going, hotstuff?"
        ]
        self.debug = debug
        self.rDebug()


class Item(core):
    def __init__(self,world):
        self.debug = world.debug
        self.internalID = 'library-items'
        self.rDebug()
        self.qualities = {
            0 : "trash",
            1 : "common",
            2 : "useful",
            3 : "treasure",
            4 : "impossible",
            5 : "crafted"
        }
        self.trash = [
            'stone',
            'branch',
            'scrapmetal',
            'twine',
            'brick',
            'mud',
            'clay',
            'snailshell',
            'toyplane',
            'spatula',
            'sunglasses'
        ]
        self.common = [
            'shinystone',
            'branch',
            'berry',
            'ironore'
        ]
        self.useful = [
            'egg',
            'potato',
            'twine'
        ]
        self.treasure = [
            'diamond',
            'ruby',
            'sapphire',
            'emerald',
            'opal',
            'wrench'
        ]
        self.impossible = [
            'excalibur'
        ]
        self.crafted = [
            'crudespear',
            'slingshot',
            'breakfast',
            'charcoal',
            'brick',
            'axe',
            'molteniron'
        ]
        self.complexfinding = [
            'meat',
            'wood',
            'dinowhistle'
        ]
        self.full = self.trash + self.common + self.useful + self.treasure + self.impossible

        # Generate dictionary for other uses
        self.dict = {}
        for i in self.full:
            self.dict[i] = 0
        for i in self.crafted:
            self.dict[i] = 0

        self.stone = Stone(self.debug)
        self.branch = Branch(self.debug)
        self.scrapmetal = Scrapmetal(self.debug)
        self.egg = Egg(self.debug)
        self.shinystone = Shinystone(self.debug)
        self.diamond = Diamond(self.debug)
        self.excalibur = Excalibur(self.debug)
        self.ruby = Ruby(self.debug)
        self.sapphire = Sapphire(self.debug)
        self.emerald = Emerald(self.debug)
        self.opal = Opal(self.debug)
        self.potato = Potato(self.debug)
        self.twine = Twine(self.debug)
        self.crudespear = Crudespear(self.debug)
        self.slingshot = Slingshot(self.debug)
        self.breakfast = Breakfast(self.debug)
        self.brick = Brick(self.debug)
        self.mud = Mud(self.debug)
        self.clay = Clay(self.debug)
        self.meat = Meat(self.debug)
        self.charcoal = Charcoal(self.debug)
        self.wood = Wood(self.debug)
        self.dinowhistle = Dinowhistle(self.debug)
        self.berry = Berry(self.debug)
        self.axe = Axe(self.debug)
        self.ironore = Ironore(self.debug)
        self.molteniron = Molteniron(self.debug)
        self.wrench = Wrench(self.debug)
        self.snailshell = Snailshell(self.debug)
        self.toyplane = Toyplane(self.debug)
        self.spatula = Spatula(self.debug)
        self.sunglasses = Sunglasses(self.debug)


class CrudespearRecipe(core):
    def __init__(self, debug):
        self.internalID = 'recipe-crudespear'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'metalscrap',
            'branch',
            'twine'
        ]
        self.station = 'null'
        self.result = 'crudespear'


class SlingshotRecipe(core):
    def __init__(self, debug):
        self.internalID = 'recipe-slingshot'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'branch',
            'twine'
        ]
        self.station = 'null'
        self.result = 'slingshot'


class BreakfastRecipe(core):
    def __init__(self, debug):
        self.internalID = 'recipe-breakfast'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'egg',
            'potato'
        ]
        self.station = 'campfire'
        self.result = 'breakfast'


class BrickRecipe(core):
    def __init__(self, debug):
        self.internalID = 'recipe-brick'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'clay'
        ]
        self.station = 'kiln'
        self.result = 'brick'

class AxeRecipe(core):
    def __init__(self, debug):
        self.internalID = 'recipe-axe'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'branch',
            'molteniron'
        ]
        self.station = 'anvil'
        self.result = 'axe'


class CharcoalRecipe(core):
    def __init__(self, debug):
        self.internalID = 'recipe-charcoal'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'wood'
        ]
        self.station = 'kiln'
        self.result = 'charcoal'


class MoltenironRecipe(core):
    def __init__(self, debug):
        self.internalID = 'recipe-charcoal'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'ironore',
            'charcoal'
        ]
        self.station = 'smelter'
        self.result = 'molteniron'


class Recipes(core):
    def __init__(self, lexeter):
        self.lexeter = lexeter
        self.debug = self.lexeter.debug
        self.internalID = 'library-crafting'
        self.rDebug()
        self.crudespear = CrudespearRecipe(self.debug)
        self.slingshot = SlingshotRecipe(self.debug)
        self.breakfast = BreakfastRecipe(self.debug)
        self.brick = BrickRecipe(self.debug)
        self.charcoal = CharcoalRecipe(self.debug)
        self.axe = AxeRecipe(self.debug)
        self.molteniron = MoltenironRecipe(self.debug)

        self.full = [
            'crudespear',
            'slingshot',
            'breakfast',
            'brick',
            'charcoal',
            'axe',
            'molteniron'
        ]


class Campfire(core):
    def __init__(self, debug):
        self.internalID = 'construct-campfire'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'branch',
            'stone'
        ]
        self.result = 'campfire'
        self.name = 'campfire'


class Kiln(core):
    def __init__(self, debug):
        self.internalID = 'construct-kiln'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'brick',
            'mud',
            'branch'
        ]
        self.result = 'kiln'
        self.name = 'kiln'


class Furnace(core):
    def __init__(self, debug):
        self.internalID = 'construct-furnace'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'brick',
            'mud',
            'stone',
            'charcoal'
        ]
        self.result = 'furnace'
        self.name = 'furnace'


class Smelter(core):
    def __init__(self, debug):
        self.internalID = 'construct-smelter'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'brick',
            'mud',
            'stone',
            'charcoal',
            'clay'
        ]
        self.result = 'smelter'
        self.name = 'smelter'


class Anvil(core):
    def __init__(self, debug):
        self.internalID = 'construct-anvil'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'molteniron',
            'stone',
            'shinystone'
        ]
        self.result = 'anvil'
        self.name = 'anvil'


class Constructs(core):
    def __init__(self, world):
        self.world = world
        self.debug = self.world.debug
        self.internalID = 'library-construction'
        self.rDebug()
        self.campfire = Campfire(self.debug)
        self.kiln = Kiln(self.debug)
        self.furnace = Furnace(self.debug)
        self.smelter = Smelter(self.debug)
        self.anvil = Anvil(self.debug)
        self.full = [
            'campfire',
            'kiln',
            'furnace',
            'smelter',
            'anvil'
        ]
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
        self.player.room='darkroom'

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
        self.world = world(self.instances, self.them, self.zones, self.debug, self.item, self.recipes, self.constructs, self)

if __name__ == "__main__":
    from lib.player import *
    from lib.darkroom import *
    from lib.action import *
    from lib.core import *
    lexeter = lex_init()
    tick(lexeter, lexeter.world)
