class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        exist = [0] * 101

        for i in nums:
            exist[i] += 1
        for i in range(1,len(exist)):
            exist[i] += exist[i-1]
        
        answer = []
        for i in nums:
            if i == 0:
                answer.append(0)
            else:
                answer.append(exist[i-1])
        return answer