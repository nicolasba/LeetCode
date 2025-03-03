class Solution:
    """
    Rearranges nums such that the following conditions are satisfied:

    - Every element less than pivot appears before every element greater than pivot.
    - Every element equal to pivot appears in between the elements less than and greater than pivot.
    - The relative order of the elements less than pivot and the elements greater than pivot is maintained.
    """
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [n for n in nums if n < pivot] + \
            [n for n in nums if n == pivot] + \
            [n for n in nums if n > pivot]