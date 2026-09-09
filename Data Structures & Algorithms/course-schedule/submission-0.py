class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for course, pre in prerequisites: 
            prereq[course].append(pre)

        visit = set() 
        def dfs(course): 
            if course in visit: 
                return False 
            if prereq[course] == []:
                return True 
            visit.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False: 
                    return False 
            visit.remove(course)
            prereq[course] = []
            return True 

        for c in range(numCourses): 
            if dfs(c) == False:
                return False 
        return True 