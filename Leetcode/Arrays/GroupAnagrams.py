"""
Difficulty: Medium

Question:

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store similar anagrams
        wordMap = {}
        for i in strs:
            # sort alphabetically
            ordered = ''.join(sorted(i))
            # add to dictionary according to anagram
            if ordered not in wordMap:
                wordMap[ordered] = [i]
                continue
            wordMap[ordered].append(i)
        # return groupings
        return list(wordMap.values())
        