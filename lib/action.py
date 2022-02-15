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
            'buildAlias': 'build'
                    }

        self.helparray = [
            'Help: Shows help screen. | .h, help',
            'Move: Move to another room. | .m, move',
            "Pickup: Pick an item up. | .p, pick, pickup",
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
            "inspect": "(inspect) Inspected: "
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
            print(" - " + i)

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
                        room.loot.remove(room.loot[int(choice)])
                        self.player.inventory.append(room.loot[int(choice)])
                        print("You picked up " + room.loot[int(choice)])
                        self.__sublog(room.loot[int(choice)])
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
        else:
            print("What would you like to craft?")
            for i in craftables:
                print(" - " + i)

            def loop(self, craftables):
                choice = input(": ")
                if choice in craftables:
                    self.player.inventory.append(choice)
                    for i in getattr(self.world.recipes, choice).ingredients:
                        self.player.inventory.remove(i)
                    print("You crafted " + getattr(self.world.item, choice).name + "!")
                    self.__sublog(getattr(self.world.item, choice).name)
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
            print("You are unable to build anything.")
        else:
            print("What would you like to build?")
            for i in craftables:
                print(" - " + i)

            def loop(self, craftables):
                choice = input(": ")
                if choice in craftables:
                    getattr(self.world.map,self.player.room).buildings.append(choice)
                    #exec("getattr(self.world.map, self.player.room)." + choice + " = choice(False)")
                    for i in getattr(self.world.constructs, choice).ingredients:
                        self.player.inventory.remove(i)
                    print("You built a " + getattr(self.world.constructs, choice).name + "!")
                    self.__sublog(getattr(self.world.constructs, choice).name)
                else:
                    loop(self, craftables)

            loop(self, craftables)

    def buildalias(self):
        self.build()