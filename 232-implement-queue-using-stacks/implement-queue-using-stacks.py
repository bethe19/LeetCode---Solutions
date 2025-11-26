class MyQueue:
    def __init__(self):
        self.z = []
        self.y = []

    def push(self, x: int) -> None:
        while self.z:
            self.y.append(self.z.pop())
        self.z.append(x)
        while self.y:
            self.z.append(self.y.pop())

    def pop(self) -> int:
        if not self.z:
            return -1
        return self.z.pop()

    def peek(self) -> int:
        if not self.z:
            return -1
        return self.z[-1]

    def empty(self) -> bool:
        return len(self.z) == 0
