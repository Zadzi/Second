import unittest
from calculator import CurrencyCalculator


class TestCurrencyCalculatorExist(unittest.TestCase):
    def setUp(self):
        self.calculator = CurrencyCalculator()

    def testCurrencyCalculatorHasEuroExchangeRate(self):
        assert self.calculator.euro_exchange_rate != None, "calculator euro_exchange_rate is None"

    def testCurrencyCalculatorHasPoundExchangeRate(self):
        assert self.calculator.pound_exchange_rate != None, "calculator pound_exchange_rate is None"

    def testCurrencyCalculatorSetEuroExchangeRate(self):
        self.calculator.setEuroExchangeRate(1.1)
        assert self.calculator.euro_exchange_rate == 1.1, "calculator euro_exchange_rate did not set correctly"

    def testCurrencyCalculatorSetPoundExchangeRate(self):
        self.calculator.setPoundExchangeRate(502)
        assert self.calculator.pound_exchange_rate == 502, "calculator pound_exchange_rate did not set correctly"

    def testCurrencyCalculatrPoundsToPLN(self):
        self.calculator.setPoundExchangeRate(4.6)
        assert self.calculator.poundsToPLN(1) == 4.6, "calculator poundsTOPLN failed"
        assert self.calculator.poundsToPLN(2) == 9.2, "calculator poundsTOPLN failed"

    def testCurrencyCalculatorEurosToPLN(self):
        self.calculator.setEuroExchangeRate(4.1)
        assert self.calculator.eurosToPLN(1) == 4.1, "calculator eurosToPLN failed"
        assert self.calculator.eurosToPLN(2) == 8.2, "calculator eurosToPLN failed"




if __name__ == "__main__":
    unittest.main()