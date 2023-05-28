// https://leetcode.com/problems/design-hashset

class MyHashSet:

    def __init__(self):
        self.d = {}
        

    def add(self, key: int) -> None:
        self.d[key] = 1
        

    def remove(self, key: int) -> None:
        if key in self.d:
            del self.d[key]
        

    def contains(self, key: int) -> bool:
        return key in self.d
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)