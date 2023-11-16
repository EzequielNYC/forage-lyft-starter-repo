from abc import ABC
from car import Car
from datetime import datetime 


class SplinderBattery(Car,ABC):
    def __init__(self, last_service_date,today):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.today = today

    def battery_should_be_serviced(self):
        years_since_last_service = self.today.year - self.last_service_date.year
        return years_since_last_service >= 2

class NubbinBattery(Car,ABC):
    def __init__(self, last_service_date,today):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.today = today

    def battery_should_be_serviced(self):
        years_since_last_service = self.today.year - self.last_service_date.year
        return years_since_last_service >= 4
