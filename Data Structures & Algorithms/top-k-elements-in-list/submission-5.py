from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        sorted_dict=sorted(count,key=count.get,reverse=True)
        return sorted_dict[:k]