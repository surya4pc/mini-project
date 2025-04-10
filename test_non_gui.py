import unittest
from currency_conversion import RealTimeCurrencyConverter

class TestRealTimeCurrencyConverter(unittest.TestCase):
    def test_get_exchange_rates(self):
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        converter = RealTimeCurrencyConverter(url)
        data = converter.get_exchange_rates(url)
        self.assertIsNotNone(data)
        self.assertIn('rates', data)

    def test_convert(self):
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        converter = RealTimeCurrencyConverter(url)
        converted_amount = converter.convert('INR', 'USD', 1)
        self.assertIsNotNone(converted_amount)
        self.assertIsInstance(converted_amount, float)

if __name__ == '__main__':
    unittest.main()
