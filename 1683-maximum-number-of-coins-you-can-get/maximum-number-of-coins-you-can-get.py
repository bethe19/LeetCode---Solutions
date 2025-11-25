class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        coins = 0
        for i in range(1, len(piles), 2):
            if i >= len(piles) // 3 * 2:
                break
            coins += piles[i]
        return coins
