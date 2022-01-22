import numpy as np
import time
import cv2

map_bit_str = open("3_1.txt")
map_bit_arr = np.loadtxt(map_bit_str)

img_arr = np.zeros((6496, 6496, 3))
block = cv2.imread('BanhChung.png')

for i in range(203):
    for j in range(203):
        if map_bit_arr[i][j] == 0:
            for x in range(i*32, (i+1)*32):
                for y in range(j*32, (j+1)*32):
                    img_arr[x][y] = [200, 212, 163]
        else:
            for x in range(i*32, (i+1)*32):
                for y in range(j*32, (j+1)*32):
                    img_arr[x][y] = block[x % 32][y % 32]


cv2.imwrite("map_tmp.png", img_arr)

map_bit_str.close()
