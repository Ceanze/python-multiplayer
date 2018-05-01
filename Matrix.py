
import math
import copy

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
    def __init__(self, vec3left = Vec3(1,0,0) , vec3mid= Vec3(0,1,0) , vec3right= Vec3(0,0,1)):
        self.values = [vec3left, vec3mid, vec3right]

    def __mul__(self, other):
        temp = Mat3(self.values[0], self.values[1], self.values[2])
        for x in range(0,3):
            for y in range(0,3):
                self.values[x][y] = temp.values[0][x]*other.values[y][0] + temp.values[1][x]*other.values[y][1] + temp.values[2][x]*other.values[y][2]
        return self
    def __rmul__(self, other):
        print ('__rmul__')
        return other
        
    def __str__(self):
        return str(str(self.values[0]) + ", " + str(self.values[1]) + ", " + str(self.values[2]))

    def copy(self, other):
        self = copy.deepcopy(other)
        return self
    
    def rotate(self, angle):
        rot = Mat3(Vec3(math.cos(angle), math.sin(angle), 0), Vec3(-math.sin(angle), math.cos(angle), 0), Vec3(0, 0, 1))
        return self * rot

    # This does not work
    def rotateAround(self, angle, target):
        rot = Mat3(Vec3(math.cos(angle), math.sin(angle), 0), Vec3(-math.sin(angle), math.cos(angle), 0), Vec3(-target[0], -target[1], 1))
        translate = Mat3(Vec3(1,0,0), Vec3(0,1,0), Vec3(target[0], target[1], 1))
        self *= rot
        translate *= self
        self.copy(translate)
        return self

    def move(self, translation):
        self.values[2][0] += translation[0]
        self.values[2][1] += translation[1]
        return self

    def getPosition(self):
        return [self.values[2][0], self.values[2][1]]

h = Mat3(Vec3(1,0,0), Vec3(0,1,0), Vec3(0,0,1))
v = Mat3(Vec3(2,0,0), Vec3(0,2,0), Vec3(0,0,2))


h *= v

print(h)


