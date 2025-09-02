#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict

strs = ["ate", "eat", "tab", "tan", "nat", "bat"]
class Solution:
    def groupAnagrams(self, strs:list[str])-> list[list[str]]:
        anagram_map = defaultdict(list)
        
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        return list(anagram_map.values())  
    
soln1 = Solution()
print(soln1.groupAnagrams( ["ate", "eat", "tab", "tan", "nat", "bat"]))    