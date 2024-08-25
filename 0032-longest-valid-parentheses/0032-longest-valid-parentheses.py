class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxcnt = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxcnt = max(maxcnt, i - stack[-1])
        
        return maxcnt 