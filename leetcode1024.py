class Solution:
    def videoStitching(self, clips, T):
        if T == 0:return 0
        clips.sort(key=lambda x:(x[0],x[0]-x[1]))
        print(clips)
        dp = [float("inf") for i in range(T+1)]
        dp[0] = 0
        if clips[0][0] != 0: return -1
        for start, end in clips:
            if start>=T:
                continue
            if end>=T:
                end=T
            for i in range(start+1, end+1):
                dp[i] = min(dp[i], 1 + dp[start])
        if dp[-1] == float("inf"): return -1
        return dp[-1]