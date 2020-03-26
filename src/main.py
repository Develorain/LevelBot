from imagesearch import *
from state import State
import keyboard
import random

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

# playagain
# findmatch... etc

def determine_current_state():
    time1 = time.clock()
    im = region_grabber((0, 0, 1920, 1080))
    
    a = imagesearcharea("play.png", 0, 0, 1920, 1080, 0.95, im)
    b = imagesearcharea("confirm.png", 0, 0, 1920, 1080, 0.95, im)
    c = imagesearcharea("lobby.png", 0, 0, 1920, 1080, 0.95, im)
    i = imagesearcharea("findingmatch.png", 0, 0, 1920, 1080, 0.95, im)
    d = imagesearcharea("accept.png", 0, 0, 1920, 1080, 0.95, im)
    e = imagesearcharea("champion.png", 0, 0, 1920, 1080, 0.95, im)
    f = imagesearcharea("lockin.png", 0, 0, 1920, 1080, 0.95, im)
    
    pos = imagesearcharea("missinghp.png", 962, 380, 1010, 404, 0.95, im)

    g = imagesearcharea("nexus.png", 0, 0, 1920, 1080, 0.8, im)
    h = imagesearcharea("continue.png", 0, 0, 1920, 1080, 0.95, im)
    j = imagesearcharea("waitingforgametostart.png", 0, 0, 1920, 1080, 0.8, im)
    
    k = imagesearcharea("honorscreen.png", 0, 0, 1920, 1080, 0.8, im)
    m = imagesearcharea("playagain.png", 0, 0, 1920, 1080, 0.8, im)

    n = imagesearcharea("ok.png", 0, 0, 1920, 1080, 0.8, im)
    o = imagesearcharea("loadingscreen.png", 0, 0, 1920, 1080, 0.8, im)


    if pos[0] != -1:
        return State.IN_GAME_HEAL_MODE, 1
    elif g[0] != -1:
        return State.IN_GAME_ATTACK_MODE, 1
    #elif p[0] != -1:
        #return State.IN_GAME_WAIT_MODE
    elif n[0] != -1:
        return State.OK, 1
    elif o[0] != -1:
        return State.LOADING_SCREEN, 1
    elif k[0] != -1:
        return State.HONOR_SCREEN, 1
    elif b[0] != -1:
        return State.GAME_TYPE_SELECT, 1
    elif c[0] != -1:
        return State.LOBBY, 1
    elif d[0] != -1:
        return State.ACCEPT_SCREEN, 1
    elif e[0] != -1:
        return State.CHAMPION_SELECT, 1
    elif f[0] != -1:
        return State.LOCK_IN, 1
    elif h[0] != -1:
        return State.ACCEPT_VICTORY, 1
    elif a[0] != -1:
        return State.HOME, a
    elif i[0] != -1:
        return State.FINDING_MATCH, 1
    elif j[0] != -1:
        return State.WAITING_FOR_GAME_TO_START, 1
    elif m[0] != -1:
        return State.POST_GAME_LOBBY, 1
    else:
        return State.UNKNOWN_STATE, 1

def main():
    while True:
        state, position = determine_current_state()
        print(state)
        print(position)

    while True:
        state, position = determine_current_state()
        print(state)

        if state == State.HOME:
            pos = imagesearch("play.png")

            if pos[0] != -1:
                click_image("play.png", pos, "left", 0.2, offset=5)
            
            time.sleep(5)

        elif state == State.GAME_TYPE_SELECT:
            pos = imagesearch("confirm.png")
            
            if pos[0] != -1:
                click_image("confirm.png", pos, "left", 0.2, offset=5)
            
            time.sleep(5)
            
        elif state == State.LOBBY:
            pos = imagesearch("findmatch.png")
            
            if pos[0] != -1:
                click_image("findmatch.png", pos, "left", 0.2, offset=5)

            time.sleep(5)

        elif state == State.FINDING_MATCH:
            time.sleep(5)

        elif state == State.LOADING_SCREEN:
            time.sleep(5)

        elif state == State.ACCEPT_SCREEN:
            pos = imagesearch("accept.png")
            
            if pos[0] != -1:
                click_image("accept.png", pos, "left", 0.2, offset=5)
            
            time.sleep(5)

        elif state == State.CHAMPION_SELECT:
            pos = imagesearch("champion.png")
            
            if pos[0] != -1:
                click_image("champion.png", pos, "left", 0.2, offset=5)
            
            time.sleep(5)
        
        elif state == State.LOCK_IN:
            pos = imagesearch("lockin.png")
            
            if pos[0] != -1:
                click_image("lockin.png", pos, "left", 0.2, offset=5)
            
            time.sleep(5)

        elif state == State.WAITING_FOR_GAME_TO_START:
            time.sleep(5)
        
        elif state == State.IN_GAME_ATTACK_MODE:
            pos = imagesearch("nexus.png")

            if pos[0] != -1:
                moveMouseRandomPosition()
                pyautogui.mouseDown(button="right")
                waitRandomTime()
                pyautogui.mouseUp(button="right")
                waitRandomTime()

                click_image("nexus.png", pos, "left", 0.2, offset=10)
                time.sleep(5)
        
        elif state == State.IN_GAME_HEAL_MODE:
            pos = imagesearch("recallspot.png")
            
            if pos[0] != -1:
                pyautogui.moveTo(pos)
                pyautogui.mouseDown(button="right")
                waitRandomTime()
                pyautogui.mouseUp(button="right")

                time.sleep(10)
                pos1 = imagesearch("recall.png")
                
                if pos1[0] != -1:
                    click_image("recall.png", pos1, "left", 0.2, offset=5)
                    time.sleep(20)
        
        elif state == State.ACCEPT_VICTORY:
            pos = imagesearch("continue.png")

            if pos[0] != -1:
                click_image("continue.png", pos, "left", 0.2, offset=5)
                time.sleep(5)
        
        elif state == State.HONOR_SCREEN:
            pos = imagesearch("honorscreen.png")

            if pos[0] != -1:
                click_image("honorscreen.png", pos, "left", 0.2, offset=5)
                time.sleep(5)
        
        elif state == State.POST_GAME_LOBBY:
            pos = imagesearch("playagain.png")

            if pos[0] != -1:
                click_image("playagain.png", pos, "left", 0.2, offset=5)
                time.sleep(5)
        
        elif state == State.OK:
            pos = imagesearch("ok.png")

            if pos[0] != -1:
                click_image("ok.png", pos, "left", 0.2, offset=5)
                time.sleep(5)


def waitRandomTime():
    # random time between the two times
    time.sleep(random.uniform(0.5, 1.5))

def moveMouseRandomPosition():
    x = random.uniform(0, 1920)
    y = random.uniform(0, 1080)

    pyautogui.moveTo(x, y)

if __name__ == '__main__':
    main()