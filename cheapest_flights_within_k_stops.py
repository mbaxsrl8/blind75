# Tags: dynamic-programming, graph, breadth-first-search, needs-review
class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        flightsDict = {}
        for s, d, price in flights:
            if s not in flightsDict:
                flightsDict[s] = []
            flightsDict[s].append((d, price))

        hop = 0
        level = [(src, 0)]
        next_level = []
        minPriceByStop = {}
        while hop <= k + 1 and level:
            hop += 1
            for stop, expense in level:
                if stop not in minPriceByStop:
                    minPriceByStop[stop] = expense
                elif expense < minPriceByStop[stop]:
                    minPriceByStop[stop] = expense
                else:
                    continue
                    
                if stop in flightsDict:
                    for nextStop, price in flightsDict[stop]:
                        next_level.append((nextStop, expense + price))

            level = next_level
            next_level = []

        return minPriceByStop.get(dst, -1)


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.findCheapestPrice(
            n=3,
            flights=[[0,1,100],[1,2,100],[0,2,500]],
            src=0,
            dst=2,
            k=1,
        )
    )
