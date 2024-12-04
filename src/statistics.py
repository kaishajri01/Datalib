import numpy as np
from scipy import stats

def calculate_mean(data):
    """
    Calculate the mean (average) of a dataset.

    This function computes the arithmetic mean of the given data.

    Parameters:
    data (array-like): The dataset for which the mean is calculated.

    Returns:
    float: The mean of the data.
    """
    return np.mean(data)

def calculate_median(data):
    """
    Calculate the median of a dataset.

    This function computes the middle value of the dataset. If the dataset 
    has an even number of elements, the median is the average of the two middle values.

    Parameters:
    data (array-like): The dataset for which the median is calculated.

    Returns:
    float: The median of the data.
    """
    return np.median(data)

def calculate_mode(data):
    """
    Calculate the mode of a dataset.

    This function returns the most frequent value(s) in the dataset. If there are
    multiple modes, only the first one is returned.

    Parameters:
    data (array-like): The dataset for which the mode is calculated.

    Returns:
    float: The mode of the data.
    """
    return stats.mode(data).mode[0]

def calculate_std(data):
    """
    Calculate the standard deviation of a dataset.

    This function computes the standard deviation, which measures the spread of 
    values around the mean in the dataset.

    Parameters:
    data (array-like): The dataset for which the standard deviation is calculated.

    Returns:
    float: The standard deviation of the data.
    """
    return np.std(data)

def correlation(data1, data2):
    """
    Calculate the correlation coefficient between two datasets.

    This function computes the Pearson correlation coefficient, which measures 
    the linear relationship between two datasets. The coefficient ranges from 
    -1 (perfect negative correlation) to 1 (perfect positive correlation).

    Parameters:
    data1 (array-like): The first dataset.
    data2 (array-like): The second dataset.

    Returns:
    float: The correlation coefficient between data1 and data2.
    """
    return np.corrcoef(data1, data2)[0, 1]

def t_test(data1, data2):
    """
    Perform a t-test to compare the means of two datasets.

    This function tests whether the means of two independent datasets are 
    significantly different from each other. It returns the t-statistic and 
    the p-value.

    Parameters:
    data1 (array-like): The first dataset.
    data2 (array-like): The second dataset.

    Returns:
    tuple: A tuple containing the t-statistic and the p-value.
    """
    return stats.ttest_ind(data1, data2)

def chi_square_test(observed, expected):
    """
    Perform a Chi-Square test to compare observed and expected frequencies.

    This function tests whether there is a significant difference between the 
    observed and expected frequencies in categorical data.

    Parameters:
    observed (array-like): The observed frequencies.
    expected (array-like): The expected frequencies.

    Returns:
    tuple: A tuple containing the Chi-Square statistic and the p-value.
    """
    return stats.chisquare(observed, f_exp=expected)
