from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        lastNonUniqueIndex = 1
        lastNum = 0

        if len(nums) < 2:
            return len(nums)
        
        lastNum = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            if num != lastNum:
                nums[lastNonUniqueIndex] = num
                lastNonUniqueIndex += 1

            lastNum = num

        return lastNonUniqueIndex