from classes.DigitalAsset import DigitalAsset
from classes.Reportable import Reportable

class MobileApp(DigitalAsset, Reportable):

    def __init__(self, avg_rating, downloads ,name, registration_date, cost):
        super().__init__(name, registration_date, cost)
        self.__avg_rating = avg_rating
        self.__downloads = downloads

    def calculate_value(self):
        self.__downloads * 0.5 + self.__avg_rating * 1000

    def asset_type(self):
        return "MOBILE_APP"

    def to_report_line(self):
        return f"{self.asset_type()}, {self.name}, {self.registration_date}..."