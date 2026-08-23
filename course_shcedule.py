# Tags: dfs, graph

from typing import List, Set

# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# The pair [0, 1], indicates that must take course 1 before taking course 0.

# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return true if it is possible to finish all courses, otherwise return false.

# Constraints:

# 1 <= numCourses <= 1000
# 0 <= prerequisites.length <= 1000
# prerequisites[i].length == 2
# 0 <= a[i], b[i] < numCourses
# All prerequisite pairs are unique.


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cache = {}
        for pre in prerequisites:
            if pre[0] not in cache:
                cache[pre[0]] = []
            cache[pre[0]].append(pre[1])
        
        taken = set()
        def takeCourse(course: int, visited: Set[int]) -> bool:
            if course in taken or course not in cache:
                return True
            if course in visited:
                return False
            visited.add(course)
            to_take_list = cache[course]
            for to_take in to_take_list:
                if not takeCourse(to_take, visited):
                    return False
            taken.add(course)
            return True
        
        for pre in prerequisites:
            if not takeCourse(pre[0], set()):
                return False
        return True
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     preCache = {}
    #     for pre in prerequisites:
    #         if pre[0] not in preCache:
    #             preCache[pre[0]] = set()
    #         preCache[pre[0]].add(pre[1])
            
    #     cache={}
    #     def dfs(courseNo: int, visited) -> bool:
    #         visited.add(courseNo)
    #         if courseNo in cache:
    #             return cache[courseNo]
    #         res = True
    #         if courseNo in preCache:
    #             for p in preCache[courseNo]:
    #                 if p in visited:
    #                     res = False
    #                     break
    #                 res = dfs(p, visited)
    #                 visited.remove(p)
    #                 if not res:
    #                     break
    #         cache[courseNo] = res
    #         return res
        
    #     for i in range(numCourses):
    #         if not dfs(i, set()):
    #             return False
            
    #     return True
    
if '__main__' == __name__:
    sol = Solution()
    # print(sol.canFinish(numCourses = 2, prerequisites = [[0,1]]))
    # print(sol.canFinish(numCourses = 2, prerequisites = [[0,1],[1,0]]))
    print(sol.canFinish(numCourses = 3, prerequisites = [[1,0],[1,2],[0,1]]))
