class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        out = []

        # Presorted list of available letters
        self.recConstructHappyString(['a','b','c'], n, k, "", out)

        if len(out) < k:
            return ""
        else:
            return out[k - 1]
        
    def recConstructHappyString(self, avail_letters, n, k, acc, list_strings):
        if len(list_strings) >= k:
            return

        if len(acc) >= n:
            list_strings.append(acc)
            return

        # By starting with the first available letter at every iteration. the constructed
        # string is guaranteed to be in lexicographical order
        for letter in avail_letters:
            if letter == 'a':
                self.recConstructHappyString(['b', 'c'], n, k, acc + letter, list_strings)
            elif letter == 'b':
                self.recConstructHappyString(['a', 'c'], n, k, acc + letter, list_strings)
            else:
                self.recConstructHappyString(['a', 'b'], n, k, acc + letter, list_strings)
