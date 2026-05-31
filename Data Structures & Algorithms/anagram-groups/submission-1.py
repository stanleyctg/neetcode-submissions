class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        # Build the dictionary
        group_hash ={}
        for string in strs:
            anagram = ''.join(sorted(string))

            if anagram not in group_hash:
                group_hash[anagram] = [string]
            else:
                group_hash[anagram].append(string)

        output = [group_hash[key] for key in group_hash]
        return output

