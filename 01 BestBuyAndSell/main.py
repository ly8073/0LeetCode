from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        自己的想法：双指针
        实际：动态规划，DP
        dp[i][0]表示第i+1天交易完之后手中没有股票的最大利润，dp[i][1]表示第i+1天交易之后手中有股票的最大利润

        递推公式：dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - price[i])
        :param prices:
        :return:
        """
        if prices is None or len(prices) < 2:
            return 0

        dp = [[0, -prices[0]]]
        for i in range(1, len(prices)):
            no_shares = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            with_shares = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp.append([no_shares, with_shares])

        return dp[len(prices) - 1][0]


if __name__ =="__main__":
    solution = Solution()
    max_profit = solution.maxProfit([7,1,5,3,6,4])
    print(max_profit)