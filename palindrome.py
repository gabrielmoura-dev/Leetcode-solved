class Solution:
    def isPalindrome(self, x: int) -> bool:
        convert = str(x)
        value = convert[::-1]
        if value == convert:
            return True
        else:
            return False