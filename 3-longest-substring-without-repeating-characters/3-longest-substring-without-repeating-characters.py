"""
We want the longest substring without repeating characters
- use sliding window that expands each interation and stores all elements and their frequencies in a dict
- shorten the window while (len(dict) > fast - slow + 1)
- keep track of max length and return

 a b c a b c b b 
     s   f

cur_freq = {
    a : 1, 
    b : 1,
    c : 1
}

max_len = 3
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        cur_freq = {}
        max_len = 0
        
        for fast in range(len(s)):
            if s[fast] in cur_freq:
                cur_freq[s[fast]] += 1
            else:
                cur_freq[s[fast]] = 1
            
            while len(cur_freq) < (fast - slow + 1):
                if cur_freq[s[slow]] == 1:
                    cur_freq.pop(s[slow])
                else:
                    cur_freq[s[slow]] -= 1
                slow += 1
            
            max_len = max(max_len, fast - slow + 1)
        
        return max_len