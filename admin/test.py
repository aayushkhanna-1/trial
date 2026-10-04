import numpy as np

def test_numpy_array_creation():
    # Create a numpy array
    arr = np.array([1, 2, 3, 4, 5])
    
    # Check if the array is created correctly
    assert isinstance(arr, np.ndarray), "The object is not a numpy array"
    assert arr.shape == (5,), "The shape of the array is incorrect"
    assert np.array_equal(arr, np.array([1, 2, 3, 4, 5])), "The contents of the array are incorrect"