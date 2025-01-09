class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0

        for w in words:
            if len(w) >= len(pref) and w[:len(pref)] == pref: 
                count += 1
        
        return count