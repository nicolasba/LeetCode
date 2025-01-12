from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False

        # Count how many letters appear an odd number of times
        char_count = Counter(s)
        odd_count = sum(1 for count in char_count.values() if count % 2 == 1)

        # Singles cannot be paired together, if there are more singles than number of palindromes
        # then cannot construct k palindromes
        if odd_count > k:
            return False

        # Pairs can be arbitrarily rearranged into desired number of palindromes as long
        # as pairs_count <= (k - single_count) <= 2 * pairs_count
        # If there are (k - single_count) > 2 * pairs_count, there are not enough letters, but this is
        # covered by initial len(s) < k check
        return True        