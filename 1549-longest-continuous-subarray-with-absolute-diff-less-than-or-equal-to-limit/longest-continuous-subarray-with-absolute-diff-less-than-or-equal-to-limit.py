class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_ques = deque()
        min_ques = deque()
        left = 0
        count =0 

        for right in range(len(nums)):
            while max_ques and nums[max_ques[-1]] <= nums[right]:
                max_ques.pop()
            max_ques.append(right)

            while min_ques and nums[min_ques[-1]] >= nums[right]:
                min_ques.pop()
            min_ques.append(right)

            while (nums[max_ques[0]] -  nums[min_ques[0]]) > limit:
                left += 1
                if max_ques[0] < left:
                    max_ques.popleft()
                if min_ques[0] < left:
                    min_ques.popleft()

            count = max(count, right - left + 1)

        return count
            