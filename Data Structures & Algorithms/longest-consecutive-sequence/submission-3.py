class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        for num in nums:
            count = 0
            if num - 1 not in nums_set:
                count += 1
                while num + 1 in nums_set:
                    num += 1
                    count += 1
                max_count = max(max_count, count)

        return max_count
