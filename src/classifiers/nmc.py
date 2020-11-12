import numpy as np
from sklearn.metrics.pairwise import euclidean_distances


class NMC(object):
    """
    Class implementing the Nearest Mean Centroid (NMC) classifier.
    This classifier estimates one centroid per class from the training data,
    and predicts the label of a never-before-seen (test) point based on its
    closest centroid.
    Attributes
    -----------------
    - centroids: read-only attribute containing the centroid values estimated
        after training
    Methods
    -----------------
    - fit(x,y) estimates centroids from the training data
    - predict(x) predicts the class labels on testing points
    """

    def __init__(self):
        self._centroids = None
        self._class_labels = None  # class labels may not be contiguous indices

    @property
    def centroids(self):
        return self._centroids

    @property
    def class_labels(self):
        return self._class_labels

    def fit(self, xtr, ytr):
        pass

<<<<<<< HEAD
    def predict(self, xts):
        pass
=======
        dist_euclidean = euclidean_distances(Xts, self._centroids)
        idx_min = np.argmin(dist_euclidean, axis=1)
        yc = self._class_labels[idx_min]
        return yc
>>>>>>> main
