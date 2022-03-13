import pyautogui as pag
import threading
import time

#N_DISCRETE_ACTIONS = 11
MULTIDISCRETE_NVEC = [3, 3, 3, 3, 2]

keys = ['left', 'right', 'down', 'c', 'shift']
hold_times = [-1, 0, .3]

def hold_key (key, hold):
    if hold < 0: return
    pag.keyDown(key)
    time.sleep(hold)
    pag.keyUp(key)

def async_hold_key(key, hold):
    threading.Thread(target=hold_key, args=(key, hold)).start()

def take_action(action):
    for key, hold in enumerate(action):
        async_hold_key(keys[key], hold_times[hold])

    # match action:
    #     case 1:
    #         pag.hotkey('left')
    #     case 2:
    #         pag.hotkey('right')
    #     case 3:
    #         pag.hotkey('c')
    #     case 4:
    #         pag.hotkey('shift')
    #     case 5:
    #         pag.hotkey('left', 'c')
    #     case 6:
    #         pag.hotkey('right', 'c')
    #     case 7:
    #         pag.hotkey('left', 'c', 'shift')
    #     case 8:
    #         pag.hotkey('right', 'c', 'shift')
    #     case 9:
    #         pag.hotkey('left', 'down', 'c', 'shift')
    #     case 10:
    #         pag.hotkey('right', 'down', 'c', 'shift')


if __name__ == '__main__':
    time.sleep(1)
    take_action([0, 0, 0, 1, 0])