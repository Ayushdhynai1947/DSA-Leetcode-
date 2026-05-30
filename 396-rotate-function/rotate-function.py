class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Edge case
        if n == 1:
            return 0

        total_sum = sum(nums)

        F = sum(i*n for i , n in enumerate(nums))
        max_val = F

        for k in range(1 , n):
            F = F + total_sum - n * nums[n - k]
            max_val = max(max_val, F)

        return max_val

        