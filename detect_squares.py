# Tags: math, hash-map
class CountSquares:

    def __init__(self):
        self.xMap = {}
        self.yMap = {}
        

    def add(self, point: list[int]) -> None:
        x, y = point[0], point[1]
        if x not in self.xMap:
            self.xMap[x] = []
        self.xMap[x].append(point)
        if y not in self.yMap:
            self.yMap[y] = []
        self.yMap[y].append(point)
        

    def count(self, point: list[int]) -> int:
        res = 0
        x, y = point[0], point[1]
        for p in self.xMap.get(x, []):
            y_ = p[1]
            if y - y_ == 0:
                continue
            for pp in self.yMap.get(y, []):
                x_ = pp[0]
                if abs(x- x_) != abs(y - y_):
                    continue
                for ppp in self.xMap.get(x_, []):
                    if ppp[1] == y_:
                        res += 1
        return res
    
if __name__ == "__main__":
    cs = CountSquares()
    cs.add([1, 1])
    cs.add([2, 2])
    cs.add([1, 2])
    print(cs.count([2, 1]))
    print(cs.count([3, 3]))
    cs.add([2, 2])
    print(cs.count([2, 1]))
