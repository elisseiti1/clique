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

    def fit(self, data):
        self.data = data

    def generate_oneDimensionalUnits(self):
        number_data_points = np.shape(self.data)[0]
        number_features = np.shape(self.data)[1]

        subspaces = np.zeros((self.xi, number_features))

        # project data into each of the clusters
        for feature in range(number_features):
            minVal = min(self.data[:, feature])
            maxVal = max(self.data[:, feature])
            interval = (maxVal - minVal) / self.xi
            for element in self.data[:, feature]:
                index = int((element - minVal) // interval)
                if (element == maxVal):
                    index = self.xi - 1

                subspaces[index, feature] += 1

        print("1D projection:\n", subspaces, "\n")
        is_dense = subspaces > self.tau * number_data_points
        print("is_dense:\n", is_dense)
        one_dim_dense_units = []
        for f in range(number_features):
            for unit in range(self.xi):
                if is_dense[unit, f]:
                    dense_unit = dict()
                    dense_unit[f] = unit
                    one_dim_dense_units.append(dense_unit)
        return one_dim_dense_units

    def run_clique(self):
        # Finding 1 dimensional dense units
        dense_units = self.generate_oneDimensionalUnits()
        number_features = np.shape(self.data)[1]
        # Getting 1 dimensional clusters
        # clusters = self.get_clusters(dense_units, self.data, self.xsi)
        self.get_clusters(dense_units)
        clusters = []
        # Finding dense units and clusters for dimension > 2
        current_dim = 2
        number_of_features = np.shape(self.data)[1]

        while (current_dim <= number_of_features) & (len(dense_units) > 0):
            print("\n", str(current_dim), " dimensional clusters:")
            dense_units = self.get_dense_units_for_dim(dense_units, current_dim)
            for cluster in self.get_clusters(dense_units):
                clusters.append(cluster)
            current_dim += 1

        return clusters

    # def get_clusters(self, dense_units):
    #     graph = build_graph_from_dense_units(dense_units)
    #     number_of_components, component_list = scipy.sparse.csgraph.connected_components(
    #         graph, directed=False)
    #
    #     dense_units = np.array(dense_units)
    #     clusters = []
    #     # For every cluster
    #     for i in range(number_of_components):
    #         # Get dense units of the cluster
    #         cluster_dense_units = dense_units[np.where(component_list == i)]
    #         print("cluster_dense_units: ", cluster_dense_units.tolist())
    #
    #         # Get dimensions of the cluster
    #         dimensions = set()
    #         for u in cluster_dense_units:
    #             dimensions.update(u.keys())
    #
    #         # Get points of the cluster
    #         cluster_data_point_ids = get_cluster_data_point_ids(
    #             data, cluster_dense_units)
    #         # Add cluster to list
    #         clusters.append(Cluster(cluster_dense_units,
    #                                 dimensions, cluster_data_point_ids))

        return clusters

    def get_dense_units_for_dim(data, dense_units, current_dim):
        pass

    def get_clusters(self, dense_units):
        pass
