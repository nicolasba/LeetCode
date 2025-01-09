class Solution:
    def grayCode(self, n: int) -> List[int]:
        l = recGrayCode(n)
        return [int(s, 2) for s in l]

def recGrayCode(n):
    l = []
    
    if n == 1:
        return ["0", "1"]
    else:
        prev_substring = recGrayCode(n - 1)
        for s in prev_substring:
            l.append("0" + s)
        for s in prev_substring[::-1]:
            l.append("1" + s)
    return l

        