class Counter:
    def __init__(self):
        self.count = 0

    def reset(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get(self):
        return self.count


a = Counter()
b = Counter()

a.increment()
print("카운터 a의 값은", a.get())
print("카운터 b의 값은", b.get())
