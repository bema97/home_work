class Car():
    def __init__(self, make, model, year, odometer, fuel):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70


    def drive(self, km):
        self.km = km

        if self.fuel*10 >= self.km:
            self.__add_distance()
        self.__subtract_fuel()

        
    def __add_distance(self):
        self.odometer += self.km
    

    def __subtract_fuel(self):
        
        if self.km <= self.fuel*10:
            print("\nLet's drive")
        else:
            print("Need more fuel, please, fill more.")

car_1 = Car('Toyota', 'Ist', 2002, 0, 70)

car_1.drive(700)
resoult = str(car_1.odometer) + " " + str(car_1.fuel)

print(resoult)

        