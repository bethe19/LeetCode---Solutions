class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_items = count.most_common()

        result = ""
        for i,j in sorted_items:
            result += i * j
        return result