from portfoliovisualizerapi.backtest_api.backtest_portfolio import BacktestPortfolio
from portfoliovisualizerapi.backtest_api.parse_portfolio import ParserPortfolio


name_portfolio = "test_simple_backtest"

conf = {
    'Time Period': 'Year-to-Year',
    'Start Year': 1985,
    'First Month': 'Jan',
    'End Year': 2021,
    'Last Month': 'Dec',
    'Include YTD': 'Yes',
    'Initial Amount': 10000, # $
    'Cashflows': 'None',
    'Rebalancing': 'No rebalancing',
    'Leverage Type': 'None',
    'Reinvest Dividends': 'Yes',
    'Display Income': 'Yes',
    'Factor Regression': 'No',
    'Benchmark': 'Vanguard 500 Index Investor',
}

asset_allocation = {
    "SPY": 30,
    "QQQ": 20,
    "TLT": 50
}


if __name__ == "__main__":
    portfolio = BacktestPortfolio(conf_portfolio=conf)
    portfolio.setup_portfolio_name(name_portfolio)
    portfolio.setup_asset_allocation(asset_allocation)
    url = portfolio.build_url()
    print(url)
    print(ParserPortfolio(url).get_backtest())
