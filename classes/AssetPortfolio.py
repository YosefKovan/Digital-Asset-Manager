from os import write

from classes.Website import Website
from classes.MobileApp import MobileApp


class AssetPortfolio:

    def __init__(self, file_name="digital_assets.csv"):
        self.__assets = []
        self.__filename = file_name


    def add_asset(self, asset):
        self.__assets.append(asset)

    def calculate_total_net_worth(self):
        total_cost = 0
        for prop in self.__assets:
            total_cost += prop.calculate_value() - prop.cost

        return str(round(total_cost, 2))


    def save_portfolio(self):
        with open(self.__filename, 'w') as f:
            f.write('Type, Name, Date, Cost \n')
            for asset in self.__assets:
                f.write(asset.to_report_line())

    def create_object(self, obj_type, split_line):

        match obj_type:
            case "WEBSITE" :
                self.__assets.append(Website(int(split_line[1]), float(split_line[2]), str(split_line[3]), split_line[4], split_line[5]))
            case "MOBILE_APP":
                self.__assets.append(MobileApp(int(split_line[1]), float(split_line[2]), str(split_line[3]), split_line[4], split_line[5]))


    def load_portfolio(self):
        self.__assets = []

        try:

            with open(self.__filename, 'r') as f:
                f.readline()
                for line in f:
                    split_line = line.split(',')
                    self.create_object(split_line[0], split_line)

        except FileNotFoundError:
            print("File not found!!!")











