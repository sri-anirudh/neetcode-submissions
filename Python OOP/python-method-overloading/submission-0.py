class TextProcessor:
    # Implement method overloading for format_text method
    def __init__(self):
        pass
    def format_text(self, txt1: str, txt2: str = "")-> str:
        if txt2 == "":
            return txt1.upper()
        else:
            return txt1+txt2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
