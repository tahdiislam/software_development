from abc import ABC, abstractmethod
from datetime import datetime


class Ride_sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f"{self.company_name} with drivers {len(self.drivers)} and riders {len(self.riders)}"


class User(ABC):
    def __init__(self, name, email, nid, initial_amount) -> None:
        self.name = name
        self.email = email
        self.nid = nid
        self.id = id
        self.wallet = initial_amount
        super().__init__()

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        self.current_ride = None
        self.current_location = current_location
        super().__init__(name, email, nid, initial_amount)

    def display_profile(self):
        print(f"Rider name is {self.name}, and email {self.email}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
            print(f"{amount}TK loaded successfully")
            print(f"Current balance is {self.wallet}TK")

    def request_ride(self, ride_sharing, destination):
        if not self.current_ride:
            # TODO: set ride properly
            # TODO: set current ride via ride match
            ride_requiest = Ride_request(self, destination)
            ride_matcher = Ride_matching(ride_sharing.drivers)
            self.current_ride = ride_matcher.find_driver(ride_requiest)

    def update_location(self, current_location):
        self.current_location = current_location

    def show_current_ride(self):
        print(self.current_ride)


class Driver(User):
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        self.current_location = current_location
        super().__init__(name, email, nid, initial_amount)

    def display_profile(self):
        print(f"Driver name {self.name} and email {self.email}")

    def accept_ride(self, ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, rider, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = rider
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.rider.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f"Ride details. Started {self.start_location} to {self.end_location}"


class Ride_request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location


class Ride_matching:
    def __init__(self, drivers) -> None:
        self.available_driver = drivers

    def find_driver(self, ride_request):
        if len(self.available_driver) > 0:
            # TODO: find the closest driver of the rider
            driver = self.available_driver[0]
            ride = Ride(
                ride_request.rider,
                ride_request.rider.current_location,
                ride_request.end_location,
            )
            driver.accept_ride(ride)
            return ride


class Vehicle(ABC):
    speed = {"car": 50, "bike": 60, "cng": 40}

    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = "available"
        super().__init__()

    @abstractmethod
    def start_drive(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = "unavailable"


class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = "unavailable"


# check the class integration

niye_jao = Ride_sharing("Niye jao")
sakib = Rider("sakib khan", "sakib@khan.com", 23343, "mohakhali", 1200)
niye_jao.add_rider(sakib)
kala_pakhi = Driver("kala pakhi", "lala@pakhi.com", "30233", "gulsan", 2000)
niye_jao.add_driver(kala_pakhi)
print(niye_jao)
sakib.request_ride(niye_jao, "uttara")
sakib.show_current_ride()
