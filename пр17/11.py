import os

print("Файлы в текущей папке:")
for item in os.listdir('.'):
    print(f"  {item}")