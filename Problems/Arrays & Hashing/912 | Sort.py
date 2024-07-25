# LC 912. Sort an Array | Daily LC - 7/25/24
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(unsortedNums):
            if len(unsortedNums) > 1:
                mid = len(unsortedNums) // 2
                left = unsortedNums[:mid]
                right = unsortedNums[mid:]

                mergeSort(left)
                mergeSort(right)

                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        unsortedNums[k] = left[i]
                        i += 1
                    else:
                        unsortedNums[k] = right[j]
                        j += 1
                    k += 1
                
                while i < len(left):
                    unsortedNums[k] = left[i]
                    i += 1
                    k += 1
                
                while j < len(right):
                    unsortedNums[k] = right[j]
                    j += 1
                    k += 1

        mergeSort(nums)
        return nums

  '''
  TLDR: Use merge sort here. Given that the input arr can be of len <= 5 * 10^6, merge sort is more stable and would handle the better than quick sort.
  '''
