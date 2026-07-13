class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num=0
        temp_num=0
        for i in nums:
            if i == 1:
                temp_num+=1
                max_num=max(temp_num,max_num)
            else:
                temp_num =0
        return max_num
            
