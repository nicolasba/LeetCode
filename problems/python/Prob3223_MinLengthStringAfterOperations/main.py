class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        min_count = 0

        for c in counter:
            if counter[c] != 0:
                if counter[c] % 2 == 0:
                    min_count += 2
                else:
                    min_count += 1
                    
        return min_count
                