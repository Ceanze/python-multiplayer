# Get position
# Jump
# moveDirection(dir:vec2)void

# p;11.11/22.22/33.33

class Physics:
    '''Physics class that is per player'''

    jumpSpeed = 10
    isJumping = False

    def __init__(self, position, maxVelocity):
        self.position = position
        self.maxVelocity = maxVelocity
        self.acceleration = [0, 0]
        self.velocity = 0
        self.gravity = 0.2
        self.dt = 1

    def move(self, direction):
        if direction[0] > 0 and self.acceleration[0] < self.maxVelocity:
            self.acceleration[0] += direction[0]
        elif direction[0] < 0 and self.acceleration[0] > -self.maxVelocity:
            self.acceleration[0] += direction[0]

    def setMaxVelocity(self, velocity):
        self.maxVelocity = velocity

    def setPosition(self, position):
        self.position = position

    def jump(self):
        self.isJumping = True
        if self.position[1] == 470:
            self.acceleration[1] -= self.jumpSpeed
            self.position[1] -= 1

    def getPosition(self):
        return self.position

    def update(self, dt):
        for i in range(0, abs(int(self.acceleration[1]))):
            if self.acceleration[1] > 0:
                self.position[1] += 1
            else:
                self.position[1] -= 1              

            if self.position[1] == 470:
                self.acceleration[1] = 0

        for i in range(0, abs(int(self.acceleration[0]))):
            if self.acceleration[0] > 0:
                self.position[0] += 1
            else:
                self.position[0] -= 1              

        if self.position[1] < 470:
            self.acceleration[1] += self.gravity
        
        
        if self.acceleration[0] != 0:
            if self.acceleration[0] > 0:
                self.acceleration[0] -= 0.1
            else:
                self.acceleration[0] += 0.1    
            

        # if self.acceleration[0] != 0:
        #     print(self.acceleration[0])
