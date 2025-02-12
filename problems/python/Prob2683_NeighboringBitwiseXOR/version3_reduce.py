class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(lambda d1, d2: d1 ^ d2, derived) == 0
