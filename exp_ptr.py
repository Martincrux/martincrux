import numpy as np
import time
import cv2

map_bit_str = open("3_1.txt")
map_bit_arr = np.loadtxt(map_bit_str)

img_arr = np.zeros((6496, 6496, 3))

for i in range(203):
    for j in range(203):
        if map_bit_arr[i][j] == 0:
            for x in range(i*32, (i+1)*32 - 1):
                for y in range(j*32, (j+1)*32 - 1):
                    img_arr[x][y] = [255, 255, 255]
        else:
            for x in range(i*32, (i+1)*32 - 1):
                for y in range(j*32, (j+1)*32 - 1):
                    img_arr[x][y] = [0, 0, 0]


cv2.imwrite("3_1_png.png", img_arr)

map_bit_str.close()
