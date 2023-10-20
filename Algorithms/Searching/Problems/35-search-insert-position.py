# https://leetcode.com/problems/search-insert-position/description/

# Binary Search using iterative method to find the ceiling of a number in the ordered list
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            elif nums[middle] > target:
                high = middle - 1
        return low
