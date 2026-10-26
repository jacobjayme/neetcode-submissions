class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            before = len(seen)
            seen.add(i)
            after = len(seen)
            if before == after:
                return True
        return False

        