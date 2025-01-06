from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    for i, num in enumerate(nums):
        if type(num) == bool:
            continue
        elif num != (i + 1):
            tmp = num
            nums[i] = False
            recReplace(nums, tmp - 1)
        else:
            nums[i] = True

    for i, occupied in enumerate(nums):
        if not occupied:
            return i + 1

    return len(nums) + 1
        
        
def recReplace(nums, i):
    if type(i) == bool:
        return
    elif i >= len(nums) or i < 0 or nums[i] is True:
        return
    else:
        tmp = nums[i]
        nums[i] = True
        recReplace(nums, tmp - 1)


l = [2,1]
print(firstMissingPositive(l))


        