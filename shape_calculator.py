class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2) + (self.height **2)) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ("*" * self.width + "\n") * self.height
        
    def get_amount_inside(self, shape):
        big_width = self.width
        big_height = self.height
        
        while not (big_width % shape.width == 0):
            big_width -= 1
        
        while not (big_height % shape.height == 0):
            big_height -= 1
        
        big_area = big_height * big_width
        
        return (big_area // shape.get_area())
    
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side) -> None:
        self.side = side
        super().__init__(side, side)
        
    def set_side(self, side):
        self.side = side
    
    def set_width(self, width):
        self.side = width
    
    def set_height(self, height):
        self.side = height
        
    def get_picture(self):
        if self.side > 50:
            return "Too big for picture."
        else:
            return ("*" * self.side + "\n") * self.side
    
    def __str__(self) -> str:
        return f"Square(side={self.side})"
