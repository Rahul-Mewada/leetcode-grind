'''
["3z4"]

'''

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        results = []
        results.append(S)
        self.dfs(S, 0, results)
        return results
    
    def dfs(self, string, index, results):
        if index >= len(string):
            return 
        
        while index <= len(string)-1:
            temp = string
            
            if not temp[index].isnumeric():
                if temp[index].islower():
                    temp = temp[:index] + temp[index].upper() + temp[index + 1:] # makes uppercase
                else:
                    temp = temp[:index] + temp[index].lower() + temp[index + 1:] # makes uppercase
                results.append(temp)
                index += 1
            else:
                index += 1
                continue
            
            self.dfs(temp, index, results)
        
        return 