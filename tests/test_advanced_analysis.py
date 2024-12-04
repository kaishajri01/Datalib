import pytest
import numpy as np
from sklearn.datasets import make_classification, make_blobs
from src.advanced_analysis import (linear_regression, k_means_clustering, 
                                       pca_analysis, decision_tree_classifier)

def test_linear_regression():
    X = np.array([[1], [2], [3]])
    y = np.array([2, 4, 6])
    model = linear_regression(X, y)
    assert np.isclose(model.predict([[4]])[0], 8)

def test_k_means_clustering():
    data, _ = make_blobs(n_samples=100, centers=3, random_state=42)
    model = k_means_clustering(data, n_clusters=3)
    assert len(model.cluster_centers_) == 3

def test_pca_analysis():
    data = np.random.rand(100, 5)
    transformed_data = pca_analysis(data, n_components=2)
    assert transformed_data.shape[1] == 2

def test_decision_tree_classifier():
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    model = decision_tree_classifier(X, y)
    assert model.score(X, y) > 0.9
