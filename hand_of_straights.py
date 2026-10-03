# Tags: heap, greedy, hash-map
import heapq

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand = sorted(hand)
        frequencyMap = {}
        minHeap = []
        for card in hand:
            if card not in frequencyMap:
                heapq.heappush(minHeap, card)
                frequencyMap[card] = 0
            frequencyMap[card] += 1
        
        while minHeap:
            start = minHeap[0]
            num = start
            for i in range(groupSize):
                if num not in frequencyMap or frequencyMap[num] == 0:
                    return False
                frequencyMap[num] -= 1
                num += 1
            while minHeap and frequencyMap[minHeap[0]] == 0:
                heapq.heappop(minHeap)
        
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isNStraightHand(hand = [1,2,4,2,3,5,3,4], groupSize = 4))
