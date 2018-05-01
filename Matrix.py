
class Vec3:
    def __init__(self, f1, f2, f3):
        self.values = [f1, f2, f3]

    def __mul__(self, other):
        self.values[0] *= other.values[0]
        self.values[1] *= other.values[1]
        self.values[2] *= other.values[2]
        return self


    # operator[]
    def __getitem__(self, key):
        if(key > 2):
            print("Vec3: Key out of range")
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __rmul__(self, other):
        print ('__rmul__')
        return other

    def __str__(self):
        return str(self.values)

    def length(self):
        l = pow((pow(self.values[0],2) + pow(self.values[1],2) + pow(self.values[2],2)), 0.5)
        return l



class Mat3:
    def __init__(self, vec3top = Vec3(1,0,0) , vec3mid= Vec3(0,1,0) , vec3bot= Vec3(0,0,1)):
        self.values = [vec3top, vec3mid, vec3bot]

    def __mul__(self, other):
        temp = Mat3()
        for x in range(0,3):
            for y in range(0,9):
                self.values[x][y] *= other.values[y][x]
        return self
    def __rmul__(self, other):
        print ('__rmul__')
        return other
        
    def __str__(self):
        return str(str(self.values[0]) + "\n" + str(self.values[1]) + "\n" + str(self.values[2]))

h = Mat3(Vec3(1,2,3), Vec3(4,5,6), Vec3(7,8,9))
v = Mat3(Vec3(9,7,8), Vec3(6,5,4), Vec3(3,2,1))


h *= v

print(h)


