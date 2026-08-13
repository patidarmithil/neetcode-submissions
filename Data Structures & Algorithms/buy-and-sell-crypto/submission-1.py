class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,p,m=0,1,prices,0
        while r<len(p):
            if p[l]<p[r]:
                m=max(m,p[r]-p[l])
            else:
                l=r
            r+=1
        return m
