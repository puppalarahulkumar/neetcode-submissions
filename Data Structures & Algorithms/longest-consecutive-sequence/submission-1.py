class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if len(nums) == 0:
            return 0
        count=0
        longest_count=0
        for i in range(0,len(nums)):
            temp_var= nums[i] + 1
            
            if i+1 == len(nums):
                continue

            elif nums[i+1] == temp_var:
                count +=1
            elif nums[i+1] == nums[i]:
                count = count
            elif nums[i+1] != temp_var:
                if longest_count <= count:
                    longest_count=count
                count=0
            
        if longest_count >= count:
                
            count = longest_count
        return count + 1