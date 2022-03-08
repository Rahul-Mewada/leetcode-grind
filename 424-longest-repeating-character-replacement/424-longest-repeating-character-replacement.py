"""
we need a way to find out if the substring is valid, ie - that the freq of chars that are not repeating are <= k
    - keep track of the freq of 'main' char, ie - the char with the highest freq
    - (highest_freq - size of the window) gives us freq of non repeating chars- we want this to be <= k
    - adjust the window based off this
    
    
 A  k = 10
sf

cur_freq = {
    A : 1
}

max_len = 1
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow = 0
        cur_freq = {}
        max_len = 0
        max_freq = 0
        
        for fast in range(len(s)):
            if s[fast] in cur_freq:
                cur_freq[s[fast]] += 1
            else:
                cur_freq[s[fast]] = 1
            
            max_freq = max(max_freq, cur_freq[s[fast]])
            
            if ((fast - slow + 1) - max_freq) > k:
                if cur_freq[s[slow]] == 1:
                    cur_freq.pop(s[slow])
                else:
                    cur_freq[s[slow]] -= 1
                slow += 1
            
            max_len = max(max_len, fast - slow + 1)
        return max_len
    
        