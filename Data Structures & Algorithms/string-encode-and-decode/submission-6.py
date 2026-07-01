class Solution:

    def encode(self, strs: List[str]) -> str:
        
        word=""

        for i in strs:
            word_len=len(i)
            word +=f"{word_len}#" + i
        

        print(word)
        return word
            

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            # Find the position of '#'
            j = i
            while s[j] != '#':
                j += 1

            # Extract the length
            length = int(s[i:j])

            # Extract the word
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # Move i to the start of the next encoded word
            i = j + 1 + length

        return result