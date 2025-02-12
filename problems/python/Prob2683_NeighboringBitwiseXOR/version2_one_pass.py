class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor_acc = derived[0]
        for d in derived[1:]:
            xor_acc = xor_acc ^ d

        return xor_acc == 0
