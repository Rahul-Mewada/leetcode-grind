'''
 1, 3,-1,-3, 5, 3, 6, 7
l      r

q = [3,-1]

'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        r,l = 0,0
        results = []
        
        while r < len(nums):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if r - l + 1 == k:
                results.append(nums[q[0]])
                l+=1
                
            r += 1
                
        return results