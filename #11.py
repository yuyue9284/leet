__author__ = 'yuyue'


def solution(height):
    length = len(height)
    start = 0
    stop = length - 1
    maxcontain = min(height[start], height[stop]) * abs(start - stop)
    while start < stop:
        s = abs((height[start] - height[stop]) * (stop - start))
        if s > maxcontain:
            maxcontain = s
        if height[start] > height[stop]:
            stop -= 1
        else:
            start += 1
    return maxcontain