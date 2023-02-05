import unittest
import requests_mock
import retrieve_data

class TestRetrieveData(unittest.TestCase):
    @requests_mock.Mocker()
    def test_retrieve_data_success(self, mock_requests):
        mock_requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC%2CETH%2CSOL%2CDOGE&convert=USD&CMC_PRO_API_KEY=4f0a6417-58ab-41f1-8770-6cf42db5d653", 
                          json={"data": {"BTC": {"quote": {"USD": {"price": 12345}}}}}, 
                          status_code=200)
        result = retrieve_data.retrieve_data("USD")
        self.assertEqual(result, {"BTC": {"price": 12345}})

    @requests_mock.Mocker()
    def test_retrieve_data_failure(self, mock_requests):
        mock_requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC%2CETH%2CSOL%2CDOGE&convert=USD&CMC_PRO_API_KEY=4f0a6417-58ab-41f1-8770-6cf42db5d653", 
                          status_code=500)
        with self.assertRaises(Exception) as context:
            retrieve_data.retrieve_data("USD")
        self.assertEqual(str(context.exception), "Error in retrieving data")

if __name__ == '__main__':
    unittest.main()
