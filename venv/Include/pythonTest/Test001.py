#coding=utf-8
import itertools
temp_arr = list(itertools.permutations([1, 2, 3, 4, 5], 4)) # 排列  # A_4^3 = (4)!/(4-3)! = (4*3*2*1)/1 = 24
arr = [100*t[0]+10*t[1]+t[2] for t in temp_arr]
print(len(arr),arr)
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            string = '%d*%d=%d' % (j, i, j * i)
            print('%-7s' % string, end='')
    print('')