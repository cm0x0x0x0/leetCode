class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U']
        forwardVowels = []
        for c in s:
            if c in vowels:
                forwardVowels.append(c)
                
        vowelIdx = 0
        size = len(forwardVowels)
        listS = list(s)
        for idx in range(len(listS)):
            if listS[idx] in vowels:
                listS[idx] = forwardVowels[size-vowelIdx-1]
                vowelIdx += 1

        return ''.join(listS)