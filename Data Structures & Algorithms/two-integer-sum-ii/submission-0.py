class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num=numbers
        left=0
        right=len(numbers)-1

        while left<right:
            if num[left]+num[right]>target:
                right-=1
            if num[left]+num[right]==target:
                return [left+1,right+1]
            if num[left]+num[right]<target:
                left+=1