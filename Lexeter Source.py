if __name__ == "__main__":
    from lib.player import *
    from lib.darkroom import *
    from lib.action import *
    from lib.core import *
    log = open('save/log.txt', 'a')
    log.write('|| Initializing Lexeter ||')
    try:
        lexeter = lex_init()
    except:
        print("Error! Issue initializing Lexeter.")
        print("Please report this to https://github.com/TriusMalarky/lexeterbuilds/issues")
        log.write("!! Issue Initializing Lexeter !!")

    try:
        tick(lexeter, lexeter.world)
    except:
        print("Error! Something went wrong.")
        print("This is a catch-all error, unfortunately there is no more information.")
        print("Please report this to https://github.com/TriusMalarky/lexeterbuilds/issues")
        log.write("!! Unknown Game Error !!")
        _ = input("Enter anything to exit Lexeter: ")
        quit()
