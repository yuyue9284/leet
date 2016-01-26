__author__ = 'yuyue'


def solution(array):
    maxsub = array[0]
    f = []
    f.append(array[0])
    length = len(array)
    for i in range(1, length):
        if f[i - 1] > 0:
            f.append(f[i-1] + array[i])
        else:
            f.append(array[i])
        if f[i] > maxsub:
            maxsub = f[i]
    return maxsub


print solution([-2,1,-3,4,-1,2,1,-5,4])
