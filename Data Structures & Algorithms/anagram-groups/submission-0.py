class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comp_dict=defaultdict(list)

        for s in strs:
            word="".join(sorted(s))
            comp_dict[word].append(s)
        
        final_list=[]

        for li in comp_dict.values():
            final_list.append(li)
        return final_list