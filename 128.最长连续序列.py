#
# @lc app=leetcode.cn id=128 lang=python
#
# [128] 最长连续序列
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_len = 1
                cur_num = num

                while cur_num + 1 in nums_set:
                    cur_len += 1
                    cur_num += 1
                
                max_len = max(cur_len, max_len)
        return max_len


        # if not nums: return 0
        # max_len = 0
        # hashtable = dict()
        # for i in range(len(nums)):
        #     if nums[i] not in hashtable:
        #         left = hashtable.get(nums[i]-1, 0)
        #         right = hashtable.get(nums[i]+1, 0)
        #         cur_len = 1 + left + right
        #         if cur_len > max_len:
        #             max_len = cur_len

        #         hashtable[nums[i]] = cur_len
        #         hashtable[nums[i]-left] = cur_len
        #         hashtable[nums[i]+right] = cur_len
        # return max_len
        
# @lc code=end

