from classes.DigitalAsset import DigitalAsset
from classes.Reportable import Reportable

class Website(DigitalAsset, Reportable):

    def __init__(self, monthly_traffic, monetization_rate, name, registration_date, cost):
        super().__init__(name, registration_date, cost)
        self.__monthly_traffic = monthly_traffic
        self.__monetization_rate = monetization_rate

    def calculate_value(self):
        return self.__monthly_traffic * self.__monetization_rate * 12

    def asset_type(self):
        return "WEBSITE"

    def to_report_line(self):
        return f"{self.asset_type()}, {self.__monthly_traffic}, {self.__monetization_rate}, {self.name}, {self.registration_date}, {self.cost}"

