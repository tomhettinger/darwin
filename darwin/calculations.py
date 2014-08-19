import numpy as np
from numba import double, int64, jit

def image_difference(image1, image2):
    """For each pixel, determine the distance between colors in RGB-space.
    sqrt(dR^2 + dG^2 + dB^2) with respect to another image."""
    X1, Y1, B1 = image1.shape
    X2, Y2, B2 = image2.shape

    assert X1 == X2
    assert Y1 == Y2
    assert B1 == B2

    result = np.zeros((X1, Y1))
    
    for x in range(X1):
        for y in range(Y1):
            squareDiffs = 0.0
            for b in range(B1):
                squareDiffs += (image1[x][y][b] - image2[x][y][b])**2
            result[x][y] = np.sqrt(squareDiffs)

    return result


fast_image_difference = jit(double[:,:](int64[:,:,:], int64[:,:,:]))(image_difference)