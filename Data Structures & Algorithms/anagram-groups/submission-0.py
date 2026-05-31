class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        # sort the strs
        group_hash ={}
        for string in strs:
            anagram_char = sorted(string)
            anagram = ''.join(anagram_char)
            if anagram not in group_hash:
                group_hash[anagram] = [string]
            else:
                group_hash[anagram].append(string)
        
        print(group_hash)
        output = [group_hash[key] for key in group_hash]

        return output

