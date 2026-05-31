class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        bucket = [[] for _ in range(N)]
        output = []
        freq = {}

        unique_nums = list(set(nums))
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for uNum in unique_nums:
            bucket[freq[uNum]-1].append(uNum)

        for i in range(len(bucket) - 1, -1, -1):
            should_break = False
            if bucket[i] == []:
                continue

            for b in bucket[i]:
                output.append(b)
                if len(output) == k:
                    should_break = True
                    break

            if should_break:
                break
        
        return output