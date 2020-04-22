from imagesearch import *
from state import State
import keyboard
import random

def determine_current_state():
    im = region_grabber((0, 0, 1920, 1080))
    
    a = imagesearcharea("play.png", 0, 0, 1920, 1080, 0.95, im)
    b = imagesearcharea("confirm.png", 0, 0, 1920, 1080, 0.95, im)
    c = imagesearcharea("findmatch.png", 0, 0, 1920, 1080, 0.95, im)
    i = imagesearcharea("findingmatch.png", 0, 0, 1920, 1080, 0.95, im)
    d = imagesearcharea("accept.png", 0, 0, 1920, 1080, 0.95, im)
    e = imagesearcharea("champion2.png", 0, 0, 1920, 1080, 0.95, im)
    f = imagesearcharea("lockin.png", 0, 0, 1920, 1080, 0.95, im)
    
    pos = imagesearcharea("missinghp2.png", 962, 380, 1010, 404, 0.95, im)

    g = imagesearcharea("nexus2.png", 0, 0, 1920, 1080, 0.8, im)
    h = imagesearcharea("continue.png", 0, 0, 1920, 1080, 0.95, im)
    j = imagesearcharea("waitingforgametostart.png", 0, 0, 1920, 1080, 0.95, im)
    
    k = imagesearcharea("honorscreen.png", 0, 0, 1920, 1080, 0.8, im)
    m = imagesearcharea("playagain.png", 0, 0, 1920, 1080, 0.8, im)

    n = imagesearcharea("ok.png", 0, 0, 1920, 1080, 0.8, im)
    o = imagesearcharea("loadingscreen.png", 0, 0, 1920, 1080, 0.8, im)
    
    p = imagesearcharea("shop.png", 0, 0, 1920, 1080, 0.8, im)
    q = imagesearcharea("doran.png", 0, 0, 1920, 1080, 0.95, im)
    r = imagesearcharea("item2large.png", 0, 0, 1920, 1080, 0.85, im)
    u = imagesearcharea("item3large.png", 0, 0, 1920, 1080, 0.95, im)

    s = imagesearcharea("closeshop.png", 0, 0, 1920, 1080, 0.8, im)

    t = imagesearcharea("lockscreen.png", 0, 0, 1920, 1080, 0.95, im)

    if q[0] != -1 and s[0] != -1:
        print("FOUND ITEM 111111111111111111")
        return State.ITEM1, q
    elif r[0] != -1 and s[0] != -1:
        print("FOUND ITEM 22222222222222222222")
        return State.ITEM2, r
    elif u[0] != -1 and s[0] != -1:
        print("FOUND ITEM 3333333333333333333333")
        return State.ITEM3, u
    elif q[0] == -1 and r[0] == -1 and u[0] == -1 and s[0] != -1:
        print("CANT AFFORD ALL ITEMS")
        return State.CLOSE_SHOP, s

    if pos[0] != -1:
        return State.IN_GAME_HEAL_MODE, 0
    elif t[0] != -1:
        return State.LOCK_SCREEN, t
    elif p[0] != -1:
        return State.SHOP, p
    elif s[0] != -1:
        print("just jumped straight here")
        return State.CLOSE_SHOP, s
    elif g[0] != -1:
        return State.IN_GAME_ATTACK_MODE, g
    elif n[0] != -1:
        return State.OK, n
    elif o[0] != -1:
        return State.LOADING_SCREEN, 0
    elif k[0] != -1:
        return State.HONOR_SCREEN, k
    elif b[0] != -1:
        return State.GAME_TYPE_SELECT, b
    elif c[0] != -1:
        return State.LOBBY, c
    elif d[0] != -1:
        return State.ACCEPT_SCREEN, d
    elif e[0] != -1:
        return State.CHAMPION_SELECT, e
    elif f[0] != -1:
        return State.LOCK_IN, f
    elif h[0] != -1:
        return State.ACCEPT_VICTORY, h
    elif a[0] != -1:
        return State.HOME, a
    elif i[0] != -1:
        return State.FINDING_MATCH, 0
    elif j[0] != -1:
        return State.WAITING_FOR_GAME_TO_START, 0
    elif m[0] != -1:
        return State.POST_GAME_LOBBY, m
    else:
        return State.UNKNOWN_STATE, 0

