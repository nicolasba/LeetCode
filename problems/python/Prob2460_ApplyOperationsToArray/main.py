class Solution:
    """
    If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0
    After performing all the operations, shift all the 0's to the end of the array.
    """
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = 2 * nums[i]
                nums[i + 1] = 0

        out = [n for n in nums if n > 0]
        return out + [0] * (len(nums) - len(out))