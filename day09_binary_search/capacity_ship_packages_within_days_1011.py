class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)
        answer = right

        while left <= right:
            mid = (left + right)//2
            required_days = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > mid:
                    required_days += 1
                    current_load = weight
                else:
                    current_load += weight
            if required_days <= days:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    sol = Solution()
    ans = sol.shipWithinDays(weights, days)
    print("Weights:", weights)
    print("Days:", days)
    print("Minimum Capacity:", ans)