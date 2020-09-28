class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip()
        words = words.split(' ')
        return len(words[-1])