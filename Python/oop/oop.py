class Car:
    def __init__(self, brand, model, year, color, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        return amount

    def brake(self,amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        return self.speed

    def get_speed(self):
        return self.speed

    def honk(self):
        return "Beep beep! I'm a Toyota!"

car1 = Car("Toyota", "Corolla", 2023, "Red")
car1.accelerate(50)
print(car1.get_speed())  # Should print 50
car1.brake(20)
print(car1.get_speed())  # Should print 30
print(car1.honk())  # Should print "Beep beep! I'm a Toyota!"
