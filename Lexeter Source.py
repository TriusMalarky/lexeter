from lib.action import *
from lib.core import *
import tkinter as tk

__author__ = 'TriusMalarky'

if __name__ == "__main__":

    runtime = runtime_init()
    tick(runtime, runtime.lexeter.world)


    try:
        runtime = runtime_init()
    except:
        log = open('save/log.txt', 'a')
        print("Error! Issue initializing Lexeter.")
        print("Please report this to https://github.com/TriusMalarky/lexeterbuilds/issues")
        log.write("!! Issue Initializing Lexeter !!\n")
        log.close()

    try:
        tick(runtime, runtime.lexeter.world)
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