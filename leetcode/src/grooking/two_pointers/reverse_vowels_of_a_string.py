class Solution:
    def reverseVowels(self, s: str) -> str:
        firstPointer = 0
        lastPointer = len(s) - 1
        vowels = ['u', 'e', 'o', 'a', 'i']
        
        sArr = list(s)

        while firstPointer < lastPointer:
            if sArr[firstPointer].lower() in vowels and sArr[lastPointer].lower() in vowels:
                sArr[firstPointer], sArr[lastPointer] = sArr[lastPointer], sArr[firstPointer]
                firstPointer += 1
                lastPointer -= 1
            
            if sArr[firstPointer].lower() not in vowels:
                firstPointer += 1
            
            if sArr[lastPointer].lower() not in vowels:
                lastPointer -= 1

            

        return ''.join(sArr)

s = "Euston saw I was not Sue."
solution = Solution()
result = solution.reverseVowels(s)
print(result)