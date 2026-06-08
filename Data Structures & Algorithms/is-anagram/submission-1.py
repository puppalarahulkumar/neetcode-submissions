class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        compare_dict={}
        for i in s:
            compare_dict[i] = 0

        for i in s:
            compare_dict[i] += 1

        print(compare_dict) 

        for j in t:
            if j not in compare_dict:
                return False
            compare_dict[j]-= 1
        
        for index,value in compare_dict.items():
            if value != 0:
                return False
        return True
