class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        i = 0
        while candies>0:
            if candies >= i+1:
                res[i%num_people] += i+1
                candies -= i+1
            else:
                res[i%num_people] += candies
                break
            i += 1
        return res
        