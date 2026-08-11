class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        longest=0

        for n in num:
            if n-1 not in num:  #If left side empty then its a starting sequence
                length=1
                while (n+length) in num:
                    length+=1
                longest=max(length,longest)
        return longest
            