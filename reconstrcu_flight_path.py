# Tags: depth-first-search, graph, needs-review
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        flightBySrc = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            if src not in flightBySrc:
                flightBySrc[src] = []
            flightBySrc[src].append(dst)
        
        result = ["JFK"]
        def dfs(src: str) -> bool:
            if len(result) == len(tickets) + 1:
                return True
            if src not in flightBySrc or len(flightBySrc[src]) == 0:
                return False
            
            temp = list(flightBySrc[src])
            for i, nextStop in enumerate(temp):
                result.append(nextStop)
                flightBySrc[src].pop(i)
                
                if dfs(nextStop): return True
                
                result.pop()
                flightBySrc[src].insert(i, nextStop)
                
            return False
                
            
        dfs("JFK")
        return result
    # def findItinerary(self, tickets: list[list[str]]) -> list[str]:
    #     flights = {src: [] for src, dst in tickets}
    #     for src, dst in tickets:
    #         flights.setdefault(src, []).append(dst)
            
    #     for values in flights.values():
    #         values.sort(reverse=True)
        
    #     stack: list[str] = ["JFK"]
    #     route: list[str] = []
        
    #     while stack:
    #         src = stack[-1]
    #         if flights.get(src):
    #             stack.append(flights[src].pop())
    #         else:
    #             route.append(stack.pop())
        
    #     return route[::-1]
    
if __name__ == "__main__":
    sol = Solution()
    # print(sol.findItinerary(tickets=[["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))
    print(sol.findItinerary(tickets=[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
