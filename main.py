from pynput import keyboard
control = keyboard.Controller()
Key = keyboard.Key
ignore = False
def pressed(key):
    global ignore
    print(key)
    if key == keyboard.KeyCode.from_char('q'):
        print("space pressed")
        ignore = True
        control.press(Key.space)
        control.release(Key.space)
        ignore = False
def released(key):
    """if key == Key.space:
        print("key released")
        control.release(key)"""
def win32_event_filter(msg, data):
    global ignore
    INJECTED = 0x10
    print(data.flags)
    print(msg, data.vkCode)
    if data.vkCode == 32 and not ignore:
        print("space blocked")
        listener.suppress_event()
with keyboard.Listener(on_press=pressed,on_release=released,win32_event_filter=win32_event_filter) as listener:
    listener.join()