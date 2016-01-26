__author__ = 'yuyue'


def permuation(nums, tmp, pos, result, length,not_used,used):
    if pos >= length:
        result.append(tmp[:])
        return

    for i in not_used:
            tmp[i] = nums[pos]
            used.append(i)
            permuation(nums, tmp, pos + 1, result, length,not_used,used)
            tmp[i] = None
    return


nums = [1, 2, 3]

length = len(nums)
not_used = [i for i in range(length)]
used = []
tmp = [None for i in range(length)]
result = []

permuation(nums, tmp, 0, result, length)

print result
