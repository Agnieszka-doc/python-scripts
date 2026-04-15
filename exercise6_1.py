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


# ===== TESTY =====

v = Vector(1, 2, 3)
w = Vector(2, -3, 2)

assert v != w
assert v + w == Vector(3, -1, 5)
assert v - w == Vector(-1, 5, 1)
assert v * w == 2
assert v.cross(w) == Vector(13, 4, -7)
assert v.length() == math.sqrt(14)

S = set([v, v, w])
assert len(S) == 2

print("Tests passed")

# ===== TESTY =====

v = Vector(0, 0, 0)
w = Vector(5, -2, 3)

assert v != w
assert v + w == Vector(5, -2, 3)
assert v - w == Vector(-5, 2, -3)
assert v * w == 0
assert v.cross(w) == Vector(0, 0, 0)
assert v.length() == 0

S = set([v, v, w])
assert len(S) == 2

print("Tests passed")

# ===== TESTY =====

v = Vector(-2, -1, 3)
w = Vector(4, -3, 1)

assert v != w
assert v + w == Vector(2, -4, 4)
assert v - w == Vector(-6, 2, 2)
assert v * w == (-2)*4 + (-1)*(-3) + 3*1  # -8 + 3 + 3 = -2
assert v.cross(w) == Vector((-1)*1 - 3*(-3), 3*4 - (-2)*1, (-2)*(-3) - (-1)*4)
assert v.length() == math.sqrt(14)

S = set([v, v, w])
assert len(S) == 2

print("Tests passed")