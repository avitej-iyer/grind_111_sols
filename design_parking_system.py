class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        self.bi, self.med, self.smol = big, medium, small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bi == 0:
                return False
            self.bi -= 1
            return True
        
        elif carType == 2:
            if self.med == 0:
                return False
            self.med -= 1
            return True
        
        elif carType == 3:
            if self.smol == 0:
                return False
            self.smol -= 1
            return True
        