from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def subarrays_with_at_most_k(max_distinct: int) -> int:
            if max_distinct == 0:
                return 0
            freq = {}
            left = 0
            total_subarrays = 0

            for right in range(len(nums)):
                freq[nums[right]] = freq.get(nums[right], 0) + 1

                while len(freq) > max_distinct:
                    freq[nums[left]]  -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                total_subarrays += right - left + 1
            return total_subarrays
        return subarrays_with_at_most_k(k) - subarrays_with_at_most_k(k - 1)

        