import random


def euc_dist(a, b):
    return sum([(a[i] - b[i]) ** 2 for i in range(len(a))]) ** 0.5


class Kmeans:
    def __init__(self, n_clusters, n_features):
        self.n_clusters = n_clusters
        self.n_features = n_features
        self.clusters = []
        self.centroids = []
        self.old_centroids = []
        self.coef_silhouette = []

    def find_cluster(self, x):
        dist = []
        for centroid in self.centroids:
            dist.append(euc_dist(x, centroid))
        return dist.index(min(dist))

    def initialize_centroids(self, x):
        self.centroids.append(random.choice(x))
        for i in range(self.n_clusters - 1):
            dist = []
            for j in range(len(x)):
                dist.append(euc_dist(x[j], self.centroids[-1]))
            self.centroids.append(x[dist.index(max(dist))])

    def not_same_centroids(self):
        for i in range(self.n_clusters):
            for j in range(self.n_features):
                if self.old_centroids[i][j] != self.centroids[i][j]:
                    return True
        return False

    def compute_silhouette(self):
        coefs = []
        for i in range(self.n_clusters):
            for j in range(len(self.clusters[i])):
                # compute a
                a = sum([euc_dist(self.clusters[i][j], self.clusters[i][k]) for k in range(len(self.clusters[i]))]) / (
                        len(self.clusters[i]) - 1)

                # compute b
                b = min([sum(
                    [euc_dist(self.clusters[i][j], self.clusters[k][kj]) for kj in range(len(self.clusters[k]))]) / len(
                    self.clusters[k]) if k != i else float("inf") for k in range(self.n_clusters)])

                # store result
                coefs.append((b - a) / max([a, b]))

        return sum(coef for coef in coefs) / len(coefs)

    def fit(self, x, epochs=1000):
        self.initialize_centroids(x)
        self.old_centroids = [[0.0 for _ in range(self.n_features)] for _ in range(self.n_clusters)]
        while epochs > 0 and self.not_same_centroids():
            self.clusters = {k: [] for k in range(self.n_clusters)}

            # assign a cluster for an object
            for data in x:
                index = self.find_cluster(data)
                self.clusters[index].append(data)

            # update centroids
            for i in range(self.n_clusters):
                for j in range(self.n_features):
                    self.old_centroids[i][j] = self.centroids[i][j]

            for i in range(self.n_clusters):
                for j in range(self.n_features):
                    mean = 0.0
                    for k in range(len(self.clusters[i])):
                        mean += self.clusters[i][k][j]
                    self.centroids[i][j] = mean / len(self.clusters[i])

            # compute silhouette
            self.coef_silhouette.append(self.compute_silhouette())

            epochs -= 1

    def predict(self, x):
        return [self.find_cluster(x[i]) for i in range(len(x))]
