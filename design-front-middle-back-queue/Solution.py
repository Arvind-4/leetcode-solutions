// https://leetcode.com/problems/design-front-middle-back-queue

class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []
        

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)
        

    def pushMiddle(self, val: int) -> None:
        n = len(self.queue)
        if n % 2 == 0: n = int(n / 2)
        else: n = n // 2
        self.queue.insert(n, val)
        

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        

    def popFront(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)
        

    def popMiddle(self) -> int:
        n = len(self.queue)
        if n == 0: return -1
        if n % 2 == 0: n = int(n / 2) - 1
        else: n = n // 2
        return self.queue.pop(n)
        

    def popBack(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue.pop()
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()