'''
19

82
68
100

'''
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        slow = n
        fast = n
        fast = self.gen_happy(self.gen_happy(fast))
        
        while fast != slow:
            fast = self.gen_happy(self.gen_happy(fast))
            slow = self.gen_happy(slow)
            if fast == 1 or slow == 1:
                return True
            
        return False
    
    
    def gen_happy(self, n : int) -> int:
        n_list = [int(c) for c in str(n)]
        happy = 0
        for num in n_list:
            happy += num*num
        return happy