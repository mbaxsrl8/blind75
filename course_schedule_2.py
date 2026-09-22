# Tags: depth-first-search, graph, needs-review
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        prerequisites_by_course = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            prerequisites_by_course[course].append(prerequisite)

        # 0: unvisited  1: visiting 2. visited
        state = [0] * numCourses
        order = []

        def dfs(course: int) -> bool:
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for pre_course in prerequisites_by_course[course]:
                previous = dfs(pre_course)
                if not previous:
                    return False
            state[course] = 2
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return order


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.findOrder(
            numCourses=8,
            prerequisites=[
                [0, 1],
                [0, 2],
                [1, 3],
                [2, 3],
                [3, 4],
                [3, 5],
                [6, 0],
                [7, 0],
            ],
        )
    )
