class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ele=set()
        for i in nums:
            if i in ele:
                return True
            ele.add(i)
        return False