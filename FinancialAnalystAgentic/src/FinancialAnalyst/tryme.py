# -- delete this later ---
import finanalysis.ratios as fira

def main():
    stock_symbol = "MSFT"
    print("Liquidity Ratios")
    print(fira.liquidity_ratios(stock_symbol))
    print("Profitability Ratios")
    print(fira.profitability_ratios(stock_symbol))
    print("Efficiency Ratios")
    print(fira.efficiency_ratios(stock_symbol))
    print("Valuation Ratios")
    print(fira.valuation_ratios(stock_symbol))
    print("Leverage Ratios")
    print(fira.leverage_ratios(stock_symbol))
    print("Performance & Growth Metrics")
    print(fira.performance_and_growth_metrics(stock_symbol))

if __name__ == "__main__":
    main()