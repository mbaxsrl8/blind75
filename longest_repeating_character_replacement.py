# Tags: sliding-window, hash-map, string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        cache = {}
        l = 0
        r = 0
        max_frequency = 0
        while r < len(s):
            cache[s[r]] = cache.get(s[r], 0) + 1
            max_frequency = max(max_frequency, cache[s[r]])
            while r - l + 1 - max_frequency > k and l < r:  # not a valid window
                # we don't have to update max frequent char because what we're looking for equals to finding the max num of the most frequency char
                cache[s[l]] = cache[s[l]] - 1
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res

    def find_most_frequent_char(self, cache: dict):
        max_count = 0
        char = None
        for k, v in cache.items():
            if v > max_count:
                max_count = v
                char = k
        print("most frequent char is %s", char)
        return char


if "__main__" == __name__:
    sol = Solution()
    print(sol.characterReplacement(s="AAAAABBBBCBB", k=3))
