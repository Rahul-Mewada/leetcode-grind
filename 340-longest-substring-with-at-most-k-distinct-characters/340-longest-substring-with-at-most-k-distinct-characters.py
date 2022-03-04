'''
 e c e b a
     s f

{
 e: 1
 b: 1
}

num_distinct = 2
max_len = 2

for fast in range(len(s)):
    
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_len = 0
        slow = 0
        char_freq = {}
        num_distinct = 0
        
        for fast in range(len(s)):
            if s[fast] not in char_freq:
                num_distinct += 1
                char_freq[s[fast]] = 1
            else:
                char_freq[s[fast]] += 1
            
            while(num_distinct > k):
                if char_freq[s[slow]] == 1:
                    del char_freq[s[slow]]
                    num_distinct -= 1
                else:
                    char_freq[s[slow]] -= 1
                slow += 1
                
            max_len = max(max_len, fast - slow + 1)
            
        return max_len