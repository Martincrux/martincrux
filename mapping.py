import numpy as np

file_tmp = open('3.txt')
data_tmp = file_tmp.read()

data = data_tmp.replace(" ", "0")
data = data.replace('0', '0 ')
data = data.replace('1', '1 ')

# print(data)
file_tmp.close()

with open('3_1.txt', 'a') as f:
    f.write(data)
