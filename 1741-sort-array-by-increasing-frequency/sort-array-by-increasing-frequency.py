class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = []
        for i in nums:
            count = 0 
            for j in nums:
                if i == j:
                    count += 1
            frequency.append((i,count))
        result = [i for i,j in sorted(frequency, key=lambda t: (t[1], -t[0]))]

        return result