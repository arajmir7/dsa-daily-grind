class Solution(object):
    def majorityElement(self, A: list[int])->int:
        count = 0
        element = None
        for num in A:
            if count == 0:
                element = num
                count = 1
            elif num == element:
                count += 1
            else:
                count -= 1
        if A.count(element) > len(A)//2:
            return element
        return -1
A = [2,2,1,1,1,2,2,1,3,3,1,1,1,1]
sol = Solution()
ans = sol.majorityElement(A)
print("Array: ", A)
print("Majority element: ", ans)