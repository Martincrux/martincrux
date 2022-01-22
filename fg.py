import numpy as np
import time
import cv2

map_bit_str = open("Maze_1(1).txt")
map_bit_arr = np.loadtxt(map_bit_str)

img_arr = np.zeros((215*32, 215*32, 3))
tham_do = cv2.imread('tham_do.png')
san = cv2.imread('san.png')
banh_chung = cv2.imread('BanhChung (1).png')
tuong = cv2.imread('tuong.png')


for i in range(215):
    for j in range(215):
        if map_bit_arr[i][j] == 0:
            for x in range(i*32, (i+1)*32):
                for y in range(j*32, (j+1)*32):
                    img_arr[x][y] = [0, 0, 0]
        elif map_bit_arr[i][j] == 2:
            for x in range(i*32, (i+1)*32):
                for y in range(j*32, (j+1)*32):
                    img_arr[x][y] = [0, 0, 0]
        elif map_bit_arr[i][j] == 4:
            for x in range(i*32, (i+1)*32):
                for y in range(j*32, (j+1)*32):
                    img_arr[x][y] = [0, 0, 0]

for i in range(215):
    for j in range(215):
        if map_bit_arr[i][j] == 1:
            if i == 214:
                for x in range(i*32, (i+1)*32):
                    for y in range(j*32, (j+1)*32):
                        banh_chung[x % 32][y % 32]
                        img_arr[x][y] = banh_chung[x % 32][y % 32]
            # elif map_bit_arr[i+1][j] != 1:
            else:
                x_1 = 0
                for x in range(i*32, (i+1)*32):
                    for y in range(j*32, (j+1)*32):
                        # if x_1 >= 32:
                        img_arr[x][y] = banh_chung[x_1][y % 32]
                    x_1 = x_1 + 1

        elif map_bit_arr[i][j] == 3:
            if i == 214:
                for x in range(i*32, (i+1)*32):
                    for y in range(j*32, (j+1)*32):
                        img_arr[x][y] = [0, 0, 0]
            else:
                x_1 = 0
                for x in range(i*32, (i+1)*32 + 12):
                    for y in range(j*32, (j+1)*32):
                        img_arr[x][y] = [0, 0, 0]
                    x_1 = x_1 + 1

cv2.imwrite("fg.png", img_arr)

map_bit_str.close()
