class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for num in arr2:
            i = 0
            while i < len(arr1):
                if arr1[i] == num:
                    result.append(arr1.pop(i))
                    continue
                i+=1
        return result + sorted(arr1)