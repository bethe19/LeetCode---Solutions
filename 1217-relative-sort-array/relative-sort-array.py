class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map = {}
        for i in arr1:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        result = []
        for i in arr2:
            if i in map:
                result.extend([i]*map[i])
                del map[i]
        remaining = sorted(map.keys())
        for i in remaining:
            result.extend([i] * map[i])
        return result