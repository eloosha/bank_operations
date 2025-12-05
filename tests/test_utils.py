import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import get_operations


def test_get_operations_valid():
    sample_data = [{"amount": 100, "currency": "RUB"}]
    m = mock_open(read_data=json.dumps(sample_data))
    with patch("builtins.open", m):
        result = get_operations("dummy_path.json")
        assert result == sample_data


def test_get_operations_file_not_found():
    result = get_operations("nonexistent.json")
    assert result == []


def test_get_operations_invalid_json():
    m = mock_open(read_data="not json")
    with patch("builtins.open", m):
        result = get_operations("dummy.json")
        assert result == []
