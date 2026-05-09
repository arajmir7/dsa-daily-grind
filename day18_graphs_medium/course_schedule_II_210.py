class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()
        visited = set()
        order = []

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
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order

if __name__ == "__main__":
    numCourses = 4
    prerequisites = [
        [1, 0],
        [2, 0],
        [3, 1],
        [3, 2] ]
    sol = Solution()
    result = sol.findOrder(numCourses, prerequisites)
    print("Course Order:", result)