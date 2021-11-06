import numpy


class Clique:

    # xi is the partition input parameter
    xi: int = 1

    # tau is the density threshold value
    tau: int = 0.2

    # pruning value
    isPruning: bool = False

    # data is the dataset input
    data = numpy.array([])

    def __init__(self, xi, tau, pruning):
        self.xi = xi
        self.tau = tau
        self.isPruning = pruning

    def generateClusters(self):
        return []
