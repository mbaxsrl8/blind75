# Tags: string, design
from typing import List


class Solution:
    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            word_len = len(string)
            res += str(word_len) + self.delimiter + string
            
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            len_str = ''
            while j < len(s) and s[j] != self.delimiter:
                len_str += s[j]
                j += 1
            word_len = int(len_str)
            i = j  +1
            res.append(s[i : i + word_len])
            i += word_len
        return res
            


if '__main__' == __name__:
    sol = Solution()
    print(sol.decode(sol.encode(["we","say",":","yes","!@#$%^&*()"])))