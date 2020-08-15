"""
Set Up Notes:
1. Press "esc"
2. Go to "settings"
3. Go to "matchmaking preferences"
    a. The generic gamemodes are there. Turn every preference off besides "hostage"
    b. Under that are the sub-gamemodes. Set all mode off besides "protect hostage"
    c. Under that are the maps. Set all off besides "tower"
4. Go to "display"in the settings
5. Switch the display from the current to windowed. It should work with full screen, but I started with windowed and its easier to see the code and errors so its your preference.
6. In the code, work with the "mouse.position" functions for the mouse cursor to hit the four main targets:
    a.1F Restaurant
    b. Operator Doc(When he gets shot down, he is down but not out, delaying the time and ensuring the renown is gained)
    c. Confirm loadout(TIP: The x coordinate is the same as the second target, so just raise the y coordinate up)
    d. Vote for retry(continues the loop after dying
    NOTE: These targets also allow you to shoot and pretend the character is playing. You do not move your aiming, as that is banned by "Battleye Services."
    So you stand still, but with no risk of shooting the hostage

TO START:
    After geteting it all set up, go to terrorist hunt, lone wolf, normal (the moste efficient for renown)
        ***Do NOT play program with other players, especially randoms, as they may report and ban you***
WARNING: You may get banned for this. I have not yet, but still there is always a risk. I do not run the program more than 10 hours overnight, and not every night
"""

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random
#You need to pip3 install "pynput" and "threading". the rest should be already included


long_delay = 1 #The delays are in seconds, so you can change it to experiment
delay = 0.1
delay2 = 0.75
longer_delay = 2.5
button = Button.left
start_stop_key = KeyCode(char=';') #The start/stop button is semicolon and apostrophe. I made is so it doesn't overlap with keybinds but you can change it
exit_key = KeyCode(char="'")


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                #Location
                time.sleep(delay2)
                mouse.position = (135,375) #Mouse Position moves the mouse. Idk your resolution so just experiment with tehe current ones
                time.sleep(delay)
                mouse.press(Button.left)
                time.sleep(delay)
                mouse.release(Button.left)

                #Character
                #time.sleep(delay2)
                #time.sleep(delay)
                #time.sleep(long_delay)
                time.sleep(longer_delay)
                mouse.position = (350, 280)
                time.sleep(delay)
                mouse.press(Button.left)
                time.sleep(delay)
                mouse.release(Button.left)

                #Confirm
                time.sleep(long_delay)
                mouse.position = (325,220)
                time.sleep(delay)
                mouse.press(Button.left)
                time.sleep(delay)
                mouse.release(Button.left)

                #retry
                time.sleep(long_delay)
                mouse.position =  (560, 600)
                time.sleep(delay)
                mouse.press(Button.left)
                time.sleep(delay)
                mouse.release(Button.left)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start();


def on_press(key):
    if key == start_stop_key:
        #print("program started")
        if click_thread.running:
            click_thread.stop_clicking()
            print("program paused")
        else:
            click_thread.start_clicking()
            print("program started")
    elif key == exit_key:
        print("program ended")
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()







