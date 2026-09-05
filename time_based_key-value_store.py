# Tags: design, binary-search, review-priority
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.map.setdefault(key, [])
        l, r = 0, len(values)
        while l < r:
            m = (l + r) // 2
            if values[m][0] > timestamp:
                r = m
            else:
                l = m + 1
        values.insert(l, (timestamp, value))
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        values = self.map[key]
        if timestamp < values[0][0]:
            return ""
        l, r = 0, len(values) - 1
        result = ""
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                result = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return result
    
if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.set("test", "one", 10)
    timeMap.set("test", "two", 20)
    timeMap.set("test", "three", 30)
    print(timeMap.get("test", 15))
    print(timeMap.get("test", 25))
    print(timeMap.get("test", 35))
