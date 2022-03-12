import pyautogui as pag

N_DISCRETE_ACTIONS = 6

def take_action(action):
    match action:
        case 0:
            pag.keyDown('up')
            pag.keyUp('up')
        case 1:
            pag.keyDown('right')
            pag.keyUp('right')
        case 2:
            pag.keyDown('down')
            pag.keyUp('down')
        case 3:
            pag.keyDown('left')
            pag.keyUp('left')
        case 4:
            pag.keyDown('c')
            pag.keyUp('c')
        case 5:
            pag.keyDown('shift')
            pag.keyUp('shift')
        # case 6:
        #     pag.keyDown(['up', 'right'])


if __name__ == '__main__':
    take_action(4)
    