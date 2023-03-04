from dtw_sofar import dtw_cost, get_initial_matrices
from unittest.mock import patch
import numpy as np


def test_dtwcost():
    features_a = np.random.rand(10)
    features_b = features_a
    cost = dtw_cost(features_a, features_b)
    assert np.isclose(0, cost)


def test_get_initial_matrices_backpointers():
    frame_features = np.random.rand(10)
    text_features = np.random.rand(5)
    cost_matrix, backpointers = get_initial_matrices(frame_features, text_features)
    backpointers_expected = np.zeros((frame_features.shape[0], text_features.shape[0]))
    assert np.array_equal(backpointers, backpointers_expected)


def test_get_initial_matrices_costmatrix():
    frame_features = np.random.rand(20)
    text_features = np.random.rand(10)
    cost_matrix, backpointers = get_initial_matrices(frame_features, text_features)
    n = frame_features.shape[0]
    m = text_features.shape[0]

    cost_matrix_expected = np.zeros((n + 1, m + 1))
    for i in range(1, n + 1):
        cost_matrix_expected[i, 0] = np.inf
    for i in range(1, m + 1):
        cost_matrix_expected[0, i] = np.inf
    assert np.array_equal(cost_matrix_expected, cost_matrix)


def test_dtw():
    assert True


def test_dtw_onthefly_classification():
    assert True


def test_dtw_sofar():
    frame_features = np.random.rand(10)
    text_features = np.random.rand(5)
    assert True


# sanity check
def test_always_passes():
    assert True
