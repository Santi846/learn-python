class Vehicle:
    # speed=0;
    # started=False;
    
    #improving init method, adding parameters inside it
    def __init__(self, started=False, speed=0):
        self.started=started;
        self.speed=speed;   
    
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
vehicle = Vehicle();
vehicle_two = Vehicle(started=True);
vehicle_three = Vehicle(started=True, speed=50);
vehicle_four = Vehicle(speed=40);
# for printing car increase speed, we need at firts to start the car object
# car.start();
# print(car.increase_speed(10));

#print objects id
# print(id(car),id(car_two), car.started, car_two.started);

#Class tree structure
# print("Class structure: -> ", dir(Car));

#Objetc tree structure
# print("Objetc structure: -> ", dir(car_two));

#print object instance
print(vehicle_two);

#Inheritence
