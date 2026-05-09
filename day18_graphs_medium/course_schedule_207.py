class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):

            if not dfs(course):
                return False

        return True

if __name__ == "__main__":
    numCourses = 4
    prerequisites = [
        [1, 0],
        [2, 1],
        [3, 2] ]
    sol = Solution()
    result = sol.canFinish(numCourses, prerequisites)
    print("Can Finish All Courses:", result)