import numpy as np
def test_contour_ordered():
    from ytfcontour.contour import Contour

    square_lines = np.array([[[0,0],[0,1]],[[0,1],[1,1]],[[1,1],[1,0]],[[1,0],[0,0]]])
    c_square = Contour(square_lines)
    print(c_square._segments['next'], c_square._segments['prev'], c_square._vertices['segment'])
    n = np.all(c_square._segments['next'] == np.array([1,2,3,0]))
    p = np.all(c_square._segments['prev'] == np.array([3,0,1,2]))
    s = np.all(c_square._vertices['segment'] == np.arange(4))
    assert(n&p&s)

def test_contour_unordered():
    from ytfcontour.contour import Contour

    square_lines = np.array([[[0,0],[0,1]],[[1,1],[1,0]],[[0,1],[1,1]],[[1,0],[0,0]]])
    c_square = Contour(square_lines)
    n = np.all(c_square._segments['next'] == np.array([2,3,1,0]))
    p = np.all(c_square._segments['prev'] == np.array([3,2,0,1]))
    s = np.all(c_square._vertices['segment'] == np.arange(4))
    assert(n&p&s)
    
def test_contour_flipped():
    from ytfcontour.contour import Contour

    square_lines = np.array([[[0,0],[0,1]],[[1,1],[0,1]],[[1,1],[1,0]],[[1,0],[0,0]]])
    c_square = Contour(square_lines)
    n = np.all(c_square._segments['next'] == np.array([1,2,3,0]))
    p = np.all(c_square._segments['prev'] == np.array([3,0,1,2]))
    s = np.all(c_square._vertices['segment'] == np.arange(4))
#     print(c_square._segments['next'],np.array([1,2,3,0]))
#     print(c_square._segments['prev'],np.array([3,0,1,2]))
    assert(n&p&s)
