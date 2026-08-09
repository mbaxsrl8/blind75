# Tags: dfs, graph, string

# There is a new alien language that uses the English alphabet, but the order of the letters is unknown.

# You are given a list of strings words from the alien language's dictionary. It is claimed that the strings in words are sorted lexicographically by the rules of this new language.

# If this claim is incorrect, and the given arrangement of strings in words cannot correspond to any order of letters, return "".

# Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

# A string a is lexicographically smaller than a string b if either of the following is true:

# The first letter where they differ is smaller in a than in b.
# a is a prefix of b and a.length < b.length.

class Solution:

    def foreignDictionary(self, words: list[str]) -> str:
        res = []
        p2c = {}
        # children = {}
        all_dict = set()
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            j = 0
            while j < len(word1) and j < len(word2) and word1[j] == word2[j]:
                j += 1

            if j < len(word1) and j < len(word2):
                char1 = word1[j]
                char2 = word2[j]
                if char1 not in p2c:
                    p2c[char1] = set()
                p2c[char1].add(char2)
            elif len(word1) > len(word2):
                return ""
            for c in word1:
                all_dict.add(c)
        for c in words[-1]:
            all_dict.add(c)
        
        res = ""
        def dfs(k: str, visited: set) -> bool: # return if this graph is valid
            nonlocal p2c
            nonlocal all_dict
            nonlocal res
            if k in visited and k in all_dict:
                return False
            if k not in p2c:
                res = k  +res
                all_dict.remove(k)
                return True
            visited.add(k)
            for c in p2c[k]:
                if c not in all_dict:
                    continue
                if not dfs(c, visited):
                    return False
            res = k + res
            all_dict.remove(k)
            return True
        while len(all_dict) > 0:
            if not dfs(next(iter(all_dict)), set()):
                return ""
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.foreignDictionary(words=["hrn","hrf","er","enn","rfnn"]))
