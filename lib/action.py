from lib.core import *
import random
from lib.biome import *


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
            'invAlias': 'inv'
                    }

        self.helparray = [
            'Help: Shows help screen. | .h, help',
            'Move: Move to another room. | .m, move',
            "Pickup: Pick an item up. | .p, pick, pickup",
            "Interact: Interact with an object. | .in, interact",
            'Inspect: Look at the current room and its contents. | .i, inspect',
            'Inventory: Take inventory, see what you have in your pockets. | .inv, inv, inventory',
            'Wait: Waste a moment. | .w, wait'
        ]
        self.debug = self.world.debug
        self.rDebug()

    def playeraction(self):
        resp = input(": ")
        found = False
        for item in self.array:
            if resp == self.array[item]:
                found = True
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
        list = ['room', 'inventory']
        for i in room.loot:
            list.append(i)
        print("What do you want to inspect?")
        for i in list:
            print(" - " + i)
        def invLoop(world):
            choice = input(": ")
            if choice in world.player.inventory:
                item = getattr(world.item, choice)
                print(random.choice(item.descriptions))
            else:
                invLoop(world)
        def loop(self,world):
            choice = input(": ")
            if choice in list:
                if choice == 'room':
                    print(random.choice(room.descriptions))
                elif choice == 'inventory':
                    clearConsole()
                    print("Inspect an item in inventory:")
                    self.inventory()
                    invLoop(world)
                else:
                    item = getattr(world.item, choice)
                    print(random.choice(item.descriptions))
            else:
                print("That's not an option. Try again.")
                loop(world)
        loop(self, self.world)

    def movealias(self):
        self.moveTo()

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
                    print(" - " + i)
                choice = input(": ")

                def loop(choice, room):
                    if choice == 'all':
                        for i in room.loot:
                            print("You picked up " + i)
                        self.player.inventory = self.player.inventory + room.loot
                        room.loot = []
                    elif choice in room.loot:
                        room.loot.remove(choice)
                        self.player.inventory.append(choice)
                        print("You picked up " + choice)
                    else:
                        print("That's not an option, try again.")
                        loop(input(": "),room)
                loop(choice,room)
            else:
                print("There's nothing here.")
        else:
            print("There's nothing here.")

    def pickupalias(self):
        self.pickup()

    def pickalias(self):
        self.pickup()

    def interact(self):
        pass

    def interactalias(self):
        self.interact()

    def inventory(self):
        clearConsole()
        print("You have:")
        print(self.world.player.inventory)
        inv = self.world.player.inventory
        itemList = []#{} + self.world.item.dict
        for i in inv:
            count = inv.count(i)
            itemList.append(" - " + str(count) + " " + i)
        for n in itemList:
            print(n)
            for x in itemList:
                if x == n:
                    itemList.remove(x)

    def invenalias(self):
        self.inventory()

    def invalias(self):
        self.inventory()