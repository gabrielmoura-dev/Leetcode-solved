class Solution:
    roman_symbol = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                result += self.roman_symbol[s[i]]
                return result
            if self.roman_symbol[s[i]] < self.roman_symbol[s[i+1]]:
                result -= self.roman_symbol[s[i]]
            else:
                result += self.roman_symbol[s[i]]