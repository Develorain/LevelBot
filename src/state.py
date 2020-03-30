from enum import Enum

class State(Enum):
    HOME = 1
    GAME_TYPE_SELECT = 2
    LOBBY = 3
    FINDING_MATCH = 4
    ACCEPT_SCREEN = 12
    CHAMPION_SELECT = 5
    LOCK_IN = 6
    WAITING_FOR_GAME_TO_START = 7 # useless state should just be a general waiting state
    IN_GAME_WAIT_MODE = 8
    IN_GAME_ATTACK_MODE = 16
    IN_GAME_HEAL_MODE = 17
    SHOP = 21
    ITEM1 = 22
    ITEM2 = 23
    ITEM3 = 27
    CLOSE_SHOP = 24
    LOCK_SCREEN = 25
    CANT_BUY_ITEM = 26
    ATTACK_MODE = 9
    HEAL_MODE = 10
    ACCEPT_VICTORY = 13
    POST_GAME_LOBBY = 11
    WAITING = 14
    UNKNOWN_STATE = 15
    HONOR_SCREEN = 18
    OK = 19
    LOADING_SCREEN = 20

# play
# confirm
# findmatch
# accept
# champion
# lockin
# ingame (redundant)
# item (add later)
# nexus, missinghp
# continue