import numpy as np


class Clique:

    # xi is the partition input parameter
    xi: int = 1

    # tau is the density threshold value
    tau: int = 0.2

    # pruning value
    isPruning: bool = False

    # data is the dataset input
    data = []

    def __init__(self, xi, tau, pruning):
        self.xi = xi
        self.tau = tau
        self.isPruning = pruning

    def generate_oneDimensionalUnits(self, data, xsi, tau):
        number_data_points = np.shape(data)[0]
        number_features = np.shape(data)[1]

        subspaces = np.zeros(xsi, number_features)

        # project nr
        for feature in range(number_features):
            minVal = min(data[:, feature])
            maxVal = max(data[:, feature])
            interval = (maxVal - minVal)/xsi
            for element in data[:, feature]:
                index = (element - minVal)//interval
                subspaces[index, feature] += 1

        # print("1D projection:\n", subspaces, "\n")
        is_dense = subspaces > tau * number_data_points
        # print("is_dense:\n", is_dense)
        one_dim_dense_units = []
        for f in range(number_features):
            for unit in range(xsi):
                if is_dense[unit, f]:
                    dense_unit = dict({f: unit})
                    one_dim_dense_units.append(dense_unit)
        return one_dim_dense_units

