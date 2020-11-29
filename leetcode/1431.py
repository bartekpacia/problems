from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        greatest = max(candies)
        for i in range(len(candies)):
            total_candies = candies[i] + extraCandies
            cond = total_candies >= greatest
            print(f"{total_candies} >= {greatest} : {cond}")
            res.append(cond)

        return res


res = Solution().kidsWithCandies([2, 3, 5, 1, 3], 3)
print(res)
