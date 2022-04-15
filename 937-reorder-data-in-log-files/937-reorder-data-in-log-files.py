class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digi_logs = []
        letter_logs = []

        for log in logs:
            if self.is_digit(log):
                digi_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key = lambda x : x.split()[0])
        letter_logs.sort(key = lambda x : x.split()[1:])
        letter_logs.extend(digi_logs)
        
        return letter_logs
    
    def is_digit(self, log):
        content = log.split()[1]
        return content.isdigit()