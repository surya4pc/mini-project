import unittest
from currency_conversion import RealTimeCurrencyConverter, CurrencyConverterApp

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

class TestCurrencyConverterApp(unittest.TestCase):
    def setUp(self):
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        self.converter = RealTimeCurrencyConverter(url)
        self.app = CurrencyConverterApp(self.converter)

    def test_restrict_number_only(self):
        valid_cases = ['123', '12.34', '0.56']
        invalid_cases = ['abc', '12.34.56', '12a']

        for case in valid_cases:
            result = self.app.restrict_number_only('%d', case)
            self.assertTrue(result)

        for case in invalid_cases:
            result = self.app.restrict_number_only('%d', case)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
