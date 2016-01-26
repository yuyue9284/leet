__author__ = 'yuyue'


def search(nums, target, i, j, start, stop):
    middle = (i + j) / 2
    if j - i > 1:
        if nums[middle] > target:
            search(nums, target, i, middle, start, stop)
        elif nums[middle] < target:
            search(nums, target, middle, j, start, stop)
        elif nums[middle] == target:
            if middle < start[0]:
                start[0] = middle
            if middle > stop[0]:
                stop[0] = middle
            search(nums, target, i, middle, start, stop)
            search(nums, target, middle, j, start, stop)
    else:
        if nums[j] == target:
            if j > stop[0]:
                stop[0] = j
        if nums[i] == target:
            if i < start[0]:
                start[0] = i


nums = [1, 3, 4, 5, 6, 7]

start = [len(nums)]
stop = [-1]

search(nums,4,0,start[0]-1,start,stop)

print start
print stop