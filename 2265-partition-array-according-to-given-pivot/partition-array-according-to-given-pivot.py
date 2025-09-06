class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessers = []
        greaters = []
        count = 0
        for i in range(len(nums)):
            if nums[i] > pivot:
                greaters.append(nums[i])
            elif nums[i] < pivot:
                lessers.append(nums[i])
            else:
                count += 1
                

        return lessers + ([pivot]*count) + greaters