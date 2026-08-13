class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,p,m=0,1,prices,0
        while r<len(p):
            if p[l]<p[r]:
                m=max(m,p[r]-p[l])
            else:
                l=r #As we want maximum profit and we have found minimum
            r+=1
        return m
