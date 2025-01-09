class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Transpose along diagonal bottom-left to top-right diagonal
        for i in range(num_rows):
            for j in range(num_cols - 1 - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[num_rows - 1 - j][num_cols - 1 - i]
                matrix[num_rows - 1 - j][num_cols - 1 - i] = tmp

        matrix.reverse()
        
