class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessers = []
        greaters = []
        p = []
        for i in nums:
            if i > pivot:
                greaters.append(i)
            elif i < pivot:
                lessers.append(i)
            else:
                p.append(i)
                

        return lessers + p+ greaters