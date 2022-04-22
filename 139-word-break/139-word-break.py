'''
 a b c d      [a, abc, b, cd]
 i
 T T T - T
 0 1 2 3 4 5 6 7 8 9

- if there is a word that starts at index i and ends at t (where t + 1 == T)
    then cache[i] = True
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False] * (len(s) + 1)
        cache[-1] = True
        
        for i in reversed(range(len(s))):
            for word in wordDict:
                # if dis between i and len(list) + 1 >= len(word) and s[i : len(word)] == word
                if (len(s) - i) >= len(word) and word == s[i : (i+len(word))] and cache[i] != cache[i + len(word)]:
                    cache[i] = cache[i + len(word)]
                    break
                    
        print(cache)
        return cache[0]
        
        
        
                
        