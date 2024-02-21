class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def setDimensions(self, w, h):
        self.width = w
        self.height = h
    
    def getArea(self):
        area = (self.width * self.height)
        return area
    
rectangle = Rectangle()
rectangle.setDimensions(10, 5)
print(rectangle.getArea())