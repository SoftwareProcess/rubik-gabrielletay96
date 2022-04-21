class Point:
    """A 3D point/vector"""

    def __init__(self, x, y=None, z=None):
        #Construct a Point from an (x, y, z) tuple
        try:
            # convert from an iterable
            i = iter(x)
            self.x = next(i)
            self.y = next(i)
            self.z = next(i)
        except TypeError:
            # not iterable
            self.x = x
            self.y = y
            self.z = z
    
    def dot(self, other):
        # Returns the dot product"""
        return self.x * other.x + self.y * other.y + self.z * other.z

        
    def count(self, val):
        return int(self.x == val) + int(self.y == val) + int(self.z == val)

    
class Matrix:
    def __init__(self, *args):
        self.vals = list(args)
        
    def rows(self):
        yield self.vals[0:3]
        yield self.vals[3:6]
        yield self.vals[6:9]

    def cols(self):
        yield self.vals[0:9:3]
        yield self.vals[1:9:3]
        yield self.vals[2:9:3]
