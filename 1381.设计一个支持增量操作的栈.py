#
# @lc app=leetcode.cn id=1381 lang=python3
#
# [1381] 设计一个支持增量操作的栈
#

# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.len = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.len < self.maxSize:
            self.stack.append(x)
            self.len += 1


    def pop(self) -> int:
        if self.len is 0:
            return -1
        self.len -= 1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.len)):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end

