'''
[A A A A B B B B C C] n = 3
[B1 C2]
A---A---A---A

1) Keep track of the maximum freq
2) num_slots = n * (freq - 1) and gaps = max_freq - 1
3) fill the slots with the next max freq
'''


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = [0] * 26
        
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort(reverse=True)
        
        max_freq = freq[0]
        gaps = max_freq - 1 
        idle_time = n * gaps
        
        for index in range(1, len(freq)):
            cur_freq = freq[index]
            idle_time -= min(gaps, cur_freq)
            
        idle_time = max(idle_time, 0)
        return idle_time + len(tasks)
        