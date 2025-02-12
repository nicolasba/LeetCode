class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = s.find(part)
        
        while i >= 0:
            s = s[0:i] + s[i + len(part):]
            i = s.find(part)
        return s