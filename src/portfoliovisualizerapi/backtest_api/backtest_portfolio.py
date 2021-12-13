"""
Backtest Portfolio Asset Allocation API endpoint
https://www.portfoliovisualizer.com/backtest-portfolio
"""
from typing import Dict, Union
from portfoliovisualizerapi.common.naming import NAMING_KEYS, NAMING_VALUES


BASE_URL = "https://www.portfoliovisualizer.com/backtest-portfolio?s="


class BacktestPortfolio():
    
    def __init__(self,
                 conf_portfolio: Dict[str, Union[str, float]],
                 base_naming_keys: Dict[str, str] = NAMING_KEYS,
                 base_naming_values: Dict[str, str] = NAMING_VALUES,
                 base_url: str = BASE_URL):
        # TODO
        # _setup_portfolio_config(self,
        #                         base_naming_keys,
        #                         base_naming_values)
        pass

    def _setup_portfolio_config():
        # TODO
        # replace keys and values with the appropiate base_naming dicts
        pass

    def setup_asset_allocation(conf_allocation: Dict[str, float]):
        # assert sum of values is as max 100%
        # TODO
        pass

    def build_url(self):
        # TODO
        # build url and return value
        pass
