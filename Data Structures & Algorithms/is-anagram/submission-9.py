class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict={}

        for i in s:
            if i not in anagram_dict:
                anagram_dict[i]=1
            else:
                anagram_dict[i] +=1
            
        print(anagram_dict)

        for i in t:
            if i in anagram_dict:
                anagram_dict[i] -=1
            else:
                return False
        
        print(anagram_dict)

        for key,value in anagram_dict.items():
            if value == 0:
                pass
            else:
                return False
        
        return True