from abc import ABC, abstractmethod

# Step 1: Create an abstract base class Vehicle with start_engine() method
class Vehicle(ABC):
    def __init__(self, make, model, region_spec):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self):
        pass

# Step 2: Modify Car and Motorcycle classes to inherit from Vehicle
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region_spec} Spec): Engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region_spec} Spec): Engine started")

# Step 3: Create an abstract VehicleFactory class with create_car() and create_motorcycle() methods
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

# Step 4: Implement two factory classes: USVehicleFactory and EUVehicleFactory
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")

# Step 5: Update initial code to use factories for vehicle creation
# Using US factory
us_factory = USVehicleFactory()
vehicle1 = us_factory.create_car("Toyota", "Corolla")
vehicle1.start_engine()

# Using EU factory
eu_factory = EUVehicleFactory()
vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()