class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the sorted array where it includes the target number
        # find the middle, if target is in between left and middle then move right ptr
        # if target is in between middle and right then move left pointer and keep going
        if not nums:
            return -1
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            
            # check sorted halves
            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1 

        return -1