from imagesearch import *
from state import State
import keyboard
import random

class Main:
    def determine_current_state(self):
        im = region_grabber((0, 0, 1920, 1080))
        
        a = imagesearcharea("play.png", 0, 0, 1920, 1080, 0.95, im)
        b = imagesearcharea("confirm.png", 0, 0, 1920, 1080, 0.95, im)
        c = imagesearcharea("findmatch.png", 0, 0, 1920, 1080, 0.95, im)
        i = imagesearcharea("findingmatch.png", 0, 0, 1920, 1080, 0.95, im)
        d = imagesearcharea("accept.png", 0, 0, 1920, 1080, 0.95, im)
        e = imagesearcharea("champion.png", 0, 0, 1920, 1080, 0.95, im)
        f = imagesearcharea("lockin.png", 0, 0, 1920, 1080, 0.95, im)
        g = imagesearcharea("nexus.png", 0, 0, 1920, 1080, 0.8, im)
        h = imagesearcharea("continue.png", 0, 0, 1920, 1080, 0.95, im)
        k = imagesearcharea("honorscreen.png", 0, 0, 1920, 1080, 0.8, im)
        m = imagesearcharea("playagain.png", 0, 0, 1920, 1080, 0.8, im)
        n = imagesearcharea("ok.png", 0, 0, 1920, 1080, 0.8, im)
        p = imagesearcharea("shop.png", 0, 0, 1920, 1080, 0.8, im)
        q = imagesearcharea("doran.png", 0, 0, 1920, 1080, 0.95, im)
        s = imagesearcharea("closeshop.png", 0, 0, 1920, 1080, 0.8, im)
        t = imagesearcharea("lockscreen.png", 0, 0, 1920, 1080, 0.95, im)

        if q[0] != -1 and s[0] != -1:
            return State.ITEM, q
        elif q[0] == -1 and s[0] != -1:
            return State.CLOSE_SHOP, s
        elif t[0] != -1:
            return State.LOCK_SCREEN, t
        #elif p[0] != -1:
            #return State.SHOP, p
        elif g[0] != -1:
            return State.IN_GAME_ATTACK_MODE, g
        elif n[0] != -1:
            return State.OK, n
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
        elif m[0] != -1:
            return State.POST_GAME_LOBBY, m
        else:
            return State.UNKNOWN_STATE, 0

    def loop(self):
        while True:
            beforeanythingpos = pyautogui.position()
            state, position = self.determine_current_state()
            print(state)
            print(position)
            
            if self.active:
                if state == State.HOME:
                    click_image("play.png", position, "left", 0.2, offset=5)
                    
                    pyautogui.moveTo(beforeanythingpos)
                    time.sleep(1)
                elif state == State.GAME_TYPE_SELECT:
                    click_image("confirm.png", position, "left", 0.2, offset=5)
                    
                    pyautogui.moveTo(beforeanythingpos)
                    time.sleep(1)
                elif state == State.LOBBY:
                    click_image("findmatch.png", position, "left", 0.2, offset=5)

                    pyautogui.moveTo(beforeanythingpos)
                    time.sleep(1)
                elif state == State.FINDING_MATCH:
                    time.sleep(2)
                elif state == State.ACCEPT_SCREEN:
                    click_image("accept.png", position, "left", 0.2, offset=5)
                    pyautogui.moveTo(beforeanythingpos)
                elif state == State.CHAMPION_SELECT:
                    click_image("champion.png", position, "left", 0.2, offset=5)

                    pyautogui.moveTo(beforeanythingpos)
                    time.sleep(1)
                elif state == State.LOCK_IN:
                    click_image("lockin.png", position, "left", 0.2, offset=5)
                    
                    pyautogui.moveTo(beforeanythingpos)
                    time.sleep(1)
                elif state == State.ITEM:
                    click_image("doran.png", position, "right", 0.2, offset=5)
                    pyautogui.moveTo(beforeanythingpos)

                    pos2 = imagesearcharea("closeshop.png", 0, 0, 1920, 1080, 0.8)

                    if pos2[0] != -1:
                        click_image("closeshop.png", pos2, "left", 0.2, offset=5)
                        pyautogui.moveTo(beforeanythingpos)

                        pos3 = imagesearcharea("nexus.png", 0, 0, 1920, 1080, 0.8)

                        if pos3[0] != -1:
                            click_image("nexus.png", pos3, "left", 0.2, offset=5)
                            pyautogui.moveTo(beforeanythingpos)
                            time.sleep(5)
                elif state == State.CANT_BUY_ITEM:
                    pos2 = imagesearcharea("closeshop.png", 0, 0, 1920, 1080, 0.8)
                    
                    if pos2[0] != -1:
                        click_image("closeshop.png", pos2, "left", 0.2, offset=5)
                        pyautogui.moveTo(beforeanythingpos)

                        pos3 = imagesearcharea("nexus.png", 0, 0, 1920, 1080, 0.8)

                        if pos3[0] != -1:
                            click_image("nexus.png", pos3, "left", 0.2, offset=5)
                            pyautogui.moveTo(beforeanythingpos)
                            time.sleep(5)
                            time.sleep(30)
                elif state == State.CLOSE_SHOP:
                    click_image("closeshop.png", position, "left", 0.2, offset=5)
                    pyautogui.moveTo(beforeanythingpos)
                    time.sleep(30)
                elif state == State.SHOP:
                    click_image("shop.png", position, "left", 0.2, offset=5)
                    pyautogui.moveTo(beforeanythingpos)

                    time.sleep(1)
                    time.sleep(30)
                elif state == State.LOCK_SCREEN:
                    click_image("lockscreen.png", position, "left", 0.2, offset=5)
                    pyautogui.moveTo(beforeanythingpos)
                elif state == State.IN_GAME_ATTACK_MODE:
                    self.moveMouseRandomPosition()
                    pyautogui.mouseDown(button="right")
                    self.waitRandomShortTime()
                    pyautogui.mouseUp(button="right")
                    pyautogui.moveTo(beforeanythingpos)
                    self.waitRandomShortTime()

                    click_image("nexus.png", position, "left", 0.2, offset=10)
                    pyautogui.moveTo(beforeanythingpos)

                    time.sleep(3)
                    time.sleep(30)
                elif state == State.ACCEPT_VICTORY:
                    click_image("continue.png", position, "left", 0.2, offset=5)
                    pyautogui.moveTo(beforeanythingpos)
                    
                    time.sleep(5)
                elif state == State.HONOR_SCREEN:
                    click_image("honorscreen.png", position, "left", 0.2, offset=5)
                    pyautogui.moveTo(beforeanythingpos)
                    
                    time.sleep(5)
                elif state == State.POST_GAME_LOBBY:
                    click_image("playagain.png", position, "left", 0.2, offset=5)
                    pyautogui.moveTo(beforeanythingpos)

                    time.sleep(5)
                elif state == State.OK:
                    click_image("ok.png", position, "left", 0.2, offset=5)
                    pyautogui.moveTo(beforeanythingpos)

                    time.sleep(5)

    def waitRandomShortTime(self):
        time.sleep(random.uniform(0.4, 0.6))

    def waitRandomTime(self):
        # random time between the two times
        time.sleep(random.uniform(0.5, 1.5))

    def moveMouseRandomPosition(self):
        x = random.uniform(0, 1920/2)
        y = random.uniform(0, 1080/2)
        y = y + 1080/2
        #bottom left corner of screen

        pyautogui.moveTo(x, y)
    
    def __init__(self):
        self.active = True
        self.loop()

if __name__ == '__main__':
    Main()