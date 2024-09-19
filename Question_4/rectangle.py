class Rectangle:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width
    
    def generator(self):
        yield {"length":self.length}
        yield {"width":self.width}
        
rect = Rectangle(10,5)
for dimensions in rect.generator():
    print(dimensions)