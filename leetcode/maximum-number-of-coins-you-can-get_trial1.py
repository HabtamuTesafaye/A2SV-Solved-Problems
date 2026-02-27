class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3

        left = 0
        right = len(piles) - 1
        coins = 0

        for _ in range(n):
            # alice takes one the right first
            right -= 1

            # i take one after alice
            coins += piles[right]
            right -= 1

            # bob takes one on the left
            left += 1

        return coins
