"""
we want to check if s2 contains a permutation of s1
    - we are just checking if there is a substring in s2 that contains all the chars of s1
- create a global_freq for s1
- when you encounter the first match, initialize a slow pointer
    - generate a cur_freq that maps elements
    - adding elements
    - if there is a mismatch, shrink the window and substract that elemement
    - if all elements match return true else continue
- return false by default

 a a b c b b a b a a c a a b b        perm = a a b b 
           s     f

cur_freq = {
   b : 2
   a : 1
}

perm = {
    a : 2
    b : 2
}
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        perm = {}
        for c in s1:
            if c in perm:
                perm[c] += 1
            else:
                perm[c] = 1
        slow = 0
        cur_freq = {}
        
        for fast in range(len(s2)):
            if s2[fast] in perm:
                if s2[fast] in cur_freq:
                    cur_freq[s2[fast]] += 1
                else:
                    cur_freq[s2[fast]] = 1
                    
                while cur_freq[s2[fast]] > perm[s2[fast]]:
                    if cur_freq[s2[slow]] == 1:
                        cur_freq.pop(s2[slow])
                    else:
                        cur_freq[s2[slow]] -= 1
                    slow += 1
                
                if self.dicts_equal(perm, cur_freq):
                    return True
            else:
                slow = fast + 1
                cur_freq.clear()
        
        return False
    
    def dicts_equal(self, perm, cur_freq):
        if len(perm) != len(cur_freq):
            return False
        
        for key, value in cur_freq.items():
            if value != perm[key]:
                return False
        return True