def main():
    #while True:
        #state, position = determine_current_state()
        #print(state)
        #print(position)
        #print(pyautogui.displayMousePosition())
    
    previousState = None
    shopJustClosed = False

    while True:
        state, position = determine_current_state()
        print(state)
        print(position)

        if state == State.HOME:
            click_image("play.png", position, "left", 0.2, offset=5)
            
            time.sleep(1)

        elif state == State.GAME_TYPE_SELECT:
            click_image("confirm.png", position, "left", 0.2, offset=5)
            
            time.sleep(1)
            
        elif state == State.LOBBY:
            click_image("findmatch.png", position, "left", 0.2, offset=5)

            time.sleep(1)

        elif state == State.FINDING_MATCH or state == State.LOADING_SCREEN or state == State.WAITING_FOR_GAME_TO_START:
            time.sleep(5)

        elif state == State.ACCEPT_SCREEN:
            click_image("accept.png", position, "left", 0.2, offset=5)

        elif state == State.CHAMPION_SELECT:
            click_image("champion2.png", position, "left", 0.2, offset=5)
            
            time.sleep(1)
        
        elif state == State.LOCK_IN:
            click_image("lockin.png", position, "left", 0.2, offset=5)
            
            time.sleep(1)

        elif state == State.ITEM1:
            click_image("doran.png", position, "right", 0.2, offset=5)

            pos2 = imagesearcharea("closeshop.png", 0, 0, 1920, 1080, 0.8)

            if pos2[0] != -1:
                click_image("closeshop.png", pos2, "left", 0.2, offset=5)

                pos3 = imagesearcharea("nexus2.png", 0, 0, 1920, 1080, 0.8)

                if pos3[0] != -1:
                    click_image("nexus2.png", pos3, "left", 0.2, offset=5)
                    time.sleep(5)

        elif state == State.ITEM2:
            click_image("item2large.png", position, "right", 0.2, offset=5)

            pos2 = imagesearcharea("closeshop.png", 0, 0, 1920, 1080, 0.8)

            if pos2[0] != -1:
                click_image("closeshop.png", pos2, "left", 0.2, offset=5)

                pos3 = imagesearcharea("nexus2.png", 0, 0, 1920, 1080, 0.8)

                if pos3[0] != -1:
                    click_image("nexus2.png", pos3, "left", 0.2, offset=5)
                    time.sleep(5)

        elif state == State.ITEM3:
            click_image("item3large.png", position, "right", 0.2, offset=5)

            pos2 = imagesearcharea("closeshop.png", 0, 0, 1920, 1080, 0.8)

            if pos2[0] != -1:
                click_image("closeshop.png", pos2, "left", 0.2, offset=5)

                pos3 = imagesearcharea("nexus2.png", 0, 0, 1920, 1080, 0.8)

                if pos3[0] != -1:
                    click_image("nexus2.png", pos3, "left", 0.2, offset=5)
                    time.sleep(5)

        elif state == State.CANT_BUY_ITEM:
            pos2 = imagesearcharea("closeshop.png", 0, 0, 1920, 1080, 0.8)
            
            if pos2[0] != -1:
                click_image("closeshop.png", pos2, "left", 0.2, offset=5)

                pos3 = imagesearcharea("nexus2.png", 0, 0, 1920, 1080, 0.8)

                if pos3[0] != -1:
                    click_image("nexus2.png", pos3, "left", 0.2, offset=5)
                    time.sleep(5)

        elif state == State.CLOSE_SHOP:
            click_image("closeshop.png", position, "left", 0.2, offset=5)

        elif state == State.SHOP:
            click_image("shop.png", position, "left", 0.2, offset=5)

            time.sleep(1)

        elif state == State.LOCK_SCREEN:
            click_image("lockscreen.png", position, "left", 0.2, offset=5)
        
        elif state == State.IN_GAME_HEAL_MODE:
            pos2 = imagesearch("recallspot.png")
            
            if pos2[0] != -1:
                pyautogui.moveTo(pos2)
                pyautogui.mouseDown(button="right")
                waitRandomTime()
                pyautogui.mouseUp(button="right")

                # Wait for player to walk to safe location
                time.sleep(10)
            
            # Just recall in place if cant walk to safe spot
            pos1 = imagesearch("recall.png")
            
            if pos1[0] != -1:
                click_image("recall.png", pos1, "left", 0.2, offset=5)
                time.sleep(20)
        
        elif state == State.IN_GAME_ATTACK_MODE:
            moveMouseRandomPosition()
            pyautogui.mouseDown(button="right")
            waitRandomShortTime()
            pyautogui.mouseUp(button="right")
            waitRandomShortTime()

            click_image("nexus2.png", position, "left", 0.2, offset=10)
            time.sleep(3)   
        
        elif state == State.ACCEPT_VICTORY:
            click_image("continue.png", position, "left", 0.2, offset=5)
            
            time.sleep(5)
        
        elif state == State.HONOR_SCREEN:
            click_image("honorscreen.png", position, "left", 0.2, offset=5)
            
            time.sleep(5)
        
        elif state == State.POST_GAME_LOBBY:
            click_image("playagain.png", position, "left", 0.2, offset=5)

            time.sleep(5)
        
        elif state == State.OK:
            click_image("ok.png", position, "left", 0.2, offset=5)

            time.sleep(5)
        

        previousState = state

def waitRandomShortTime():
    time.sleep(random.uniform(0.4, 0.6))

def waitRandomTime():
    # random time between the two times
    time.sleep(random.uniform(0.5, 1.5))

def moveMouseRandomPosition():
    x = random.uniform(0, 1920/2)
    y = random.uniform(0, 1080/2)
    y = y + 1080/2
    #bottom left corner of screen

    pyautogui.moveTo(x, y)

if __name__ == '__main__':
    main()