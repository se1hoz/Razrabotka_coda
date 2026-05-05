class Timer:
    __slots__ = ('start', 'end')
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def difference(self):
        return self.end - self.start

t = Timer(10, 35)
print(f"Разница: {t.difference()}")