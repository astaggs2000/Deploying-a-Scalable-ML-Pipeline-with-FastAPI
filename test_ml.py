import pytest
# TODO: add necessary import
import numpy as np
from ml.model import train_model
from ml.model import inference
from ml.model import compute_model_metrics


# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Tests whether the model trains successfully.
    """
    # Your code here
    X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y_train = np.array([0, 0, 1, 1])
    model = train_model(X_train, y_train)
    assert hasattr(model, "estimators_")


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Tests whether the model returns the expected number of predictions.
    """
    # Your code here
    X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y_train = np.array([0, 0, 1, 1])
    model = train_model(X_train, y_train)
    preds = inference(model, X_train)
    assert len(preds) == len(X_train)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Tests whether precision, recall, and F1 score are calculated correctly.
    """
    # Your code here
    y = np.array([0, 0, 1, 1])
    preds = np.array([0, 1, 1, 1])
    precision, recall, f1 = compute_model_metrics(y, preds)
    assert precision == pytest.approx(2 / 3)
    assert recall == pytest.approx(1.0)
    assert f1 == pytest.approx(0.8)
