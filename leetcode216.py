class Solution:    def combinationSum3(self, k, n):        def helper(candi,target,path,k):            if target<0:                return            elif target==0:                if path not in self.ans and len(path)==k:                    self.ans.append(path)            else:                for i in range(len(candi)):                    helper(candi[i+1:],target-candi[i],path+[candi[i]],k)        self.ans=[]        candidates=[1,2,3,4,5,6,7,8,9]        helper(candidates,n,[],k)        return self.anss=Solution()print(s.combinationSum([2,3,6,7],7))