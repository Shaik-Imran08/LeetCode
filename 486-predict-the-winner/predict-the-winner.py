class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = nums[:]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                left_pick = nums[i] - dp[i + 1]

                right_pick = nums[j] - dp[i]

                dp[i] = max(left_pick, right_pick)
        return dp[0] >= 0
