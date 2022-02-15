from lib.core import *


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