class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        i=0
        while i <2:
            for v in nums:
                ans.append(v)
            i=i+1
        return ans
        