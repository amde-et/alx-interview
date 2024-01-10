from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        price = 0
        counter = 0
        for i in costs:
            if price + i <= coins:
                price += i  # Update the total price
                counter += 1
            else:
                return counter
        return counter
