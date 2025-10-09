class rectangle:                        # creating class for rectangle
    def __init__(self, length , breadth):               # creating a method main
        self.length = length
        self.breadth = breadth
    def area(self):                                     # method for area
        return self.length * self.breadth               # return area
    def perimeter(self):                                # method for perimeter
        return (2 * (self.length + self.breadth))       # return perimeter


my_rect = rectangle(5,6)
print("Area : ", my_rect.area())
print("Perimeter : ", my_rect.perimeter)
