# write a class to c-2d vector and use it to create another class representing a 3-d vector.


class vector2d:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def printvector2d(self):
        print(self.i,"i","+",self.j,"j")


class vector3d(vector2d):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def printvector3d(self):
        print(self.i,"i","+",self.j,"j","+",self.k,"k")


v2 = vector2d(1, 3)
v3 = vector3d(1, 6, 8)

v2.printvector2d()
v3.printvector3d()
