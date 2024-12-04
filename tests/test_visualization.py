import pytest
from src.visualisation import bar_plot, scatter_plot, correlation_matrix
import matplotlib.pyplot as plt
import pandas as pd

def test_bar_plot():
    data = [1, 2, 3]
    labels = ['A', 'B', 'C']
    plt.figure()
    bar_plot(data, labels, title="Test Bar Plot")
    assert plt.gcf() is not None

def test_scatter_plot():
    x = [1, 2, 3]
    y = [4, 5, 6]
    plt.figure()
    scatter_plot(x, y, title="Test Scatter Plot")
    assert plt.gcf() is not None

def test_correlation_matrix():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    plt.figure()
    correlation_matrix(data)
    assert plt.gcf() is not None
