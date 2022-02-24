import cv2
import numpy as np
from grabscreen import grab_screen

# def empty(x):
#     pass
# cv2.namedWindow('aaa')
# cv2.createTrackbar('t1','aaa',0,255, empty)
# cv2.createTrackbar('t2','aaa',0,255, empty)

def main():
    # while True:
    #     screen = grab_screen(region=(0, 26, 960, 750))
    #     hsv_img = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)

    #     t1 = cv2.getTrackbarPos('t1','aaa')
    #     t2 = cv2.getTrackbarPos('t2','aaa')
    #     mask = cv2.inRange(hsv_img, (t1, 68, 0), (t2, 133, 255))
    #     cv2.imshow('game', mask)
    #     if cv2.waitKey(33) & 0xFF in (ord('q'), 27):
    #         break

    screen = grab_screen(region=(0, 26, 960, 750))

    hsv_img = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, (140, 68, 0), (161, 133, 255))
    mask = np.array(mask)
    height, width = mask.shape

    # Percorre a tela em áreas de 30x30 e verifica se tem um pixel branco nessa área, o que corresponde à parede
    grid_size = 30
    level_layout = np.zeros((height // grid_size, width // grid_size))
    for i in range(0, height - grid_size, grid_size):
        for j in range(0, width - grid_size, grid_size):
            if 255 in mask[i:i+grid_size, j:j+grid_size]:
                level_layout[i // grid_size , j // grid_size] = 255

    resized_dim = (width, height)
    resized = cv2.resize(level_layout, resized_dim, interpolation = cv2.INTER_AREA)
    while True:
        cv2.imshow('level', resized)
        if cv2.waitKey(33) & 0xFF in (ord('q'), 27):
            break


if __name__ == '__main__':
    main()