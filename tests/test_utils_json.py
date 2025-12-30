import json
from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_get_operations_valid_json():
    sample_data = [{"amount": 100, "currency": "RUB"}]
    m = mock_open(read_data=json.dumps(sample_data))
    with patch("builtins.open", m):
        result = read_json_file("dummy_path.json")
        assert result == sample_data


def test_get_operations_file_not_found():
    result = read_json_file("nonexistent.json")
    assert result == []


def test_get_operations_invalid_json():
    m = mock_open(read_data="not json")
    with patch("builtins.open", m):
        result = read_json_file("dummy.json")
        assert result == []
