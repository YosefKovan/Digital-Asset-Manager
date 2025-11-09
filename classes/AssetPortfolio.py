

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







