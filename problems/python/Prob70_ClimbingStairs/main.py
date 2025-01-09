class Solution:
    def climbStairs(self, n: int) -> int:
        
        climb_combinations = [0] * 46
        
        climb_combinations[1] = 1
        climb_combinations[2] = 2

        for i in range(3, n + 1):
            climb_combinations[i] = climb_combinations[i - 1] + climb_combinations[i - 2]

        return climb_combinations[n]