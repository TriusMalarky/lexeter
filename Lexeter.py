# Build File, use other lexeter for testing
import pickle
import os
import inspect
import random

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


class core():  # <-- core class, all other classes should inherit this
    def __init__(self):
        self.internalID = 'core-parent'

    def __str__(self):  # <-- core function for displaying all relevant members of a given class instance
        attr = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        ar = []
        for _ in [a for a in attr if not (a[0].startswith('__')) and not (a[0].startswith('internal'))]:
            ar.append(_)
        return str(ar)

    def rDebug(self):
        if self.debug:
            print("Debug: " + self.internalID)
            print(" ++ " + str(self))


class prefer(core):  # <-- dummy class
    def __init(self):
        self.internalID = 'character-preference'


def save(lexeter):
    lexMem = inspect.getmembers(lexeter, lambda a: not (inspect.isroutine(
        a)))  # <-- Not sure if this is necessary, the save function only worked right after I added this though . . .
    loc = open('save\\lexeter.txt', 'wb')
    pickle.dump(lexeter, loc)
    # Unused function for saving each individual class instance. Ignore.
    # for lexMemEntry in [a for a in lexMem if not(a[0].startswith('__') and not (a[0].startswith('internal'))]:
    # loc=open('save\\'++'.txt','wb')
    # pickle.dump(lexMemEntry,loc)


def load():
    savefile = open('save\\lexeter.txt', 'rb')  # <-- open save file in readable binary for pickle
    return pickle.load(savefile)  # <-- returning loaded save state class instance


def lex_init():
    if os.path.exists('save\\lexeter.txt'):
        return load()  # <-- returning the loaded save state class instance
    else:
        open('save\\lexeter.txt', 'w')
        from lib.player import lexeter
        lexet = lexeter()
        save(lexet)  # <-- saving the save state instance
        return lexet  # <-- returning the newly created save state


def tick(lexeter, world):
    for _ in world.characterlist:
        exec('world.characters.' + _.lower() + '.tick(world)')
    world.player.act.playeraction()
    save(lexeter)  # save on every tick
    tick(lexeter, world)

class corebiome(core):
    def __init__(self):
        self.internalID = 'biome-core'
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

