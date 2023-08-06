import numpy as np
from sklearn.base import ClassifierMixin

def euclidean_distance(x1,x2):
    ## x1 is n1 x m and x2 is m x n2
    ## return array of shape n1 x n2
    if isinstance(x1,list) and isinstance(x2,list):
        x1, x2 = np.array(x1), np.array(x2)
        return np.sum(np.square(x1-x2))
    x1, x2 = np.array(x1), np.array(x2)
    if x1.shape[1] != x2.shape[1]:
        return "Error : array x1 and x2 should have dimesion same in axis=1"
    n1,m = x1.shape
    n2,m = x2.shape
    x1_square = np.sum(np.square(x1), axis=1).reshape((n1,1))
    x2_square = np.sum(np.square(x2.T), axis=0).reshape((1,n2))
    x1_x2 = np.dot(x1,x2.T)
#    print(x1_x2.shape,x1_square.shape,x2_square.shape)
    return -x1_x2 * 2 + x1_square + x2_square

def cosine_distance(x1,x2):
    ## x1 is n1 x m and x2 is m x n2
    ## return array of shape n1 x n2
    if isinstance(x1,list) and isinstance(x2,list):
        x1, x2 = np.array(x1), np.array(x2)
        return 1 - np.dot(x1,x2.T)/np.sqrt(np.sum(x1**2))/np.sqrt(np.sum(x2**2))
    x1, x2 = np.array(x1), np.array(x2)
    if x1.shape[1] != x2.shape[1]:
        return "Error : array x1 and x2 should have dimesion same in axis=1"
    n1,m = x1.shape
    n2,m = x2.shape
    x1_sqrt = np.sqrt(np.sum(np.square(x1), axis=1).reshape((n1,1)))
    x2_sqrt = np.sqrt(np.sum(np.square(x2.T), axis=0).reshape((1,n2)))
    x1_x2 = np.dot(x1,x2.T)
#    print(x1_x2.shape,x1_square.shape,x2_square.shape)
    return 1 - x1_x2/x1_sqrt/x2_sqrt



class KNearestNeighbors():
    def __init__(self, k=1, distance=euclidean_distance):
        self.k = k
        self.X = None
        self.y = None
        self.n_rows_ = None
        self.dist = distance
    def fit(self,X,y):
        self.X = X
        self.y = y
        self.n_rows_ = X.shape[0]
    def predict(self,X_new):
        n_new = X_new.shape[0]
#        print(X_new.shape,self.X.shape)
        dist_mat = euclidean_distance(X_new,self.X)
        sort_index = np.argsort(dist_mat,axis = 1)
        y_pred = np.zeros((n_new,1))
        for i in xrange(n_new):
            y_pred[i] = np.mean(self.y[sort_index[i,0:self.k]])
        # print("Distant Matrix")
        # print(dist_mat)
        # print(self.y[sort_index[0,0:self.k]])
        # print(np.mean(self.y[sort_index[0,0:self.k]]))
        # print(sort_index.shape)
        # print(y_pred)
        y_pred = (y_pred > 0.5).astype(int)
        return y_pred
    def score(self,X,y_true):
        n = len(y_true)
        y_pred = self.predict(X)
        y_true,y_pred = np.array(y_true).reshape((n,1)),np.array(y_pred).reshape((n,1))
        return float(len(y_true[y_true - y_pred == 0]))/len(y_true)

