import matplotlib.pyplot as plt
import seaborn as sns

def bar_plot(data, labels, title='Bar Plot'):
    """
    Create a bar plot for the given data.

    This function generates a bar plot with the provided data and labels. It also
    allows an optional title to be added to the plot.

    Parameters:
    data (array-like): The data to be plotted on the bars.
    labels (array-like): The labels for the bars.
    title (str, optional, default='Bar Plot'): The title of the plot.

    Returns:
    None
    """
    plt.bar(labels, data)
    plt.title(title)
    plt.show()

def scatter_plot(x, y, title='Scatter Plot'):
    """
    Create a scatter plot for the given data.

    This function generates a scatter plot with the provided x and y values. 
    It also allows an optional title to be added to the plot.

    Parameters:
    x (array-like): The data for the x-axis.
    y (array-like): The data for the y-axis.
    title (str, optional, default='Scatter Plot'): The title of the plot.

    Returns:
    None
    """
    plt.scatter(x, y)
    plt.title(title)
    plt.show()

def correlation_matrix(dataframe):
    """
    Generate a correlation matrix heatmap for the given DataFrame.

    This function computes the correlation matrix for the DataFrame and visualizes 
    it using a heatmap. The correlations are annotated on the heatmap, and a 
    color map is applied to represent the strength of correlations.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame containing the data.

    Returns:
    None
    """
    sns.heatmap(dataframe.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()
