class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ele=dict()

        for i in strs:
            i_temp="".join(sorted(i))
            if i_temp in ele.keys():
                ele[i_temp].append(i)
            else:
                ele[i_temp]=[i]
        
        return(list(ele.values()))