class Solution:
    def threeSum(self, A):
        A.sort()
        result = []

        for i in range(len(A)):
            if i > 0 and A[i] == A[i-1]:
                continue


            
if __name__ == "__main__":
    s = "ibobi"
    sol = Solution()
    ans = sol.isPalindrome(s)
    print("Word: ", s)
    print("Is it palindrome: ", ans)