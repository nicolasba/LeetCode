import math
from typing import List

def search(nums: List[int], target: int) -> int:
    return binarySearch(nums, target, 0, len(nums))

def binarySearch(nums, target, start, end):
    mid = math.floor((start + end) / 2)

    if end < start or start >= len(nums) or end < 0:
        return -1

    if nums[mid] == target:
        return mid
    
    if nums[mid] >= nums[start]:
        if target < nums[mid] and target >= nums[start]:
            return binarySearch(nums, target, start, mid)
        else:
            return binarySearch(nums, target, mid + 1, end)
    elif nums[mid] <= nums[end - 1]:
        if target > nums[mid] and target <= nums[end - 1]:
            return binarySearch(nums, target, mid + 1, end)
        else:
            return binarySearch(nums, target, start, mid)
    else:
        return -1
    
l = [6,1,2,3,4,5]
print(search(l, 2))
