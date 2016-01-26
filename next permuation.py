__author__ = 'yuyue'


def hello(nums):
    length = len(nums)
    flag = None
    for i in range(length):
        if length - i - 1 > 0:
            if nums[length - i - 2] < nums[length - 1 - i]:
                flag = length - i - 2
                print flag
                break
    if flag is None:
        a = nums[:]
        for i in range(length):
            nums[i] = a[length - 1 - i]
        return
    for i in range(flag, length):
        if nums[length - 1 + flag - i] > nums[flag]:
            t = nums[flag]
            nums[flag] = nums[length - 1 + flag - i]
            nums[length - 1 + flag - i] = t
            break
    tmp = nums[flag + 1:]
    for i in range(flag + 1, length):
        nums[length + flag - i] = tmp[i - flag - 1]
    return
a=[5,4,3,2,1]
hello(a)
print a