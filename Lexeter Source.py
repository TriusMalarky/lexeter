from lib.action import *
from lib.core import *

if __name__ == "__main__":


    try:
        lexeter = lex_init()
    except:
        log = open('save/log.txt', 'a')
        print("Error! Issue initializing Lexeter.")
        print("Please report this to https://github.com/TriusMalarky/lexeterbuilds/issues")
        log.write("!! Issue Initializing Lexeter !!\n")
        log.close()

    try:
        tick(lexeter, lexeter.world)
    except:
        log = open('save/log.txt', 'a')
        print("Error! Something went wrong.")
        print("This is a catch-all error, unfortunately there is no more information.")
        print("Please report this to https://github.com/TriusMalarky/lexeterbuilds/issues")
        log.write("!! Unknown Game Error !!\n")
        _ = input("Enter anything to exit Lexeter: ")
    finally:
        log.write("|| Closing Lexeter ||\n")
        log.close()
        quit()


# Official Naming Conventions:

# Logging:
# Errors:
# - Catastrophic Error: !! issue !!