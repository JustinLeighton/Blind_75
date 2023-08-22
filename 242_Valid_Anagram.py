# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:44:03 2023

@author: Justin Leighton


242. Valid Anagram
Easy
10.2K
322
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s = list(s); s.sort()
        t = list(t); t.sort()
        for i in range(0,len(s)):
            if s[i]!=t[i]:
                return False
        return True
    
s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s,t))