'''
 a b b b c c d d d e e
 
 [3,3,2,2,1]
 [3,2,1,0,0]
 
 min = 5
 
 time complexity = O(n) where n = size of input, space is O(1) since number of english letters is constant
'''
class Solution:
    def minDeletions(self, s: str) -> int:
        char_freq = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            char_freq[index] += 1
        
        char_freq.sort(reverse = True)
        min_deletions = 0
        for i in range(1, len(char_freq)):
            prev_freq = char_freq[i - 1]
            cur_freq = char_freq[i]
            
            if cur_freq == 0:
                break
            
            if prev_freq <= cur_freq:
                if prev_freq == 0:
                    diff = cur_freq
                else:
                    diff = cur_freq - prev_freq + 1
                char_freq[i] -= diff
                min_deletions += diff
                
        return min_deletions
        