import cv2
import numpy as np
import time
video = cv2.VideoCapture(0)
time.sleep(2)

background = 0 
for i in range(60):
    ret,background=video.read()

background=np.flip(background, axis=1)

while True:
    ret,img=video.read()
    img=np.flip(img, axis=1)
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blur=cv2.GaussianBlur(hsv, (11,11), 0)

    lower=np.array([0,150,120])
    upper=np.array([10,255,255])
    mask01=cv2.inRange(blur, lower, upper)

    lower_red=np.array([170,150,120])
    upper_red=np.array([180,255,255])

    mask02=cv2.inRange(blur, lower_red, upper_red)

    mask = cv2.bitwise_or(mask01, mask02)

    kernel = np.ones((7,7), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=2)

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask)

    new_mask = np.zeros_like(mask)

    for i in range(1, num_labels):  # Skip background (label 0)
        if stats[i, cv2.CC_STAT_AREA] > 800:
            new_mask[labels == i] = 255

    mask = new_mask 

    img[np.where(mask == 255)] = background[np.where(mask == 255)]


    cv2.imshow("Display", img)
        
    k=cv2.waitKey (1)
    if k==ord('d'):
        break
video.release()
cv2.destroyAllWindows() 