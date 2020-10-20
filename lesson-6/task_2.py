class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self.length * self.width * self.weight * self.height / 1000
        print(asphalt_mass)

r = Road(3000, 40)
r.asphalt_mass()