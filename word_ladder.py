# Tags: graph, string, breadth-first-search
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        allWords = set(wordList)
        if endWord not in allWords:
            return 0
        allWords.add(beginWord)
        
        buckets = {}
        for word in allWords:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                if pattern not in buckets:
                    buckets[pattern] = []
                buckets[pattern].append(word)
        
        edgeMap = {word: set() for word in allWords}
        for words in buckets.values():
            if len(words) < 2:
                continue
            for word in words:
                edgeMap[word] |= set(words)
        
        hop = 1
        level = [beginWord]
        next_level = []
        visited = set()
        while level:
            hop += 1
            for word in level:
                visited.add(word)
                for neighbor in edgeMap[word]:
                    if neighbor == endWord:
                        return hop
                    if neighbor in visited or neighbor == word:
                        continue
                    next_level.append(neighbor)
            level = next_level
            next_level = []

        return 0
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength(beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]))
