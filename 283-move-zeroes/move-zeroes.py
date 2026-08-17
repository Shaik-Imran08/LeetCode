class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        last_non_zero_found_at = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                
                last_non_zero_found_at += 1
