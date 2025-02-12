class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        sum_0 = sum(grid[0][1:])
        sum_1 = 0
        min_score_robot_two = sum_0

        for i in range(n):
            # For each column, the second robot has to choose between the max sum of points to
            # the right or bottom->right (excluding grid[1][n-1] because robot #1 will turn into 0)
            current_optimal_robot_two = max(sum_0, sum_1)

            # Select the minimum of the optimal choices from all columns
            if current_optimal_robot_two < min_score_robot_two:
                min_score_robot_two = current_optimal_robot_two

            if i < n - 1:
                sum_0 -= grid[0][i + 1]
                sum_1 += grid[1][i]

        return min_score_robot_two