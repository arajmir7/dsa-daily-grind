class Solution:
    def isValid(self, s):
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()

        return len(stack) == 0

if __name__ == "__main__":
    s = "([{}])"

    sol = Solution()
    result = sol.isValid(s)

    print("String:", s)
    print("Is valid:", result)