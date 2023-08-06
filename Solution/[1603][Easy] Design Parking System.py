class ParkingSystem:
    def __init__(self, big, medium, small):
        self.num_left = [big, medium, small]

    def addCar(self, carType):
        self.num_left[carType-1] -= 1
        return self.num_left[carType-1] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)