class Solution:    def findPoisonedDuration(self, timeSeries, duration):        """        :type timeSeries: List[int]        :type duration: int        :rtype: int        """        if len(timeSeries)==0:            return 0        all_dura=0        timelevel=timeSeries[0]        for time in timeSeries:            if time>=timelevel:                all_dura+=duration                timelevel=time+duration            elif time+duration>timelevel:                all_dura+=(time+duration-timelevel)                timelevel=time+duration        return all_duras=Solution()timeSeries=[1,1]duration=2print(s.findPoisonedDuration(timeSeries,duration))