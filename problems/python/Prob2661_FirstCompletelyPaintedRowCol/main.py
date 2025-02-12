class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        mat_i = [0] * (m*n)
        mat_j = [0] * (m*n)

        rows_count = [0] * m
        cols_count = [0] * n

        # Map values in mat to their indices i and j
        for i in range(m):
            for j in range(n):
                mat_i[mat[i][j] - 1] = i
                mat_j[mat[i][j] - 1] = j

        # Go through arr and count occurences of row i and col j until it reaches max #rows/#cols
        for idx, a in enumerate(arr):
            rows_count[mat_i[a - 1]] += 1
            if rows_count[mat_i[a - 1]] == n:
                return idx
            cols_count[mat_j[a - 1]] += 1
            if cols_count[mat_j[a - 1]] == m:
                return idx
