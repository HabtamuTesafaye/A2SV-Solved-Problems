class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345

        n,m = len(grid), len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)

        size = len(arr)

        prefix = [1] * size

        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD

        suffix = [1] * size
        for i  in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD

        res = [[0] * m for _ in range(n)]

        for i in range(size):
            val = (prefix[i] * suffix[i]) % MOD
            r,c = divmod(i, m)
            res[r][c] = val

        return res