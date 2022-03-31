'''
 n z p # o # g
             i  
 bs = 2
 
 b # n z p # o # g
                 j     
 bs = 0

'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        s_backspaces = 0
        t_backspaces = 0
        
        while (i >= 0 or j >= 0):
            # if backspace
            
            while i >= 0 and (s[i] == '#' or s_backspaces > 0):
                if s[i] == '#':
                    s_backspaces += 1
                elif s_backspaces > 0:
                    s_backspaces -= 1
                i -= 1
            
            while j >= 0 and (t[j] == '#' or t_backspaces > 0):
                if t[j] == '#':
                    t_backspaces += 1
                elif t_backspaces > 0:
                    t_backspaces -= 1
                j -= 1
                
            if (j < 0 and i >= 0 ) or (i < 0 and j >= 0):
                return False
            
            if (j >= 0 and i >=0) and s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1
            
        return True
        
