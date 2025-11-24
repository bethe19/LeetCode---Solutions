class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        newArr = [nums[0]]
        for i in range(1,len(nums)):
            if newArr[-1] != nums[i]:
                newArr.append(nums[i])
    
        count = 0
        for i in range(1,len(newArr)-1):
            if newArr[i-1] > newArr[i] and newArr[i+1] > newArr[i]:
                count += 1
            if newArr[i-1] < newArr[i] and newArr[i+1] < newArr[i]:
                count += 1
        return count

