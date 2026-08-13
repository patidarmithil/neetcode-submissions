class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        l,r=0,len(heights)-1
        h=heights

        while l<r:
            m=min(h[l],h[r])
            val=(r-l)*m
            if val>max:
                max=val
            if h[l]<h[r]:
                    l+=1
            else:
                r-=1
        return max
