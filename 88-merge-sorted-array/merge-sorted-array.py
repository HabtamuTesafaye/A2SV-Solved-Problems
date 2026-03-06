class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_ptr = m - 1
        nums2_ptr = n - 1

        # Pointer to the last position in the merged array (nums1)
        merge_position = m + n - 1

        # Merge from the end backwards
        while nums1_ptr >= 0 and nums2_ptr >= 0:
            if nums1[nums1_ptr] > nums2[nums2_ptr]:
                nums1[merge_position] = nums1[nums1_ptr]
                nums1_ptr -= 1
            else:
                nums1[merge_position] = nums2[nums2_ptr]
                nums2_ptr -= 1
            merge_position -= 1

        # Copy remaining elements from nums2 (if any)
        while nums2_ptr >= 0:
            nums1[merge_position] = nums2[nums2_ptr]
            merge_position -= 1
            nums2_ptr -= 1