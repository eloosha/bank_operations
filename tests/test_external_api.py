from unittest.mock import MagicMock, patch

from src.external_api import get_amount_rub


def test_get_amount_rub_rub():
    transaction = {"amount": 100, "currency": "RUB"}
    assert get_amount_rub(transaction) == 100


@patch("src.external_api.requests.get")
def test_get_amount_rub_usd(mock_get):
    transaction = {"amount": 10, "currency": "USD"}

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 100}}
    mock_get.return_value = mock_response

    result = get_amount_rub(transaction)
    assert result == 10 * 100
