# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:54:51 2023

@author: Justin Leighton


49. Group Anagrams
Medium
16.7K
479
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        output = {}
        for i in range(0, len(strs)):
            letters = [*strs[i]]
            letters.sort()
            letters = ''.join(letters)
            if letters in output:
                output[letters] += [strs[i]]
            else:
                output[letters] = [strs[i]]      
        return [*output.values()]