class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
            freq = defaultdict(int)
            window_sum = 0
            max_sum = 0

            for i in range(len(nums)):
                # Add right element
                freq[nums[i]] += 1
                window_sum += nums[i]

                # Remove left element when window exceeds k
                if i >= k:
                    left = nums[i - k]
                    window_sum -= left
                    freq[left] -= 1
                    if freq[left] == 0:
                        del freq[left]

                # Valid window: size == k and all distinct
                if i >= k - 1 and len(freq) == k:
                    max_sum = max(max_sum, window_sum)

            return max_sum
