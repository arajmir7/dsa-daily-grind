class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        res = [0] * n
        stack = [] 
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        
        return res
        
if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]

    sol = Solution()
    result = sol.dailyTemperatures(temperatures)

    print("Temperatures:", temperatures)
    print("Days to wait:", result)