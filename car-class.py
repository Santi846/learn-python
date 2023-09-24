class Car:
    speed=0;
    started=False;
    
    # self is for calling the object, itself
    def start(self):
        self.started=True;
        print("Car started, let's ride!");
    
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooooom!');
        else:    
            print('You need to start the car first');
        
    def stop(self):
        self.speed=0
        print('Halting');
        
# Object instance
car = Car();
car_two = Car();
# for printing car increase speed, we need at firts to start the car object
car.start();
# print(car.increase_speed(10));

#print objects id
print(id(car),id(car_two), car.started, car_two.started);
