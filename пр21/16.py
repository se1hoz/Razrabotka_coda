class Temperature:
    __slots__ = ('value',)
    
    def __init__(self, celsius):
        self.value = celsius
    
    def to_fahrenheit(self):
        return self.value * 9/5 + 32

t = Temperature(25)
print(f"{t.value}°C = {t.to_fahrenheit()}°F")