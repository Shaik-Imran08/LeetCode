from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if  k <= 1:
            return 0
        
        left  = 0
        current_product = 1
        total_subarrays = 0

        for right in range(len(nums)):
            current_product *= nums[right]

            while current_product >= k:
                current_product //= nums[left]
                left += 1

            total_subarrays += right - left + 1

        return total_subarrays
        