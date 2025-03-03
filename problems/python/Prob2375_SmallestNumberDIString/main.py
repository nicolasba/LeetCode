class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Presorted list of numbers from 1 to 9
        avail_nums = list(range(1, 10))

        out = self.recDIString(avail_nums, avail_nums, pattern, "")
        return out

    def recDIString(self, avail_nums_all, avail_nums_curr, pattern, acc):
        """
        avail_nums_all: the remaining set of numbers to complete a full sequence
        avail_nums_curr: the set of numbers that can be used in the current iteration
                       to satisfy the "D"/"I" condition
        pattern: subset of pattern (first element is the condition for the current iteration)
        acc: accumulated sequence so far
        """ 
        for n in avail_nums_curr:
            if len(pattern) > 0:
                p = pattern[0]
            else:
                return acc + str(n)
            
            tmp_avail_nums_all = avail_nums_all[:]
            tmp_avail_nums_all.remove(n)
            out = None
            
            if p == 'D':
                next_iter_avail_nums = [avail_num for avail_num in tmp_avail_nums_all if avail_num < n]
                out = self.recDIString(tmp_avail_nums_all, next_iter_avail_nums, pattern[1:], acc + str(n))
            else:
                next_iter_avail_nums = [avail_num for avail_num in tmp_avail_nums_all if avail_num > n]
                out = self.recDIString(tmp_avail_nums_all, next_iter_avail_nums, pattern[1:], acc + str(n))

            if out is not None:
                return out

        return None

