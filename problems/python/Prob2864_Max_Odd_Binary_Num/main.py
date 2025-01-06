from functools import reduce

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_ones = sum(c == '1' for c in s)
    
        ret = "1" * (num_ones - 1)
        ret += "0" * (len(s) - num_ones)
        ret += "1"
        
        return ret