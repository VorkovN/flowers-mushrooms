import cv2
import numpy as np
import matplotlib.pyplot as plt


r = 10
r_g = 20
a = 25

img = cv2.imread("gzn.jpg")
#img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
img = cv2.resize(img, (1024, 1024))


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.line(img, (x, y + r), (x, y + r + 60), (0, 255, 0), 5)
        cv2.circle(img, (x, y), r, (0, 255, 255), -1)
        cv2.circle(img, (x, y - 2 * r), r, (0, 0, 255), -1)
        cv2.circle(img, (x + int(2 * r * np.cos(np.deg2rad(18))), y - int(2 * r * np.sin(np.deg2rad(18)))), r, (0, 0, 255), -1)
        cv2.circle(img, (x + int(2 * r * np.cos(np.deg2rad(162))), y - int(2 * r * np.sin(np.deg2rad(162)))), r, (0, 0, 255), -1)
        cv2.circle(img, (x + int(2 * r * np.cos(np.deg2rad(-54))), y - int(2 * r * np.sin(np.deg2rad(-54)))), r, (0, 0, 255), -1)
        cv2.circle(img, (x + int(2 * r * np.cos(np.deg2rad(-126))), y - int(2 * r * np.sin(np.deg2rad(-126)))), r, (0, 0, 255), -1)

        leaf1 = list()
        for i in np.arange(0, 0.78, 0.02):
            leaf1.append([x+a*np.sin(2*i)*np.cos(i), y-a*np.sin(2*i)*np.sin(i)+40])
        l = np.array(leaf1)
        pts = l.reshape(-1, 1, 2)
        cv2.polylines(img, np.int32([pts]), True, (0, 255, 0), 5)

        leaf2 = list()
        for i in np.arange(0, 0.78, 0.02):
            leaf2.append([x-a*np.sin(2*i)*np.cos(i), y-a*np.sin(2*i)*np.sin(i)+50])
        l = np.array(leaf2)
        pts = l.reshape(-1, 1, 2)
        cv2.polylines(img, np.int32([pts]), True, (0, 255, 0), 5)

    elif event == cv2.EVENT_RBUTTONDOWN:

        cv2.line(img, (x, y), (x, y + 40), (200, 200, 200), 15)

        pileus = list()
        for i in np.arange(0, np.pi+0.01, 0.01):
            pileus.append([x + r_g * np.cos(i), y - r_g * np.sin(i)])
        p = np.array(pileus)
        pts = p.reshape(-1, 1, 2)
        cv2.polylines(img, np.int32([pts]), True, (0, 75, 200), 20)



cv2.namedWindow("lol")
cv2.setMouseCallback("lol", draw_circle)

while True:

    cv2.imshow("lol", img)

    if cv2.waitKey(25) & 0xFF == 27:
        break

cv2.destroyAllWindows()
