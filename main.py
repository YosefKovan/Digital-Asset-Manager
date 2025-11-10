from datetime import datetime

from classes.AssetPortfolio import AssetPortfolio
from classes.MobileApp import MobileApp
from classes.Website import Website

if __name__ == "__main__":
    my_portfolio = AssetPortfolio()
    my_portfolio.load_portfolio()

    website = Website(20, 20, "Beiti", datetime.now(), 100)
    mobile_app = MobileApp(10, 200, "Driver Tech", datetime.now(), 20)

    my_portfolio.add_asset(website)
    my_portfolio.add_asset(mobile_app)

    print(my_portfolio.calculate_total_net_worth())
    my_portfolio.save_portfolio()
