"""
Backtest Portfolio Asset Allocation API endpoint
https://www.portfoliovisualizer.com/backtest-portfolio
"""
import logging
from typing import Dict, Union
from portfoliovisualizerapi.common.naming import NAMING_KEYS, NAMING_VALUES
from portfoliovisualizerapi.common.utils import (validate_input_keys,
                                                 validate_input_values,
                                                 apply_naming_keys,
                                                 apply_naming_values)


logger = logging.getLogger(__name__)

BASE_URL = "https://www.portfoliovisualizer.com/backtest-portfolio?s="


class BacktestPortfolio():

    base_url = BASE_URL
    naming_keys = NAMING_KEYS
    naming_values = NAMING_VALUES

    def __init__(self,
                 conf_portfolio: Dict[str, Union[str, float]]):
        self._base_conf = self._setup_config(conf_portfolio)

    def __repr__(self):
        return "API for https://www.portfoliovisualizer.com/backtest-portfolio"

    @property
    def base_conf(self):
        return self._base_conf

    def _setup_config(self, conf_portfolio: Dict[str, Union[str, float]]):

        assert validate_input_keys(conf_portfolio, self.naming_keys)
        assert validate_input_values(conf_portfolio, self.naming_values)

        # replace values and keys with the appropiate naming dicts
        conf_naming_values = apply_naming_values(conf_portfolio, self.naming_values)

        return apply_naming_keys(conf_naming_values, self.naming_keys)

    def setup_portfolio_name(self, name: str):

        # activate portfolio names option
        self.base_conf.update({'portfolioNames': 'true'})

        # add portfolio name
        self.base_conf.update({'portfolioName1': name})

    def setup_asset_allocation(self, conf_allocation: Dict[str, float]):
        
        for i, (ticker, allocation) in enumerate(conf_allocation.items(), start=1):

            # add ticker
            self.base_conf.update({f'symbol{i}': ticker})

            # add allocation percentage
            self.base_conf.update({f'allocation{i}_1': allocation})

        assert self._total_allocation_percentage() == 100

    def _total_allocation_percentage(self):
        return sum(
            {key:value for (key,value)
             in self.base_conf.items()
             if key.startswith('allocation')}.values()
        )

    def build_url(self):
        parameters = ['='.join([key, str(value)])
                      for (key, value) in self.base_conf.items()]

        return '&'.join([self.base_url] + parameters)
