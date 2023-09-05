
# shapes calculations
 
while True:
    try:
        import math
        #  Parent class 'Shape' creation(with attribute self.pi, methods 'circlearea' and 'rectangleperimeter')
        class Shape:

            def __init__(self):
                self.pi = math.pi
    
            def circlearea(self):
                radius = float(input('input radius: '))
                Area = self.pi * (radius.__pow__(2))
                return F'Area is: {Area:0f}'
    
            def rectangleperimeter(self, length, width):
                perimeter = 2 * (length + width)
                return f'{perimeter:2f}'

        # Subclass 'Diameter' and 'Rec_square' inheriting from parent class(Shape) creation
        class Diameter(Shape):

            def diameter(self, area):
                Diameter = area / self.pi
                return  f'Diameter is: {Diameter}'

        class Rec_square(Shape):

            def comparison(self):
                length = float(input('Input length: '))
                width = float(input('Input width: '))
                if length != width:
                    
                    return 'not a square'
                else:
                    return 'equal dimensions,is a square'
        
        # instance of the parent class invoked
        instance = Shape() # instance of shape class
        print(instance.circlearea()) # instance of shape method
        print(instance.rectangleperimeter(4,5))

        # instance of the subclass Diameter invoked
        instance2 = Diameter()
        print(instance2.diameter(34))

        #instance of the subclass Rec_square invoked
        instance3 = Rec_square()
        print(instance3.comparison())

    except:
        pass

    user = input('revisit the calculation, (yes/no): ').lower()
    if user != 'yes':
        break

print('exiting program......')
