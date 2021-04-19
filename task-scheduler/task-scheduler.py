


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        freq = [0] * 26
        
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
            
        freq.sort()    
        num_spaces = freq[-1] - 1
        idle_slots = num_spaces * n
        
        for index in range(len(freq)-2, -1, -1):
            idle_slots -= min(num_spaces, freq[index])
        
        if idle_slots > 0:
            return idle_slots + len(tasks) 
        else:
            return len(tasks)