circle1ID = 1
circle1Radius = 10
circle1Color = 'blue'
circle1Display = True

circle1ID = 1
circle1Radius = 10
circle1Color = 'blue'
circle1Display = True

circle1ID = 1
circle1Radius = 10
circle1Color = 'blue'
circle1Display = True

print('Circle 1 circumference is: ' + str(3.141 * 2 * circle1Radius))
print('Circle 2 circumference is: ' + str(3.141 * 2 * circle1Radius))
print('Circle 3 circumference is: ' + str(3.141 * 2 * circle1Radius))

# ^ Convert to class implementation

class Circle:
    '''Class to create a circle'''
    id = 0
    radius = 0
    color = ''
    display = True

    # ^ State, below is behavior

    def __init__(self, id, radius, color, display):
        self.id = id
        self.radius = radius
        self.color = color
        self.display = display
    
    def getCircumference(self):
        return 3.141 * 2 * self.radius

circle1 = Circle(1,10,'blue',True)
circle2 = Circle(2,8,'red',True)
circle3 = Circle(3,5,'green',True)

print('Circle 1 circumference is: ' + str(circle1.getCircumference()))
print('Circle 2 circumference is: ' + str(circle2.getCircumference()))
print('Circle 3 circumference is: ' + str(circle3.getCircumference()))
