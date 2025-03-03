class Solution:
    """
    Merges two sorted arrays in 0(n) by iterating through both lists of the form
    nums1=[(id,val), ...] and nums2=[(id,val)] and picking lowest id of the two and 
    appending it to output list.

    If both ids are the same, append to output list the sum of the values associated to both ids
    """
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        out = []

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] < nums2[j][0]:
                out.append(nums1[i])
                i += 1
            elif nums1[i][0] == nums2[j][0]:
                out.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            else:
                out.append(nums2[j])
                j += 1

        while i < len(nums1):
            out.append(nums1[i])
            i += 1

        while j < len(nums2):
            out.append(nums2[j])
            j += 1

        return out