#
# @lc app=leetcode.cn id=768 lang=python3
#
# [768] 最多能完成排序的块 II
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        for i in range(0,len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] < arr[i]:
                    
                    continue

        
# @lc code=end

