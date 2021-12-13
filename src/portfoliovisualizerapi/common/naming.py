"""
Correspondence naming between www.portfoliovisualizer.com input and backend parameters
"""

NAMING_KEYS = {
    'Time Period': 'timePeriod',
    'Start Year': 'startYear',
    'First Month': 'firstMonth',
    'End Year': 'endYear',
    'Last Month': 'lastMonth',
    'Calendar Aligned': 'calendarAligned',
    'Include YTD': 'includeYTD',
    'Initial Amount': 'initialAmount',
    'Cashflows': 'annualOperation',  # 0,1,2,3
    'Contribution Amount': 'annualAdjustment',
    'Withdrawal Amount': 'annualAdjustment',
    'Withdrawal Percentage': 'annualPercentage',
    'Inflation Adjusted': 'inflationAdjusted',
    'Contribution Frequency': 'frequency', # 2 == monthly, 3 == quaterly, 4 == annualy
    'Withdrawal Frequency': 'frequency',
    'Rebalancing': 'rebalanceType',
    'Absolute Deviation': 'absoluteDeviation',
    'Relative Deviation': 'relativeDeviation',
    'Leverage Type': 'leverageType',
    'Levarage Ratio': 'leverageRatio',
    'Debt Amount': 'debtAmount',
    'Debt Interest': 'debtInterest',
    'Maintenance Margin': 'maintenanceMargin',
    'Leveraged Benchmark': 'leveragedBenchmark',
    'Reinvest Dividends': 'reinvestDividends',
    'Display Income': 'showYield',
    'Factor Regression': 'showFactors',
    'Equity Factor Model': 'factorModel',
    'Benchmark': 'benchmark',
    'Benchmark Ticker': 'benchmarkSymbol'
}

NAMING_VALUES = {
    
}