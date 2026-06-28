from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        

        for schedule in prerequisites: #[1,0] (course,prereq)
            course,prereq = schedule
            graph[course].append(prereq) 

        output = []
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True 
    
            cycle.add(crs)
            for pre in graph[crs]:
                if dfs(pre) == False:
                    cycle.remove(crs)
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True 

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output

            



