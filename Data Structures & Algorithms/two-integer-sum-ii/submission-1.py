class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution=[]
        for i in range(0,len(numbers)):
            if len(numbers) != i:
                for j in range(i+1,len(numbers)):
                    if numbers[i] + numbers[j] == target and numbers[j] > numbers[i] and numbers[i] != numbers[j]:
                        solution.append(i+1)
                        solution.append(j+1)
        return solution