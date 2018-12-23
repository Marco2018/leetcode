class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        rl = list()
        while target:
            rl.append(target%x)
            target=int(target/x)
        n = len(rl)
        pos = rl[0] * 2
        neg = (x-rl[0]) * 2
        for i in range(1,n):
            pos, neg = min(rl[i] * i + pos, rl[i] * i + i + neg), min((x - rl[i]) * i + pos, (x-rl[i]) * i + i + neg - 2 * i)
        return min(pos-1, n+neg-1)
s1=Solution()
print(s1.leastOpsExpressTarget(3,19))
