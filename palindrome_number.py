class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = str(x)
        reversed_str = original[::-1]
        return original == reversed_str


soln1 = Solution()
print(soln1.isPalindrome(121))      