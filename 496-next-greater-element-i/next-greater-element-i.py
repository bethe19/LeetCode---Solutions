class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = []
        n = len(nums2)
        for i in nums1:
            j = 0
            k = False
            while j < n:
                if nums2[j] == i:
                    k = True
                if k == True and nums2[j] > i:
                    nextGreater.append(nums2[j])
                    break
                j += 1
            if j == n:
                nextGreater.append(-1)
        return nextGreater