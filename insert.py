__author__ = 'yuyue'


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    stop = len(nums) - 1

    def search(nums, target, start, stop):
        middle = (start + stop) / 2
        if stop - start <= 1:
            if nums[middle] == target:
                return middle
            else:
                print 'a'
                result = middle + 1
                return start
        else:
            if nums[middle] < target:
                search(nums, target, middle, stop)
            elif nums[middle] > target:
                search(nums, target, start, middle)
            elif nums[middle] == target:
                return middle

    if target > nums[stop]:
        return stop + 1
    if target < nums[start]:
        return start

    a=search(nums, target, start, stop)
    return a


a=searchInsert([1, 3, 5], 5)
print a