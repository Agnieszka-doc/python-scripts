import math

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
		
    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    
    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def __mul__(self, other):  # iloczyn skalarny
        return (self.x * other.x +
                self.y * other.y +
                self.z * other.z)

    def cross(self, other):  # iloczyn wektorowy
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __hash__(self):
        return hash((self.x, self.y, self.z))
        
# do zadania 7_1
def find_axis(v1, v2):
    axis = v1.cross(v2)
    length = axis.length()

    if length == 0:
        raise ValueError("Vectors are parallel or zero")

    return Vector(axis.x / length,
                  axis.y / length,
                  axis.z / length)
                
# TEST
v1 = Vector(1, 0, 0)
v2 = Vector(0, 1, 0)

axis = find_axis(v1, v2)
print(axis)  # Vector(0, 0, 1)

# TEST 
v1 = Vector(1, 0, 0)
v2 = Vector(2, 0, 0)

try:
    find_axis(v1, v2)
except ValueError as e:
    print("Error:", e)