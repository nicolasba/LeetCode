class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False

        char_count = [0] * 26
        for c in s:
            char_count[ord(c) - ord('a')] += 1

        # Count how many letters appear once or in groups of (if number is odd it's n * 2 + 1)
        # example if 'e' appears 16 times, then single = 0, pairs = 8
        single_count = 0

        for count in char_count:
            if count % 2 == 1:
                single_count += 1     

        # Singles cannot be paired together, if there are more singles than number of palindromes
        # then cannot construct k palindromes
        if single_count > k:
            return False

        # Pairs can be arbitrarily rearranged into desired number of palindromes as long
        # as pairs_count <= (k - single_count) <= 2 * pairs_count
        # If there are (k - single_count) > 2 * pairs_count, there are not enough letters, but this is
        # covered by initial len(s) < k check
        return True        