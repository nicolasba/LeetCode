class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:    
        avail_nums = list(range(n, 0, -1))  # Pre-sort nums highest to lowest
        out = [0] * (2*n - 1)   # Elem=0 means index has not been assigned a value yet
        
        return self.recConstructDistancedSequence(avail_nums, out)

    def recConstructDistancedSequence(self, avail_nums, acc):
        if not avail_nums:
            return acc

        # Find first unassigned index
        idx = acc.index(0)
        for num in avail_nums:
            tmp_acc = acc[:]
            tmp_avail_nums = avail_nums[:]
            tmp_acc[idx] = num

            if num > 1:
                if idx + num < len(tmp_acc) and tmp_acc[idx + num] == 0:
                    tmp_acc[idx + num] = num
                else:
                    # Forced to place num at fixed distance, if another number is already
                    # placed there, we can't place num there
                    continue

            tmp_avail_nums.remove(num)
            out = self.recConstructDistancedSequence(tmp_avail_nums, tmp_acc)

            if out is not None:
                return out

        return None