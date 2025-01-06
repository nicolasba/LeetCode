
from typing import List


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    count_colors = [0,0,0]

    for n in nums:
        count_colors[n] += 1

    nums[:] = [0] * count_colors[0] + [1] * count_colors[1] + [2] * count_colors[2]
    return nums
        
l = [2,0,2,1,1,0]
print(sortColors(l))