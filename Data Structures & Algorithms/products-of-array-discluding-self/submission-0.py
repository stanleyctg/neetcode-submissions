class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get prefix of suffix of nums
        N = len(nums)
        pref, suff = [1] * (N+1), [1] * (N+1)

        for i in range(N):
            pref[i + 1] = pref[i] * nums[i]
            suff[i + 1] = suff[i] * nums[N - 1 - i]
        
        res = [1] * N
        for i in range(N):
            res[i] = pref[i] * suff[N-1-i]
        
        return res