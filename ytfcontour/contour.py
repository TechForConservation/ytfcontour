import numpy as np

VERTEX_DTYPE = [('position', '2f4'), ('segment', 'i4')]
SEGMENT_DTYPE = [('v0', 'i4'), ('v1', 'i4'), ('next', 'i4'), ('prev', 'i4')]

class Contour():
    def __init__(self, lines, **kwargs):
        self._vertices = None
        self._segments = None
        self._centroid = None
        self._bbox = None
        self._lines = None
                
        self._initialize_contour(lines)
        
        # Set non-default values
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    def _initialize_contour(self, lines):
        # Get the unique vertices
        lines_sorted = lines.reshape(2*lines.shape[0],2)
        v, inv = np.unique(lines_sorted,axis=0,return_inverse=True)
        self._vertices = np.zeros(v.shape[0],dtype=VERTEX_DTYPE)
        self._vertices['position'] = v
        self._vertices['segment'] = np.arange(v.shape[0])
        
        # Set up the line segments
        self._segments=np.zeros(v.shape[0],dtype=SEGMENT_DTYPE)
        self._segments['v0'] = inv[::2]
        self._segments['v1'] = inv[1::2]
        
        # Get line segment ordering
        n, p = np.where(self._segments['v0'][:,None] == self._segments['v1'][None,:])
        self._segments['next'][p] = n
        self._segments['prev'][n] = p

    @property
    def bbox(self):
        if self._bbox is None:
            self._bbox = [np.min(self.vertices[:,0]), np.max(self.vertices[:,0]), np.min(self.vertices[:,1]), np.max(self.vertices[:,1])]
        return self._bbox
    
    @property
    def centroid(self):
        if self._centroid is None:
            self._centroid = [np.mean(self.vertices[:,0]), np.mean(self.vertices[:,1])]
        return self._centroid
    
    @property
    def lines(self):
        if self._lines is None:
            self._lines = self._vertices['position'][np.array([self._segments['v0'],self._segments['v1']])].swapaxes(0,1)
        return self._lines
    
    @property
    def vertices(self):
        return self._vertices['position']
    
    @property
    def perimeter(self):
        return np.sqrt((self.lines[:,0]-self.lines[:,1])**2).sum()
    