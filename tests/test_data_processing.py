import pytest
import pandas as pd
from src.data_processing import load_csv, save_csv, normalize_data, handle_missing_values

def test_load_csv():
    df = load_csv('tests/test_data.csv')
    assert not df.empty
    assert isinstance(df, pd.DataFrame)

def test_save_csv(tmp_path):
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    file_path = tmp_path / "output.csv"
    save_csv(df, file_path)
    loaded_df = load_csv(file_path)
    pd.testing.assert_frame_equal(df, loaded_df)

def test_normalize_data():
    data = pd.DataFrame({'A': [1, 2, 3]})
    result = normalize_data(data, ['A'])
    assert result['A'].max() == 1
    assert result['A'].min() == 0

def test_handle_missing_values():
    data = pd.DataFrame({'A': [1, None, 3]})
    filled_data = handle_missing_values(data, strategy='mean')
    assert filled_data['A'].isnull().sum() == 0
    assert filled_data['A'].iloc[1] == 2  # mean of 1 and 3
