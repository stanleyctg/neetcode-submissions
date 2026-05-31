class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # list of empty [1 -> n]
        # index[nums[i]] + 1 each time we go, go from backwards
        N = len(nums)
        bucket = [[] for _ in range(N)] # [0,0]
        output = []

        unique_nums = list(set(nums)) # [7]
        for uNum in unique_nums:
            bucket[nums.count(uNum) - 1].append(uNum) # [0,7]
        print(bucket)
        for i in range(len(bucket) - 1, -1, -1):
            should_break = False
            if bucket[i] == []:
                continue
            for b in bucket[i]:
                output.append(b)
                if len(output) == k:
                    should_break = True
            if should_break:
                break
                    
        
        return output