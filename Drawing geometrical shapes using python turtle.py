import turtle
class Geometrical_Shapes:
    def __init__(self, shape_name,_length,_breadth):
        self.shapeName  = shape_name
        self.length = _length
        self.breadth = _breadth
        self.perimeter = 0
        self.area = 0   

    def findArea(self):
        self.area = 0
    def findPerimeter(self):
        self.perimeter = 0
    def draw_shape(self):
        window = turtle.Screen()
        window.bgcolor("white")        
        #background color
class Isoceles_Triangle(Geometrical_Shapes):
    def __init__(self,shape_name,_length,_breadth):
        Geometrical_Shapes.__init__(self,shape_name,_length,_breadth)
        print(self.shapeName," is initialized with two sides are equal")
    def findArea(self):
        self.area = 0.5 * self.length * self.breadth
        print('The area of the isoceles triangle in meters: %0.2f' %self.area)
    def findPerimeter(self):
        self.perimeter = 2 * self.length + self.breadth
        print('The perimeter of the isoceles triangle in meters: %0.2f' %self.perimeter)
    def draw_shape(self):
        tom = turtle.Turtle()
        tom.goto(50,50)
        tom.forward(100)
        tom.left(120)
        tom.forward(100)
        tom.left(120)
        tom.forward(100)
        #window.exitonclick() #to exit
class Rectangle(Geometrical_Shapes):
    def __init__(self,shape_name,_length,_breadth):
        Geometrical_Shapes.__init__(self,shape_name,_length,_breadth)
        print(self.shapeName," is initialized with opposite sides are equal")
    def findArea(self):
        self.area = self.length * self.breadth
        print('The area of the rectangle in meters: %0.2f' %self.area)
    def findPerimeter(self):
        self.perimeter = 2 * (self.length + self.breadth)
        print('The perimeter of the rectangle in meters: %0.2f' %self.perimeter)
    def draw_shape(self):
        t = turtle.Turtle()
        t.goto(150,150)
        t.forward(200)
        t.left(90) #Turn turtle by 90 degree
        t.forward(80) #Forward turtle by 80 units
        t.left(90) #Turn turtle by 90 degree
        t.forward(150) #Forward turtle by 150 units
        t.left(90) #Turn turtle by 90 degree
        t.forward(80) #Forward turtle by 80 units
        t.left(90) #Turn turtle by 90 degree
class Square(Geometrical_Shapes):
    def __init__(self,shape_name,_length,_breadth):
        Geometrical_Shapes.__init__(self,shape_name,_length,_breadth)
        print(self.shapeName," is initialized with all sides equal")
    def findArea(self):
        self.area = self.length * self.length
        print('The area of the square in meters: %0.2f' %self.area)
    def findPerimeter(self):
        self.perimeter = 4 * self.length
        print('The perimeter of the square in meters: %0.2f' %self.perimeter)
    def draw_shape(self):
        t = turtle.Turtle()
        t.goto(100,100)
        t.forward(100) #Forward turtle by 100 units
        t.left(90) #Turn turtle by 90 degree
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90) 

print("Investigatory Project On finding of area, perimeter and drawing of Isoceles Triangel/Square/Rectangle shapes using Inheritance ")
print("------------------------------------------------------------------------------------------------------------------------------------------")
print("1.Isoceles Triangle")
print("2.Square")
print("3.Rectangle")
print("4.Exit")

# Take input from the user
ch = "Y"
while (ch.upper() == 'Y'):
    choice = input("Enter choice(1/2/3/4):")
    if (choice == '1'):
        #Triangle object
        length = int(input("Enter the base of triangle in meters:"))
        breadth = int(input("Enter the height of triangle in meters:"))
        IsocelesTriangle = Isoceles_Triangle("Isoceles Triangle",length,breadth)
        IsocelesTriangle.findArea()
        IsocelesTriangle.findPerimeter()
        IsocelesTriangle.draw_shape()
    if (choice == '2'):
        #Square object
        length = int(input("Enter the side of square in meters:"))
        Square = Square("Square",length,0)  #As all sides same, breadth can be 0 itself
        Square.findArea()
        Square.findPerimeter()
        Square.draw_shape()
    if (choice == '3'):
        #Rectangle object
        length = int(input("Enter the length of rectangle in meters:"))
        breadth = int(input("Enter the breadth of rectangle in meters:"))
        Rectangle = Rectangle("Rectangle",length,breadth)
        Rectangle.findArea()
        Rectangle.findPerimeter()
        Rectangle.draw_shape()
    ch = input("Do you want to continue (Y/N): ")
