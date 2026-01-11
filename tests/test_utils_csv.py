from src.utils import read_csv_file


def test_get_operations_valid_csv(tmp_path):
    csv_content = "amount,currency\n100,RUB\n200,USD"
    file_path = tmp_path / "transactions.csv"
    file_path.write_text(csv_content, encoding="utf-8")

    result = read_csv_file(str(file_path))

    assert isinstance(result, list)
    assert result[0]["amount"] == 100
    assert result[1]["currency"] == "USD"
