from Vehicle_class import Vehicle;

class Car(Vehicle):
    trunk_open=False;
    
    def open_trunk(self):
        self.trunk_open=True;
        print("Trunk opened!");
    
    def close_trunk(self):
        self.trunk_open=False;
        print("Trunk closed!");
        
carlos = Car(started=True, speed=50);

#Inheritence behaviour
print(carlos.open_trunk());