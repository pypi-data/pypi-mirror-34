#!/usr/bin/env python3
""" Portfolio Value report """

from pydatum import Datum


def main():
    from gnucash_portfolio.reports import portfolio_value
    from gnucash_portfolio.model.stock_model import StockViewModel
    from gnucash_portfolio.reports.portfolio_models import PortfolioValueInputModel, PortfolioValueViewModel

    parameters = PortfolioValueInputModel()
    today = Datum()
    today.today()
    parameters.as_of_date = today.value
    model = portfolio_value.run(parameters)

    # Display
    print_row("security", "cost", "balance", "gain/loss", "%", "income")
    print("------------------------------------------------------------------------------------------------")

    rows = sorted(model.stock_rows, key=lambda row: f"{row.exchange}:{row.symbol}")

    for row in rows:
        x = StockViewModel()
        col1 = f"{row.exchange}:{row.symbol}"
        col2 = f"{row.shares_num:,} @ {row.avg_price:,.2f} {row.currency} = {row.cost:,.2f}"
        col3 = f"@ {row.price:,.2f} = {row.balance:,.2f}"
        col4 = f"{row.gain_loss:,.2f}"
        col5 = f"{row.gain_loss_perc:,.2f}%"
        col6 = f"{row.income:,.2f}"

        print_row(col1, col2, col3, col4, col5, col6)


def print_row(col1, col2, col3, col4, col5, col6):
    """ Print the values in one row """
    line = f"{col1:<15} {col2:>32} {col3:>20} {col4:>10} {col5:>8} {col6:>8}"
    print(line)


if __name__ == "__main__":
    main()
