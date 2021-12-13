from portfoliovisualizerapi.backtest_api import BacktestPortfolio, ParserPortfolio
from portfoliovisualizerapi.conf import base_config


example_asset_allocation = {
    "SPY": 30,
    "QQQ": 20,
    "TLT": 50
}


if __name__ == "__main__":
    portfolio = BacktestPortfolio(conf_portfolio=base_config)
    portfolio.setup_asset_allocation(example_asset_allocation)
    url = portfolio.build_url()
    print(ParserPortfolio(url).get_backtest())
