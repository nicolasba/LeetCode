class Solution:
    def punishmentNumber(self, n: int) -> int:
        l = []
        
        for i in range(n + 1):
            if self.canBePartitioned(str(i * i), i):
                l.append(i * i)
        
        return sum(l)
        
    def canBePartitioned(self, s, total):
        if int(s) == total:
            return True

        for i in range(1, len(s)):
            s_start = s[:i]

            # Recurse on remaining of the string and check if it can be partitioned to 
            # add up to the total without the first contiguous strings
            if int(s_start) <= total and self.canBePartitioned(s[i:], total - int(s_start)):
                return True

        return False