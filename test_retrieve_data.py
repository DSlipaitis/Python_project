import unittest
import requests_mock
import retrieve_data


class TestRetrieveData(unittest.TestCase):
    @requests_mock.Mocker()
    def test_retrieve_data_success(self, mock_requests):
        mock_requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC%2CETH%2CSOL%2CDOGE&convert=USD&CMC_PRO_API_KEY=4f0a6417-58ab-41f1-8770-6cf42db5d653",
                          json={
                              "data": {
                                  "BTC": {
                                      "quote": {
                                          "USD": {
                                              "price": 50
                                          }
                                      }
                                  },
                                  "ETH": {
                                      "quote": {
                                          "USD": {
                                              "price": 60
                                          }
                                      }
                                  },
                                  "SOL": {
                                      "quote": {
                                          "USD": {
                                              "price": 70
                                          }
                                      }
                                  },
                                  "DOGE": {
                                      "quote": {
                                          "USD": {
                                              "price": 80
                                          }
                                      }
                                  }
                              }
                          },
                          status_code=200)
        data = retrieve_data.retrieve_data()
        self.assertEqual(data, {"BTC": {"price": 50}, "ETH": {"price": 60}, "SOL": {"price": 70}, "DOGE": {"price": 80}})

    @requests_mock.Mocker()
    def test_retrieve_data_failure(self, mock_requests):
        mock_requests.get(
            "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC%2CETH%2CSOL%2CDOGE&convert=USD&CMC_PRO_API_KEY=4f0a6417-58ab-41f1-8770-6cf42db5d653", status_code=500)
        self.assertRaises(Exception, retrieve_data.retrieve_data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
