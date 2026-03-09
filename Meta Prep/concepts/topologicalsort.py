from collections import defaultdict
def canFinish(numCourses: int, prerequisites):
    graph = defaultdict(list)
    
    visited,cycle = set(),set()
    
    for course,prerequisite in prerequisites:
        graph[course].append(prerequisite)
    
    def dfs(crs):
        if crs in visited:
            return True 
        if crs in cycle:
            return False 

        cycle.add(crs)
        for prereq in graph[crs]:
            if dfs(crs) == False:
                return False 
        cycle.remove(crs)
        visited.add(crs)
        return True 
    for crs in range(numCourses):
        if dfs(crs) == False:
            return False 
    return True 
        