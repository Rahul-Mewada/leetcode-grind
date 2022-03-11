'''
We want to find the minimum substring of s such that every character of t is included in it
Sliding Window 
- expand fast until both dicts are equal
- reduce window with slow while both dicts are equal

smallest = 'ADOBEC'
 A D O B E C O D E B A N C  t = A B C
                c     f

cur-freq {
    B : 1
    A : 1
    C : 1
    
}
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        smallest_substring = ""
        min_len = float('inf')
        slow = 0
        t_freq = {}
        cur_freq = {}
        
        for c in t:
            if c in t_freq:
                t_freq[c] += 1
            else:
                t_freq[c] = 1
                
        for fast in range(len(s)):
            if s[fast] in cur_freq and s[fast] in t_freq:
                cur_freq[s[fast]] += 1
            elif s[fast] in t_freq:
                cur_freq[s[fast]] = 1
                
            while self.equal(cur_freq, t_freq):
                if min_len > fast - slow + 1:
                    min_len = fast - slow + 1
                    smallest_substring = s[slow:fast+1]
                if s[slow] in cur_freq and cur_freq[s[slow]] == 1:
                    cur_freq.pop(s[slow])
                elif s[slow] in cur_freq:
                    cur_freq[s[slow]] -= 1
                slow += 1
        return smallest_substring

    def equal(self, cur_freq: dict, t_freq: dict) -> bool:
        if len(cur_freq) != len(t_freq):
            return False
        
        for key, value in cur_freq.items():
            if t_freq[key] > value:
                return False
            
        return True