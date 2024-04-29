from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            print("Not enough strings to compare")
            return
        first_word = strs[0]
        all_loop = True
        char_index = 0
        while all_loop:
            for word_index in range(1, len(strs) - 1):
                if char_index > len(strs[word_index])-1 or char_index > len(first_word[word_index])-1:
                    all_loop= False
                    break
                if strs[word_index][char_index] == first_word[char_index]:
                    continue
                else:
                    if char_index == 0:
                        return ""
                    all_loop = False
                    break
            char_index += 1
        return strs[0][0:char_index]



solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","flight"])
print(result)