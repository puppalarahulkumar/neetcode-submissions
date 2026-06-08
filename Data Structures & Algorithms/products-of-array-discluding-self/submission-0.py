class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(0,len(nums)):
            mul_value=1
            temp_iteration=i
            
            for j in range(0,len(nums)):
                
                if i==j:
                    mul_value=mul_value*1
                else:
                    mul_value=mul_value*nums[j]
            output.append(mul_value)
        return output
