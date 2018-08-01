class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        isvisited=[[0 for i in range(len(image[0]))]for j in range(len(image))]
        oldcolor=image[sr][sc]
        def flood(image,sr,sc,newColor,isvisited,oldcolor):
            if -1<sr<len(image) and -1<sc<len(image[0]):
                if image[sr][sc]==oldcolor and isvisited[sr][sc]==0:
                    image[sr][sc]=newColor
                    isvisited[sr][sc]=1
                    flood(image,sr-1,sc,newColor,isvisited,oldcolor)
                    flood(image, sr+1, sc, newColor, isvisited,oldcolor)
                    flood(image, sr, sc-1, newColor, isvisited,oldcolor)
                    flood(image, sr, sc+1, newColor, isvisited,oldcolor)
        flood(image,sr,sc,newColor,isvisited,oldcolor)
        return image
solution=Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(solution.floodFill(image,sr,sc,newColor))




