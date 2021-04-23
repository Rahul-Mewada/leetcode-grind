'''
"e c e b a"
       l r
'''
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0, 0
        char_count = {}
        num_distinct = 0
        max_length = 0
        
        for right, char in enumerate(s):
            print(char)
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            
            while(len(char_count) > 2):
                print(char_count)
                char_count[s[left]] -= 1
                if char_count[s[left]] <= 0:
                    del(char_count[s[left]])
                left += 1
            
            max_length = max(max_length, (right-left+1))
        return max_length