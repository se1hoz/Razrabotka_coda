class SafeFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write("Test content")
        except:
            pass
        
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
            return self.file
        except Exception as e:
            print(f"Error opening file: {e}")
            return None
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print("File closed")

with SafeFile('input.txt', 'r') as f:
    if f:
        content = f.read()
        print(content)