from math import pi

def area_of_circle(r):
    if r<0:
        raise ValueError('Negative radius value error') # Raise an error if supplied radius is negative. Helps with unit testing as well.
    return pi*(r**2)