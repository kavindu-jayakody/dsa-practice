# Key idea: append nums twice. Time O(n), Space O(n)
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            ans.append(x)
        for x in nums:
            ans.append(x)
        return ans
