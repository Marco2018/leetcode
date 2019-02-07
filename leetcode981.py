from collections import defaultdict,deque
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = defaultdict(deque)
    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self.values[key].appendleft((value, timestamp))


    def get(self, key: 'str', timestamp: 'int') -> 'str':
        vs = self.values[key]
        for i in range(len(vs)):
            if vs[i][1] <= timestamp:
                return vs[i][0]
        return ""