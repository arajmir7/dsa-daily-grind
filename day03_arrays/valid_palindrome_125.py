class Solution:
    def palindrome(self, i, s):
        if i >= len(s)//2:
            return True
        if s[i] != s[len(s)-i-1]:
            return False
        return self.palindrome(i+1,s)

if __name__ == "__main__":
    s = "madam"
    sol = Solution()
    result = sol.palindrome(0, s)
    print("String:", s)
    print("Is Palindrome:", result)