class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        n=2*n
        ans=[]

        for i in range(0,len(nums)):
            ans.append(nums[i])
        for i in range(0,len(nums)):
            ans.append(nums[i])
        return ans

