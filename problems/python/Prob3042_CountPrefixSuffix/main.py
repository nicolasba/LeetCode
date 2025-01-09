class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        words_len = len(words)
        count = 0

        for i in range(words_len):
            for j in range(i + 1, words_len):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count


def isPrefixAndSuffix(subs: str, s: str):
    sub_length = len(subs)
    return len(s) >= sub_length and s[:sub_length] == subs and s[-sub_length:] == subs