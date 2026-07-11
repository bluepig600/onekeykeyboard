from pynput import keyboard
import time

control = keyboard.Controller()
Key = keyboard.Key
ignore = False
spacetimes = []

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
            spacetimes.append(time.time())
        #print("space blocked")
        listener.suppress_event()
listener = keyboard.Listener(on_press=pressed,on_release=released,win32_event_filter=win32_event_filter)
listener.start()
times = 0
while True:
    if len(spacetimes) > 0:
        times = time.time() - spacetimes[-1]
    if times > 0.3:
        print(len(spacetimes))
        spacetimes.clear()
        times = 0
