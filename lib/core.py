try:
    import pickle
    import os
    import inspect
    import random
    import time
except ModuleNotFoundError:
    log = open('save/log.txt', 'a')
    print("Warning! core module unable to find builtin module(s).")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    print("This involves one or more of Python's built-in modules. Consider reinstalling Python.")
    log.write("!! Core Module unable to find Builtin Module(s) !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()
except ImportError:
    log = open('save/log.txt', 'a')
    print("Warning! core module had issues importing builtin module(s).")
    print("Please submit this error and the log file to https://github.com/TriusMalarky/lexeterbuilds/issues")
    print("This involves one or more of Python's built-in modules. Consider reinstalling Python.")
    log.write("!! Core Module unable to import Builtin Module(s) !!")
    _ = input("Enter anything to exit Lexeter: ")
    log.write("|| Closing Lexeter ||\n")
    log.close()
    quit()

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


class core(): # <-- core class, all other classes should inherit this
    def __init__(self):
        self.internalID = 'core-parent'

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

    def error(self, error, location, context = 'none'):
        errorList = {
            "write-log": "writeToLogFile",
            "player-action-command": "runCommand",
            "player-action-move-createzone": "generateZone",
            "player-action-move-move": "moveZones"
        }
        errorMessage = ''
        if error in errorList:
            errorMessage = errorList[error]
        else:
            errorMessage = 'unknownError'

        print("Error! Please report the following to https://github.com/TriusMalarky/lexeterbuilds/issues :")
        print(str(self.internalID) + ":" + errorMessage + ":" + location + ":" + context)


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
    log = open('save/log.txt', 'a')
    log.write('|| Initializing Lexeter ||\n')
    log.write("[" + str(time.ctime(time.time())) + "] Initialize\n")
    log.close()
    if os.path.exists('save\\lexeter.txt'):
        lexet = load()
        random.seed = lexet.world.seed
        return lexet
    else:
        open('save\\lexeter.txt','w')
        from lib.player import Lexeter
        lexet = Lexeter()
        save(lexet)
        return lexet






def tick(lexeter, world):
    # Luck Calculations
    if lexeter.luck:
        if world.luckAttempts >= 15 + world.luck * 5:
            world.luck += 1
            world.luckAttempts = 0
        if world.luck >= 10:
            world.luck = random.randint(-3, 4)

    for _ in world.characterlist:
        exec('world.characters.'+_.lower()+'.tick(world)')
    world.player.act.playeraction()
    save(lexeter) # save on every tick
    tick(lexeter,world)
