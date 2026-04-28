class Solution(object):
    def threeSum(self, A):
        A.sort()
        result = []

        for i in range(len(A)):
            if i > 0 and A[i] == A[i-1]:
                continue
            left = i+1
            right = len(A)-1

            while left < right:
                total = A[i] + A[left] + A[right]
                
                if total == 0:
                    result.append([A[i], A[left], A[right]])
                    left += 1
                    right -= 1
                    while left < right and A[left] == A[left-1]:
                        left += 1
                    
                    while left < right and A[right] == A[right+1]:
                        right -= 1
                
                elif total < 0:
                    left += 1
                else:
                    right -= 1

            return result