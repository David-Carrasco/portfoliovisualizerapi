"""
Correspondence naming between www.portfoliovisualizer.com front and backend parameters
"""

NAMING_KEYS = {
    'Time Period': 'timePeriod',                    # Specify time period in years or in months
    'Start Year': 'startYear',                      # Start year for portfolio backtest
    'First Month': 'firstMonth',                    # Start month for portfolio backtest
    'End Year': 'endYear',                          # End year for portfolio backtest
    'Last Month': 'lastMonth',                      # End month for portfolio backtest
    'Calendar Aligned': 'calendarAligned',          # Align quarterly and annual cashflows and rebalancing with calendar periods or count from the portfolio start month
    'Include YTD': 'includeYTD',                    # Include the month-to-date period of the current month for YTD results
    'Initial Amount': 'initialAmount',              # Initial portfolio balance
    'Cashflows': 'annualOperation',                 # Specify whether any withdrawals or contributions are done
    'Contribution Amount': 'annualAdjustment',
    'Withdrawal Amount': 'annualAdjustment',
    'Withdrawal Percentage': 'annualPercentage',
    'Inflation Adjusted': 'inflationAdjusted',      # Adjust contribution or withdrawal amount for inflation
    'Contribution Frequency': 'frequency',          # 2 == monthly, 3 == quaterly, 4 == annualy
    'Withdrawal Frequency': 'frequency',
    'Rebalancing': 'rebalanceType',                 # Specify if and how rebalancing is done
    'Absolute Deviation': 'absoluteDeviation',      # Absolute percentage rebalancing corridor
    'Relative Deviation': 'relativeDeviation',      # Relative percentage rebalancing corridor. Set to zero to disable relative allocation checks.
    'Leverage Type': 'leverageType',                # Specify type of leverage used if any
    'Levarage Ratio': 'leverageRatio',              # Leverage ratio (debt/equity)
    'Debt Amount': 'debtAmount',                    # Amount of debt used for leverage
    'Debt Interest': 'debtInterest',                # Annual interest rate on borrowed funds
    'Maintenance Margin': 'maintenanceMargin',      # Maintenance margin requirement to prevent margin call
    'Leveraged Benchmark': 'leveragedBenchmark',    # Specify whether leverage is also applied to the selected benchmark
    'Reinvest Dividends': 'reinvestDividends',      # Reinvest dividends and distributions
    'Display Income': 'showYield',                  # Display portfolio income based on dividends and distributions
    'Factor Regression': 'showFactors',             # Display risk factor regression
    'Equity Factor Model': 'factorModel',           # Specify the equity factor model
    'Benchmark': 'benchmark',                       # Select benchmark index or an imported benchmark series
    'Benchmark Ticker': 'benchmarkSymbol'           # Ticker symbol for the benchmark asset
}


# NOTE: float or int values are not incluided in the values since are passed directly to the backend
NAMING_VALUES = {
    'Time Period': {
        'Month-to-Month': 2,
        'Year-to-Year': 4
    },
    'First Month': {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    },
    'Last Month': {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    },
    'Calendar Aligned': {
        'Yes': 'true',
        'No': 'false'
    },
    'Include YTD': {
        'Yes': 'true',
        'No': 'false'
    },
    'Cashflows': {
        'None': 0,
        'Contribute fixed amount': 1,
        'Withdraw fixed amount': 2,
        'Withdraw fixed percentage': 3
    },
    'Inflation Adjusted': {
        'Yes': 'true',
        'No': 'false'
    },
    'Contribution Frequency': {
        'Monthly': 2,
        'Quaterly': 3,
        'Annualy': 4
    },
    'Withdrawal Frequency': {
        'Monthly': 2,
        'Quaterly': 3,
        'Annualy': 4
    },
    'Rebalancing': {
        'No rebalancing': 0,
        'Rebalance annually': 1,
        'Rebalance semi-annually': 2,
        'Rebalance quarterly': 3,
        'Rebalance monthly': 4,
        'Rebalance bands': 5 
    },
    'Leverage Type': {
        'None': 0,
        'Fixed Debt Amount': 2,
        'Fixed Leverage Ratio': 1
    },
    'Leveraged Benchmark': {
        'Yes': 'true',
        'No': 'false'
    },
    'Reinvest Dividends': {
        'Yes': 'true',
        'No': 'false'
    },
    'Display Income': {
        'Yes': 'true',
        'No': 'false'
    },
    'Factor Regression': {
        'Yes': 'true',
        'No': 'false'
    },
    'Equity Factor Model': {
        'Three-Factor Model': 0,
        'Four-Factor Model': 1,
        'Five-Factor Model': 2
    },
    'Benchmark': {
        'None': '',
        'Specify Ticker...': -1,
        'Vanguard 500 Index Investor': 'VFINX',
        'Vanguard Balanced Index Inv': 'VBINX',
    }
}
