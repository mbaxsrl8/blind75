# Tags: heap, design, hash-map
import heapq
from itertools import count
from collections import deque


class Twitter:

    def __init__(self):
        self.counter = count()
        self.followMap = {}
        self.tweetMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = deque(maxlen=10)
        queue = self.tweetMap[userId]
        queue.append((-next(self.counter), tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        following = self.followMap.get(userId, set()) | {userId}
        heap = []
        for user in following:
            for tweet in self.tweetMap.get(user, []):
                heap.append(tweet)
        heapq.heapify(heap)
        result = []
        while heap and len(result) < 10:
            result.append(heapq.heappop(heap)[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
    
if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 10)
    twitter.postTweet(2, 20)
    print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(2))
    twitter.follow(1, 2)
    print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(2))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))
    
