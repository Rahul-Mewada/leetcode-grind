'''
"a", t = "a"
 lr
     
rem = 1
{
    a: 1
}

'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        memory = {}
        left = 0
        rem = len(t)
        result = ''
        max_length = len(s)
        
        
        for char in t:
            if char in memory:
                memory[char] += 1
            else:
                memory[char] = 1
                
        for right, char in enumerate(s):
            
            
            if char in memory:
                memory[char] -= 1
                if memory[char] >= 0:
                    rem -= 1
            while(rem == 0 and left <= right):
                temp_length = (right - left) + 1
                if temp_length <= max_length:
                    max_length = temp_length
                    result = s[left: right+1]
                    
                if s[left] in memory:
                    if memory[s[left]] >= 0:
                        rem += 1
                    memory[s[left]] += 1
                left += 1
                
        return result