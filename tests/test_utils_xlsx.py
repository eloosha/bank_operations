import pandas as pd

from src.utils import read_excel_file


def test_get_operations_valid_excel(tmp_path):
    df = pd.DataFrame([{"amount": 300, "currency": "EUR"}])
    file_path = tmp_path / "transactions.xlsx"
    df.to_excel(file_path, index=False)

    result = read_excel_file(str(file_path))

    assert result == [{"amount": 300, "currency": "EUR"}]
