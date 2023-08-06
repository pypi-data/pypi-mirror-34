""" Test security info """

import sys
sys.path.insert(0, '../src')

from gnucash_portfolio_cli import security_info


def test_latest_price():
    """ Check the latest price date """
    #security_info()

def test_return_of_capital():
    """ debug through the return of capital calculation """
    security_info.main()
    