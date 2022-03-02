try:
    from lib.items import *
except ModuleNotFoundError:
    log = open('save/log.txt', 'a')
    print("Warning! action module unable to find items module.")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    log.write("!! Action Module unable to find Items Module !!")
    log.close()
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()
except ImportError:
    log = open('save/log.txt', 'a')
    print("Warning! action module had issues importing items module.")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    log.write("!! Action Module issues importing Items Module !!")
    log.close()
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()

try:
    import time
except ModuleNotFoundError:
    log = open('save/log.txt', 'a')
    print("Warning! action module unable to find time module.")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    print("Time is one of Python's built-in modules. Consider reinstalling Python.")
    log.write("!! Action Module unable to find Builtin Time Module !!")
    log.close()
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()
except ImportError:
    log = open('save/log.txt', 'a')
    print("Warning! action module had issues importing time module.")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    print("Time is one of Python's built-in modules. Consider reinstalling Python.")
    log.write("!! Action Module unable to import Builtin Time Module !!")
    log.close()
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()


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
            "drop": "(drop) Dropped: ",
            "unfound": "Unfound Command"
        }
        self.debug = self.world.debug
        self.rDebug()

    def __log(self, message):
        try:
            log = open('save/log.txt', 'a')
        except:
            print("Warning: Unable to write to log file.")
            self.error('write-log', '__log/open-log')

        try:
            log.write("[" + str(time.ctime(time.time())) + "] " + str(self.logAnswers[message]))
        except:
            log.write("[" + str(time.ctime(time.time())) + "] " + "Unknown Command:\n")
            log.write(" - " + message)
        finally:
            log.write("\n")
            log.close()

    def __sublog(self, message):

        # Open log file
        try:
            log = open('save/log.txt', 'a')
        except:
            print("Warning: Unable to write to log file.")
            self.error('write-log', '__sublog/open-log')


        # Write message to log file
        try:
            log.write(" - " + message)
            log.write("\n")
        except:
            print("Warning: Unable to write to log file.")
            self.error('write-log', '__sublog/write-context')

        log.close()

    def __errorlog(self, message):
        try:
            log = open('save/log.txt', 'a')
        except:
            print("Warning: Unable to write to log file.")
            self.error('write-log', '__errorlog/open-log')

        try:
            log.write("![" + message + "]\n")
        except:
            print("Warning: Unable to write to log file.")
            self.error('write-log', '__errorlog/write-log')

        log.close()

    def playeraction(self, game):
        resp = input(": ")
        found = False

        try:
            for item in self.array:
                if resp == self.array[item]:
                    found = True
                    self.__log(resp)

                    if not self.world.lexeter.crafting and resp in ['craft', '.c', 'c']:
                        self.__sublog('no such thing')
                        print("There is no such thing as crafting.")
                    else:
                        try:
                            getattr(self, item.lower())(game)
                        except:
                            print("Error! Issue running command.")
                            self.error('player-action-command', 'actloop/error-executing-command', resp)
                            self.__errorlog('Issue running command, player-action-command, actloop/error-executing-command, ' + resp)

            if found == False:
                print("That's not a possible action. Try again, or use '.h' or 'help' to see the help screen.")
                self.__log('unfound')
                self.playeraction()

        except:
            print("That's not a possible action. Try again, or use '.h' or 'help' to see the help screen.")
            self.error('player-action-command', 'actloop/unknown-command-error', resp)
            self.__errorlog('Issue finding command, player-action-command, actloop/unkown-command-error, ' + resp)
            self.playeraction()

    def help(self, game):
        clearConsole()
        for i in self.helparray:
            print(' - ' + i)

    def helpalias(self, game):
        self.help(game)

    def moveto(self, game):
        clearConsole()
        self.rDebug()
        self.player.rDebug()
        self.world.rDebug()
        self.world.map.rDebug()
        print('Where would you like to go?')
        room = self.player.room
        print(room)

        try:
            if int(len(self.world.map.route[room])) < 3:
                ind = len(self.world.map.route)
                zone = str(random.choice(self.world.zones))
                newzone = str(zone + "_" + str(ind))
                self.world.map.route[newzone] = []
                self.world.map.route[self.player.room].append(newzone)
                self.world.map.route[newzone].append(self.player.room)
                exec("self.world.map." + newzone + "=" + zone + "(self.world)")
                self.__sublog('created ' + newzone)
        except:
            self.__errorlog('Issue creating new zone, player-action-move-createzone, movecommand/createzone')
            self.error('player-action-move-createzone', 'movecommand/createzone')

        for i in self.world.map.route[self.player.room]:
            print(" - [" + str(self.world.map.route[self.player.room].index(i)) + "] " + i)
        print(" - [x] Cancel")

        def movetoloop(self): # <- define loop
            newloc = input(": ")
            if newloc in self.world.map.route[self.player.room]:
                self.player.room = newloc
                print("Moving to " + newloc)
                self.__sublog(newloc)
            elif newloc.upper() == 'X' or newloc.upper() == 'CANCEL':
                self.__sublog('cancel')
            elif newloc.isnumeric():
                room = self.world.map.route[self.player.room][int(newloc)]
                self.player.room = room
                print("Moving to " + room)
                self.__sublog(room)
            else:
                print("That's not an option, try again.")
                self.__sublog("impossible option: " + newloc)
                movetoloop(self)

        try:
            movetoloop(self)
        except:
            self.__errorlog('Issue moving between zones, player-action-move-move, movecommand/move')
            self.error('player-action-move-move', 'movecommand/move')

        # Run inspection of room
        roomtitle = self.world.player.room
        room = getattr(self.world.map, roomtitle)
        clearConsole()
        print(random.choice(room.descriptions))

    def inspect(self, game):
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

    def movealias(self, game):
        self.moveto(game)

    def inspectalias(self, game):
        self.inspect(game)

    def wait(self, game):
        clearConsole()
        array = [
            'You stand about aimlessly.',
            'You wait as if you have all the time in the world.',
            'You waste a few minutes.'
        ]
        print(random.choice(array))

    def waitalias(self, game):
        self.wait(game)

    def scream(self, game):
        clearConsole()
        if self.world.lexeter.sound:
            print("Something screams with you.")
            if 'scream' not in self.world.lexeter.achievements:
                self.world.lexeter.achievements.append('scream')
                print("~~ Achievement: Scream into the darkness")
        else:
            if 'nomouthtoscream' not in self.world.lexeter.achievements:
                self.world.lexeter.achievements.append('nomouthtoscream')
                print("~~ Achievement: I have no mouth, and I must scream")

    def pickup(self, game):
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

    def pickupalias(self, game):
        self.pickup(game)

    def pickalias(self, game):
        self.pickup(game)

    def interact(self, game):
        print("This Function is not available right now. Try again later.")
        self.__sublog("notavailable")

    def interactalias(self, game):
        self.interact(game)

    def inventory(self, game):
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

    def invenalias(self, game):
        self.inventory(game)

    def invalias(self, game):
        self.inventory(game)

    def craft(self, game):
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


    def craftalias(self, game):
        self.craft(game)

    def build(self, game):
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

    def buildalias(self, game):
        self.build(game)

    def drop(self, game):
        pass

    def dropalias(self, game):
        self.drop(game)