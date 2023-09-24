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
car.start();
print(car.increase_speed(10));

