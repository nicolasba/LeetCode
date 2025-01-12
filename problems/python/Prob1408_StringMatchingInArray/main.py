class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = []
        for i, w in enumerate(words):
            for w2 in words[0:i] + words[i + 1:]:
                if w in l:
                    break 
                if w in w2:
                    l.append(w)
        return l