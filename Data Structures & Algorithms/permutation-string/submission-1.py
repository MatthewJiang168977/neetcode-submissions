class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        perm1 = defaultdict(int)
        perm2 = defaultdict(int)
        l = 0 
        for i in s1: 
            perm1[i] += 1 
        for j in range(len(s1)): 
            perm2[s2[j]] += 1
        print(perm2)
        if perm1 == perm2: 
            return True 
        
        for r in range(len(s1), len(s2)): 
            perm2[s2[r]]+=1
            perm2[s2[l]] -= 1

            if perm2[s2[l]] == 0:
                del perm2[s2[l]]
            l += 1
            
            if perm1 == perm2: 
                return True 
        return False 

        