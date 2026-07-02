class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(0,len(nums)):
            temp_num=1
            for j in range(0,len(nums)):
                if i != j:
                    temp_num *= nums[j]
            output.append(temp_num)

        return output
                    
                     