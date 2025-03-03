class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        out = ""

        # Construct output string diagonally
        for i, n in enumerate(nums):
            out += "1" if n[i] == '0' else "0"

        return out
