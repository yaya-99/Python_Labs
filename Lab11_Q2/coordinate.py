class Coordinate:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        if isinstance(other,Coordinate):
            nx= self.x+other.x
            ny = self.y + other.y
            nz = self.z + other.z
            return Coordinate(nx,ny,nz)
        else:
            raise TypeError("Unsupported operand type for +")
        
    def mag(self):
        return (self.x**2+ self.y*2+self.z**2)**0.5
    
    def dir(self):
        return (self.x / self.mag(), self.y / self.mag(), self.z / self.mag())
    
    def dis(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"
    






































































