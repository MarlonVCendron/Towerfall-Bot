import cv2
from grabscreen import grab_screen

def empty(x):
    pass

def main():
    
    while True:
        screen = grab_screen(region=(0, 40, 960, 740))


        hsv_img = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_img, (160, 30, 0), (165, 100, 100))
        filtered = cv2.bitwise_and(screen, screen, mask=mask)

        cv2.imshow('game', filtered)

        if cv2.waitKey(33) & 0xFF in (ord('q'), 27):
            break


if __name__ == '__main__':
    main()