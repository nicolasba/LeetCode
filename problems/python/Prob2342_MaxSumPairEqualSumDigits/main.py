class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # For example, given nums = [11,22,33]
        # sum_digits_list = [(2, 11), (4,22), (6, 33)]
        sum_digits_list = [(sum([int(c) for c in str(n)]), n) for n in nums]
        
        # The sum of digits in a number will not exceed 82
        sum_buckets = [[] for i in range(100)]
        
        # Numbers will be added to the buckets corresponding to the sum of their digits
        for sum_d, num in sum_digits_list:
            sum_buckets[sum_d].append(num)

        print(sum_buckets)

        maxSum = -1
        for sum_list in sum_buckets:
            if len(sum_list) >= 2:
                sum_list.sort()
                if sum(sum_list[-2:]) > maxSum:
                    maxSum = sum(sum_list[-2:])

        return maxSum
        