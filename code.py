class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d=collections.defaultdict()
        words=s.split()
        if len(pattern)!=len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if words[i] in d.values():
                    return False  
                d[pattern[i]]=words[i]
            else:
                if words[i]!=d[pattern[i]]:
                    return False
        return True
