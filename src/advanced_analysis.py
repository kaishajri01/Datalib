from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier

def linear_regression(X, y):
    """
    Perform Linear Regression on the given dataset.

    This function uses the LinearRegression model from sklearn to fit 
    a linear regression model to the provided input data (X) and target 
    values (y).

    Parameters:
    X (array-like, shape (n_samples, n_features)): The input data for the model.
    y (array-like, shape (n_samples,)): The target values.

    Returns:
    model (LinearRegression object): The trained Linear Regression model.
    """
    model = LinearRegression()
    model.fit(X, y)
    return model

def k_means_clustering(data, n_clusters=3):
    """
    Perform K-Means Clustering on the given dataset.

    This function applies the KMeans clustering algorithm from sklearn to
    the provided data and returns the fitted model. By default, it uses 
    3 clusters, but this can be adjusted using the n_clusters parameter.

    Parameters:
    data (array-like, shape (n_samples, n_features)): The input data to cluster.
    n_clusters (int, optional, default=3): The number of clusters to form.

    Returns:
    model (KMeans object): The trained KMeans clustering model.
    """
    model = KMeans(n_clusters=n_clusters)
    model.fit(data)
    return model

def pca_analysis(data, n_components=2):
    """
    Perform Principal Component Analysis (PCA) on the given dataset.

    This function uses PCA from sklearn to reduce the dimensionality of the
    provided data to the specified number of components.

    Parameters:
    data (array-like, shape (n_samples, n_features)): The input data for PCA.
    n_components (int, optional, default=2): The number of principal components 
                                              to keep.

    Returns:
    transformed_data (array-like, shape (n_samples, n_components)): 
        The data projected onto the selected principal components.
    """
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data)

def decision_tree_classifier(X, y):
    """
    Train a Decision Tree Classifier on the given dataset.

    This function uses the DecisionTreeClassifier from sklearn to train a 
    decision tree model based on the provided input data (X) and target 
    values (y).

    Parameters:
    X (array-like, shape (n_samples, n_features)): The input data for training.
    y (array-like, shape (n_samples,)): The target labels.

    Returns:
    model (DecisionTreeClassifier object): The trained Decision Tree Classifier.
    """
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model
