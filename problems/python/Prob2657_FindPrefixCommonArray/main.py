class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        not_matched_A = []
        not_matched_B = []
        count = 0
        ret = []

        for a, b in list(zip(A, B)):
            if a == b:
                count += 1
            else:
                if a in not_matched_B:
                    count += 1
                    not_matched_B.remove(a)
                else:
                    not_matched_A.append(a)

                if b in not_matched_A:
                    count += 1
                    not_matched_A.remove(b)
                else:
                    not_matched_B.append(b)
            ret.append(count)

        return ret


        