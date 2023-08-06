#!/usr/bin/env python3
"""
Display security details: holding accounts, quantity, value, last price w/ date, asset class.
Calculate:
    - Return of Capital
    - Yield
argparse can effectively replace click for building CLIs.
"""
import argparse
import logging

from piecash import Commodity, Account
from gnucash_portfolio import BookAggregate
from pricedb import PriceDbApplication, PriceModel, SecuritySymbol

from model.security_models import SecurityDetailsViewModel


def read_parameters():
    """ Read parameters from the command line """
    parser = argparse.ArgumentParser(description='read symbol from command line')
    parser.add_argument('symbol', type=str, help='security symbol')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    return args


def __get_model_for_details(
        svc: BookAggregate, symbol: str) -> SecurityDetailsViewModel:
    """ Loads the model for security details """
    sec_agg = svc.securities.get_aggregate_for_symbol(symbol)

    model = SecurityDetailsViewModel()

    model.symbol = sec_agg.security.namespace + ":" + sec_agg.security.mnemonic
    model.security = sec_agg.security

    # Quantity
    model.quantity = sec_agg.get_quantity()
    model.value = sec_agg.get_value()
    currency = sec_agg.get_currency()
    if currency:
        assert isinstance(currency, str)
        model.currency = currency
    model.price = sec_agg.get_last_available_price()

    model.average_price = sec_agg.get_avg_price()
    # Here we take only the amount paid for the remaining stock.
    model.total_paid = sec_agg.get_total_paid_for_remaining_stock()

    # Profit/loss
    model.profit_loss = model.value - model.total_paid
    if model.total_paid:
        model.profit_loss_perc = abs(model.profit_loss) * 100 / model.total_paid
    else:
        model.profit_loss_perc = 0
    if abs(model.value) < abs(model.total_paid):
        model.profit_loss_perc *= -1
    # Income
    model.income = sec_agg.get_income_total()
    if model.total_paid:
        model.income_perc = model.income * 100 / model.total_paid
    else:
        model.income_perc = 0
    # income in the last 12 months
    # income_last_year = sec_agg.get_income_total
    # model.income_perc_last_12m = 0

    # Return of Capital
    roc = sec_agg.get_return_of_capital()

    # total return
    model.total_return = model.profit_loss + model.income
    if model.total_paid:
        model.total_return_perc = model.total_return * 100 / model.total_paid
    else:
        model.total_return_perc = 0

    # load all accounts
    model.accounts = sec_agg.accounts
    model.income_accounts = sec_agg.get_income_accounts()

    # Load asset classes to which this security belongs.
    # todo load asset allocation, find the parents for this symbol
    # svc.asset_allocation.load_config_only(svc.currencies.default_currency)
    # stocks = svc.asset_allocation.get_stock(model.symbol)
    #
    # for stock in stocks:
    #     model.asset_classes.append(stock.asset_class)
    from asset_allocation import AppAggregate
    aa = AppAggregate()
    aa.open_session()
    aa.get_asset_classes_for_security(None, model.symbol)

    return model

def __display(model: SecurityDetailsViewModel):
    """ Format and display the results """
    # header
    print("    security            quantity  ")
    print("-------------------------------------------------------")

    #shares = agg.get_num_shares()
    
    print(f"{model.security.namespace}:{model.security.mnemonic}, shares: {model.quantity:,.2f}")

    # todo add all the info from the security details page in web ui,
    # prices, etc.
    # avg_price = agg.get_avg_price()
    #currency = agg.get_currency()
    currency = model.currency
    print(f"Average price: {model.average_price:.2f} {currency}")

    # last price
    prices_app = PriceDbApplication()
    sec_symbol = SecuritySymbol("", "")
    sec_symbol.parse(model.symbol)
    latest_price = prices_app.get_latest_price(sec_symbol)
    latest_price_date = latest_price.datum.to_iso_date_string()
    logging.debug(latest_price)
    print(f"Latest price: {latest_price.value:.2f} {latest_price.currency} on {latest_price_date}")

    print("")

    # Income
    print(f"Income: {model.income:,.2f} {model.currency}, {model.income_perc:.2f}%")
    

    print("")

    print("Holding Accounts:")
    print("-----------------")

    for account in model.accounts:
        balance = account.get_balance()
        value = balance * latest_price.value
        print(f"{account.fullname}, {balance:,.2f} units, {value:,.2f} {latest_price.currency}")


def main():
    args = read_parameters()
    symbol = args.symbol
    symbol = symbol.upper()

    book = BookAggregate()

    agg = book.securities.get_aggregate_for_symbol(symbol)
    security = agg.security

    model = __get_model_for_details(book, symbol)

    # Display
    if security is None:
        print(f"No securities found for {symbol}.")
        exit

    __display(model)


if __name__ == "__main__":
    main()
