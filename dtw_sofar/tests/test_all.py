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


def test_dtw():
    assert True

def test_dtw_onthefly_classification():
    assert True

def test_dtw_sofar():
    assert True

# sanity check
def test_always_passes():
    assert True