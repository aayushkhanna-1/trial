import numpy as np

def test_numpy_array_creation():
    # Create a numpy array
    arr = np.array([1, 2, 3, 4, 5])
    
    # Check if the array is created correctly
    assert isinstance(arr, np.ndarray), "The object is not a numpy array"
    assert arr.shape == (5,), "The shape of the array is incorrect"
    assert np.array_equal(arr, np.array([1, 2, 3, 4, 5])), "The contents of the array are incorrect"


def test_numpy_array_operations():
    # Create two numpy arrays
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    
    # Perform addition
    result_add = arr1 + arr2
    assert np.array_equal(result_add, np.array([5, 7, 9])), "Addition operation failed"
    
    # Perform multiplication
    result_mul = arr1 * arr2
    assert np.array_equal(result_mul, np.array([4, 10, 18])), "Multiplication operation failed"