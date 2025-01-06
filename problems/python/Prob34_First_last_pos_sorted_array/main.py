from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    minIndex = maxIndex = binarySearch(nums, target, 0, len(nums))

    while minIndex - 1 >= 0 and nums[minIndex - 1] == target:
        minIndex -= 1

    while maxIndex + 1 < len(nums) and nums[maxIndex + 1] == target:
        maxIndex += 1

    return [minIndex, maxIndex]


def binarySearch(nums, target, start, end):

    if end <= start:
        return -1
    
    mid = (start + end) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearch(nums, target, mid + 1, end)
    else:
        return binarySearch(nums, target, start, mid)
    
l = [5,7,7,8,8,10]
print(searchRange(l, 8))
        