class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area=0

        if len(heights) == 1:
            return heights[0]

        for i in range(0,len(heights)):
            
            lenght=heights[i]
            for j in range(i,len(heights)):
                lenght=min(lenght,heights[j])
                width= j-i+1
                area=max(area,lenght*width)
                
        return area