class cave(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-cave'
        self.descriptions = [
            "Drip. Drip. Drip. It's a cave, all right."
        ]
        self.loot = self.loottable(1)
        self.debug = world.debug
        self.rDebug()

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

class act(core):
    def __init__(self, name, world):
        self.name=name
        self.world=world
        self.internalID=self.name+'-action-library'
        self.debug=self.world.debug;self.rDebug()
    def speak(self,text,room):
        if room == self.world.player.room:
            print("["+self.name+"] says: "+text)
    def ask(self,text,qID,room):
        if room == self.world.player.room:
            response=input("["+self.name+"] asks: "+text+'\n')
            exec("self.world.player.rLog."+qID+"=response")

class actGod(core):
    def __init__(self,name):
        self.name=name
        self.internalID='__ignore__'
    def speak(self,text):
        print("["+self.name+"] : "+text)

class playerAct(core):
    def __init__(self,player,world):
        self.internalID = 'player-action-library'
        self.player=player;self.world=world
        self.array = {
            'moveTo': '.m',
            'moveAlias':'move',
            'help':'.h',
            'helpAlias': 'help',
            'inspect':'.i',
            'inspectAlias':'inspect',
            'wait':'.w',
            'waitAlias':'wait',
            'scream':'scream',
            'pickup':'.p',
            'pickupAlias':'pickup',
            'pickAlias':'pick',
            'interact':'.in',
            'interactAlias':'interact',
            'inventory':'.inv',
            'invenAlias':'inventory',
            'invAlias':'inv'
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
        self.debug=self.world.debug;self.rDebug()
    def playeraction(self):
        resp = input(": ")
        found = False
        for item in self.array:
            if resp == self.array[item]:
                found=True
                exec("self." + item + "()")
        if found == False:
            print("That's not a possible action. Try again, or use '.h' or 'help' to see the help screen.")
            self.playeraction()
    def help(self):
        clearConsole()
        for i in self.helparray:
            print(' - '+i)

    def helpAlias(self):
        self.help()
    def moveTo(self):
        clearConsole()
        self.rDebug()
        self.player.rDebug()
        self.world.rDebug()
        self.world.map.rDebug()
        print('Where would you like to go?')
        room=self.player.room
        print(room)
        if int(len(self.world.map.route[room])) < 3: # if there are less than 3 zones
            ind = len(self.world.map.route) # gets length of map
            zone = str(random.choice(self.world.zones))
            newzone = str(zone+"_"+str(ind))
            self.world.map.route[newzone]=[]
            self.world.map.route[self.player.room].append(newzone)
            self.world.map.route[newzone].append(self.player.room)
            exec("self.world.map."+newzone+"="+zone+"(self.world)")
        for i in self.world.map.route[self.player.room]:
            print(" - " + i)

        def moveToLoop(self): # <- define loop
            newloc = input(": ")
            if newloc in self.world.map.route[self.player.room]:
                self.player.room = newloc
                print("Moving to " + newloc)
            else:
                print("That's not an option, try again.")
                moveToLoop(self)
        moveToLoop(self) # <- run loop

        # Run inspection of room
        roomtitle = self.world.player.room
        room = getattr(self.world.map, roomtitle)
        clearConsole()
        print(random.choice(room.descriptions))

    def inspect(self):
        clearConsole()
        roomtitle = self.world.player.room
        room = getattr(self.world.map,roomtitle)
        list = ['room','inventory']
        for i in room.loot:
            list.append(i)
        print("What do you want to inspect?")
        for i in list:
            print(" - "+i)
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
                    item = getattr(world.item,choice)
                    print(random.choice(item.descriptions))
            else:
                print("That's not an option. Try again.")
                loop(world)
        loop(self,self.world)
    def moveAlias(self):
        self.moveTo()
    def inspectAlias(self):
        self.inspect()
    def wait(self):
        clearConsole()
        array = [
            'You stand about aimlessly.',
            'You wait as if you have all the time in the world.',
            'You waste a few minutes.'
        ]
        print(random.choice(array))
    def waitAlias(self):
        self.wait()
    def scream(self):
        clearConsole()
        print("Something screams with you.")
        self.world.lexeter.achievements.append('scream')
    def pickup(self):
        clearConsole()
        roomtitle = self.world.player.room
        room = getattr(self.world.map,roomtitle)
        if hasattr(room,'loot'):
            if len(room.loot) > 0:
                print("What do you want to pick up?")
                print(' - all')
                for i in room.loot:
                    print(" - "+i)
                choice = input(": ")
                def loop(choice,room):
                    if choice == 'all':
                        for i in room.loot:
                            self.player.inventory.append(i)
                            room.loot.remove(i)
                            print("You picked up "+i)
                    elif choice in room.loot:
                        room.loot.remove(choice)
                        self.player.inventory.append(choice)
                        print("You picked up "+choice)
                    else:
                        print("That's not an option, try again.")
                        loop(input(": "),room)
                loop(choice,room)
            else:
                print("There's nothing here.")
        else:
            print("There's nothing here.")
    def pickupAlias(self):
        self.pickup()
    def pickAlias(self):
        self.pickup()
    def interact(self):
        pass
    def interactAlias(self):
        self.interact()
    def inventory(self):
        clearConsole()
        print("You have:")
        print(self.world.player.inventory)
        inv = self.world.player.inventory
        list = []
        for i in inv:
            count = inv.count(i)
            list.append(" - "+i+" "+str(count))
        for n in list:
            print(n)
            for x in list:
                if x == n:
                    list.remove(x)
    def invenAlias(self):
        self.inventory()
    def invAlias(self):
        self.inventory()

class stone(core):
    def __init__(self,debug):
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

class branch(core):
    def __init__(self,debug):
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

class scrapmetal(core):
    def __init__(self,debug):
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

class egg(core):
    def __init__(self,debug):
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

class potato(core):
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

class shinystone(core):
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

class diamond(core):
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

class ruby(core):
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

class sapphire(core):
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

class emerald(core):
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

class opal(core):
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

class twine(core):
    def __init__(self,debug):
        self.internalID = 'item-twine'
        self.name = 'twine'
        self.quality = 1
        self.descriptions = [
            "A simple length of string."
        ]
        self.debug = debug
        self.rDebug()

class excalibur(core):
    def __init__(self,debug):
        self.internalID='item-excalibur'
        self.name = 'Excalibur'
        self.quality = 4
        self.descriptions = [
            "An arbitrarily powerful sword.",
            "Did this come from the stone, or the lake?",
            "It feels like you don't deserve to hold it."
        ]
        self.debug = debug
        self.rDebug()

class crudespear(core):
    def __init__(self,debug):
        self.internalID='item-crudespear'
        self.name = 'crude spear'
        self.quality = 4
        self.descriptions = [
            "An incredibly simple weapon.",
            "It's like a sharpened stick, but sharper."
        ]
        self.debug = debug
        self.rDebug()

class item(core):
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
            'twine'
        ]
        self.common = [
            'shinystone'
        ]
        self.useful = [
            'egg',
            'potato'
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
        self.crafted = [
            'crudespear'
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
        self.potato = potato(self.debug)
        self.twine = twine(self.debug)
        self.crudespear = crudespear(self.debug)

class crudespearRecipe(core):
    def __init__(self,debug):
        self.internalID = 'recipe-crudespear'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'metalscrap',
            'branch',
            'twine'
        ]

class recipes(core):
    def __init__(self,world):
        self.world = world
        self.debug = self.world.debug
        self.internalID = 'library-crafting'
        self.rDebug()
        self.crudespearRecipe = crudespearRecipe(self.debug)

class constructs(core):
    def __init__(self,world):
        self.world = world
        self.debug = self.world.debug
        self.internalID = 'library-construction'
        self.rDebug()


class shade(core):
    def __init__(self, name, world):
        self.name = name
        world.characterlist.append(self.name)
        self.internalID = 'character-shade-' + self.name
        self.world = world
        self.debug = self.world.debug
        self.rDebug()
        self.room = 'darkroom'
        self.hp = 15
        self.act = act(self.name, self.world)
        self.age = 0
        self.tickCount = random.randrange(1, 5)
        self.prefer = prefer()

        if self.name == 'mek':
            self.prefer.fruit = 'orange'
            self.week = 5
        elif self.name == 'geoflib':
            self.prefer.fruit = 'pineapple'
            self.week = 4

    def tick(self, world):
        self.age += 1;
        self.tickCount += 1
        if self.tickCount == self.week: self.tickCount = 1
        if self.tickCount == 1:
            lines = [
                'heya, stranger!', 'im a shade, not a ghost. theres a difference.',
                'waddup, ' + world.player.name + '?', 'evening!',
                'i cannae find ma lunch!', 'i like ' + self.prefer.fruit + 's. my brother doesnt.',
                'ah, the darkness. so refreshing.', 'blegh! just got a bug in my mouth!',
                'have ya talked to my twin?', 'tha rats here, they make quite the racket!',
                'not a big fan of moths. how bout you?', 'ever been to paris?']
            self.act.speak(random.choice(lines), self.room)
        elif self.tickCount == 2:
            pass  # ask
        elif self.tickCount == 3:
            pass  # nothing/atk
        elif self.tickCount == 4:
            pass  # possiblemove


class darkroom(core):
    def __init__(self, world):
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


# subclass responselog for logging player's responses
class responselog(core):
    def __init__(self):
        self.internalID = 'player-response-log'


class player(core):
    def __init__(self, age, them, world, debug):
        self.them = them;
        self.debug = debug;
        self.internalID = 'player-instance';
        self.rDebug()
        self.hp = 50;
        self.rLog = responselog()
        self.them.act.speak("What is your name?\n")
        self.name = input("")
        self.them.act.speak(self.name + ", eh?")
        self.them.act.speak("Well, have a fun adventure.");
        print("");
        print("")
        self.instance = age;
        self.age = age
        self.inventory = []
        self.act = playerAct(self, world)


class wmap(core):
    def __init__(self, world):
        self.debug = world.debug
        self.internalID = 'world-map'
        self.rDebug()


class world(core):
    def __init__(self, age, them, zones, debug, item, lexeter):
        self.debug = debug;
        self.them = them;
        self.zones = zones
        self.lexeter = lexeter
        self.internalID = 'reality-instance'
        self.rDebug()
        self.them.act.speak("Hmmmmm . . .")
        self.them.act.speak("There's nothing here.")
        self.them.act.speak("Give me a minute.")
        self.time = 45 + (age * 5)
        self.instance = age
        self.age = 0
        self.player = player(age, them, self, debug)
        self.characters = characters()
        self.characterlist = []
        self.item = item
        self.map = wmap(self)
        self.map.darkroom = darkroom(self)
        self.map.route = {}
        self.map.route['darkroom'] = []
        self.map.list = ['darkroom']
        for i in range(3):
            zone = random.choice(self.zones)
            room = str(zone + '_' + str(i))
            self.map.route['darkroom'].append(room);
            self.map.route[room] = ['darkroom']
            self.map.list.append(room)
            exec('self.map.' + room + '=' + zone + '(self)')
        self.player.room = 'darkroom'


# subclass characters for saving each individual character
class characters(core):
    def __init__(self):
        self.internalID = 'character-list'


class them():
    def __init__(self):
        self.name = "#`~<,>_r-kal"
        self.internalID = '__ignore__'
        self.act = actGod(self.name)


class lexeter(core):
    def __init__(self):
        self.debug = False
        self.internalID = 'lexeter'
        self.rDebug()
        self.them = them()
        self.instances = 1
        self.zones = ['pond', 'marble', 'terracotta', 'brickfloor', 'fractured', 'cave', 'canopy', 'cavern', 'shack']
        self.achievements = []
        self.item = item(self)
        self.world = world(self.instances, self.them, self.zones, self.debug, self.item, self)

if __name__ == "__main__":
    from lib.player import *
    from lib.darkroom import *
    from lib.action import *
    from lib.core import *
    lexeter = lex_init()
    tick(lexeter,lexeter.world)
