class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        current_sum = 0
        max_sum = 0

        for i in range(k):
            current_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i],0) + 1
        if len(freq) == k:
            max_sum = current_sum
        for i in range(k, len(nums)):
            incoming = nums[i]
            current_sum += incoming
            freq[incoming] = freq.get(incoming, 0) + 1

            outgoing = nums[i - k]
            current_sum -= outgoing
            freq[outgoing] -= 1

            if freq[outgoing] == 0:
                del freq[outgoing]
            
            if len(freq) == k:
                if current_sum > max_sum:
                    max_sum = current_sum
            
        return max_sum