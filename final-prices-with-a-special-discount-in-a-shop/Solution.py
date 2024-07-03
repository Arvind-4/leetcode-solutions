// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            result.append(prices[i]-discount)
        return result
        