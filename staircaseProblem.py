class Solution:
    def climbStairs(self, n, first=0, second=1):
        third = first + second
        if n == 1:
            return third
        return self.climbStairs(n-1, first=second, second=third)


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5))
