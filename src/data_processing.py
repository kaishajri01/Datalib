import pandas as pd
import numpy as np

def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.

    This function uses pandas to read the CSV file located at the given 
    file path and returns the data as a DataFrame.

    Parameters:
    file_path (str): The file path to the CSV file.

    Returns:
    pandas.DataFrame: The DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(file_path)

def save_csv(dataframe, file_path):
    """
    Save a pandas DataFrame to a CSV file.

    This function writes the provided DataFrame to a CSV file at the specified
    file path. The index of the DataFrame will not be included in the output file.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame to save.
    file_path (str): The file path where the DataFrame should be saved.
    """
    dataframe.to_csv(file_path, index=False)

def normalize_data(dataframe, columns):
    """
    Normalize the specified columns in the DataFrame.

    This function normalizes the specified columns in the given DataFrame
    by applying Min-Max normalization. The formula used is:
    normalized_value = (value - min) / (max - min)

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame containing the data to normalize.
    columns (list of str): The list of column names to normalize.

    Returns:
    pandas.DataFrame: The DataFrame with normalized columns.
    """
    for col in columns:
        dataframe[col] = (dataframe[col] - dataframe[col].min()) / (dataframe[col].max() - dataframe[col].min())
    return dataframe

def handle_missing_values(dataframe, strategy='mean'):
    """
    Handle missing values in the DataFrame.

    This function fills missing values in the DataFrame using the specified 
    strategy ('mean' or 'median'). If an unsupported strategy is provided,
    a ValueError is raised.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame to handle missing values in.
    strategy (str, optional, default='mean'): The strategy to use for filling 
                                              missing values. Can be 'mean' or 'median'.

    Returns:
    pandas.DataFrame: The DataFrame with missing values filled.
    
    Raises:
    ValueError: If an unsupported strategy is provided.
    """
    if strategy == 'mean':
        return dataframe.fillna(dataframe.mean())
    elif strategy == 'median':
        return dataframe.fillna(dataframe.median())
    else:
        raise ValueError("Unsupported strategy. Use 'mean' or 'median'.")
