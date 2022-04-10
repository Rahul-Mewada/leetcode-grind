'''
 8, 2, 4, 7
s         f
 
 max [8,7] if new number is > tail => pop tail
 min [2,4,7] if new number is < tail => pop tail
 
 max - min = 6 > limit
'''
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque()
        min_q = deque()
        
        l, r = 0, 0
        length = 1
        
        while r < len(nums):
            
            while max_q and nums[max_q[-1]] <= nums[r]:
                max_q.pop()
            
            max_q.append(r)
            
            while min_q and nums[min_q[-1]] >= nums[r]:
                min_q.pop()
            
            min_q.append(r)
            
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                l += 1
                if max_q[0] < l: 
                    max_q.popleft()
                if min_q[0] < l:
                    min_q.popleft()
            
            length = max(length, r - l + 1)
            r += 1
        return length
                    