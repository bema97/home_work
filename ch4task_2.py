class Airplane:
    def __init__(self, make, model,year, max_speed, odometer, is_flying=False):
            self.make = make
            self.model = model
            self.year = year
            self.max_speed = max_speed
            self.odometer = odometer
            self.is_flying = is_flying

    def take_off(self):
        self.is_flying = True
        print ("Airplane is flying")
        return self.take_off


    def fly (self, distance):
        self.distance = distance
        if self.distance != None:
            self.odometer += self.distance


    def land(self):
        self.is_flying = False
        print("Airplane landing")
        return self.is_flying


    def return_all(self):
        result = self.make + self.model
        result += self.year + self.max_speed
        result += str(self.odometer) + str(self.is_flying)
        return result

new_plane = Airplane('Boing ', '737 ', '1968 ', '970 km/h ' , 0)
print(new_plane.return_all())
        
new_plane.take_off()
new_plane.land()
new_plane.fly(8000)
new_plane.fly(80)
t1 =new_plane.return_all()
print(t1)
