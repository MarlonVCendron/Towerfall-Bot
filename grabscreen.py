import numpy as np
import cv2
from mss import mss
from PIL import Image

mon = {'left': 0, 'top': 21, 'width': 950, 'height': 719}

def empty(x):
    pass

# cv2.namedWindow("Parameters")
# cv2.createTrackbar("t1", "Parameters", 0, 255, empty)
# cv2.createTrackbar("t2", "Parameters", 0, 255, empty)

def process_img(img):
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # processed = cv2.cvtColor(processed, cv2.COLOR_RGB2BGR)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # threshold1 = cv2.getTrackbarPos("t1", "Parameters")
    # threshold2 = cv2.getTrackbarPos("t2", "Parameters")

    processed = cv2.Canny(gray_img, 255, 245)
    # ret, thresh = cv2.threshold(processed, 0, 127, 0)
    # contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(processed, contours, -1, (0,255,0), 3)

    mask = cv2.inRange(hsv_img, (95, 0, 0), (100, 255, 255))
    blue = cv2.bitwise_and(img, img, mask=mask)

    indexes = np.where(mask == 255)
    try:
        mean_x = int(np.mean(indexes[1]))
        mean_y = int(np.mean(indexes[0]))
        # processed[mean_x-40:mean_x+40,mean_y-40:mean_y+40] = 255
        cv2.circle(img, (mean_x, mean_y), 40, (20, 50, 240), thickness=5)
    except:
        print('não achou')

    
    return img
    # return cv2.cvtColor(blue, cv2.COLOR_HSV2BGR)


with mss() as sct:
    while True:
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB',
            (screenShot.width, screenShot.height),
            screenShot.rgb,
        )
        img = process_img(img)
        cv2.imshow('game', img)
        if cv2.waitKey(33) & 0xFF in (ord('q'), 27):
            break
