if __name__ == "__main__":
    from lib.player import *
    from lib.darkroom import *
    from lib.action import *
    from lib.core import *
    lexeter = lex_init()
    tick(lexeter,lexeter.world)
