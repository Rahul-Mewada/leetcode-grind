class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        num_ones = 0
        num_flips = 0
        for number in s:
            if number == '1':
                num_ones += 1
                continue
            num_flips = min(num_flips + 1, num_ones)
        
        return num_flips