// https://leetcode.com/problems/fizz-buzz-multithreaded

class FizzBuzz:
    def __init__(self, n: int):
        self.done = False        
        self.n = n
        self.fSem = threading.Semaphore(0)
        self.bSem = threading.Semaphore(0)
        self.fbSem = threading.Semaphore(0)
        self.nSem = threading.Semaphore(1)

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fSem.acquire()
            if self.done: break
            printFizz()
            self.nSem.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.bSem.acquire()
            if self.done: break
            printBuzz()
            self.nSem.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fbSem.acquire()
            if self.done: break
            printFizzBuzz()
            self.nSem.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.nSem.acquire()
            if i % 15 == 0:
                self.fbSem.release()
            elif i % 3 == 0:
                self.fSem.release()
            elif i % 5 == 0:
                self.bSem.release()
            else:
                printNumber(i)
                self.nSem.release()
        self.nSem.acquire() 
        self.done = True
        self.fSem.release()  
        self.bSem.release()  
        self.fbSem.release()