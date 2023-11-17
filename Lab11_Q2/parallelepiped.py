class Parallelepiped:
    def __init__(self, coordinate1, coordinate2, coordinate3):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2
        self.coordinate3 = coordinate3

# Using vector triple product to calculate the volume of parallelepiped

    def volume(self):
        v1 = self.coordinate1.x * (self.coordinate2.y * self.coordinate3.z - self.coordinate2.z * self.coordinate3.y)
        v2 = self.coordinate1.y * (self.coordinate2.z * self.coordinate3.x - self.coordinate2.x * self.coordinate3.z)
        v3 = self.coordinate1.z * (self.coordinate2.x * self.coordinate3.y - self.coordinate2.y * self.coordinate3.x)
        return abs(v1 + v2 + v3)