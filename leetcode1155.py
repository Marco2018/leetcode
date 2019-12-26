class Solution:
    def numRollsToTarget(self, d, f, target):
        memo = {}
        def dp(d, target):
            if d==0:
                if target != 0:
                    return 0
                else:
                    return 1
            if (d, target) in memo:
                return memo[(d, target)]
            res = 0
            for i in range(1, min(f, target)+1):
                res += dp(d-1, target - i)
            memo[(d, target)] = res
            return res
        return dp(d, target) % (10**9 + 7)