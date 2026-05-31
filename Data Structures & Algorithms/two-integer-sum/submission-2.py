class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_diff = {}
        for i, n in enumerate(nums):
            if n in hash_diff:
                return [hash_diff[n], i]
            hash_diff[target - n] = i