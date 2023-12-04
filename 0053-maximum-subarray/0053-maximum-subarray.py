class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # 1
        currentSum = 0

        # 2 
        maxSum = nums[0]

        # 3
        for num in nums:

            # 3a
            if currentSum < 0:
                currentSum = 0
            
            # 3b
            currentSum += num

            # 3c
            maxSum = max(maxSum, currentSum)
        
        # 4
        return maxSum