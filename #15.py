__author__ = 'yuyue'


def solution(nums):
    snums = sorted(nums)
    length = len(snums)
    result = []
    for t in range(length):
        j = length - 1
        i = t + 1
        while i < j:
            if j == t or snums[i] + snums[j] > -snums[t]:
                j -= 1
            elif i == t or snums[i] + snums[j] < -snums[t]:
                i += 1
            else:
                result.append([snums[t], snums[i], snums[j]])
                while i < j and snums[i] == snums[i + 1]:
                    i += 1
                while t < length - 1 and snums[t] == snums[t + 1]:
                    t += 1
                if i < j:
                    i += 1

    return result


print solution(
    [-1, 0, 1])
