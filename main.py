from pynput import keyboard
import time

control = keyboard.Controller()
Key = keyboard.Key
ignore = False
spaceTimes = []

def pressed(key):
    global ignore
    #print(key)
def released(key):
    """if key == Key.space:
        print("key released")
        control.release(key)"""
def win32_event_filter(msg, data):
    global ignore
    #print(data.flags)
    #print(msg, data.vkCode)
    if data.vkCode == 32 and not ignore:
        if msg != 257:
            spaceTimes.append(time.time())
        #print("space blocked")
        listener.suppress_event()
listener = keyboard.Listener(on_press=pressed,on_release=released,win32_event_filter=win32_event_filter)
listener.start()
times = 0
hold = False
actions = []
happening = False
holdingMaybe = 0
def action(numOfSpaces):
    actions.append((0,numOfSpaces))
def holding(secs):
    actions.append((1,secs))
    if actions[-2][0] == 0 and actions[-2][1] == 1:
        actions.pop(-2)
while True:
    happening = len(spaceTimes) > 0
    if happening:
        times = time.time() - spaceTimes[-1]
        if len(spaceTimes) > 1:
            if spaceTimes[-1]-spaceTimes[-2] < 0.05 and not hold:
                hold = True
    if times > 0.3:
        if hold:
            secs = time.time() - holdingMaybe - times
            print("hold " + str(secs) + " seconds")
            print(holdingMaybe)
            holding(secs)
            holdingMaybe = 0
        else:
            amount = len(spaceTimes)
            print(amount)
            action(amount)
            if amount == 1:
                holdingMaybe = spaceTimes[0]

        spaceTimes.clear()
        times = 0
        hold = False