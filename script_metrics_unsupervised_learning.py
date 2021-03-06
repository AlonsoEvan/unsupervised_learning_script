from sklearn import metrics
from sklearn import datasets
import pandas as pd

from sklearn.cluster import KMeans, AgglomerativeClustering, AffinityPropagation, SpectralClustering

df = datasets.load_digits()

X, y = df.data, df.target

algorithms = []

algorithms.append(KMeans(n_clusters = 10, random_state = 0))
algorithms.append(AffinityPropagation())
algorithms.append(SpectralClustering(n_clusters=10, random_state=1,
                                     affinity='nearest_neighbors'))
algorithms.append(AgglomerativeClustering(n_clusters = 10))

data = []

for algo in algorithms:
	algo.fit(X)
	data.append(({
		'ARI' : metrics.adjusted_rand_score(y, algo.labels_),
		'AMI' : metrics.adjusted_mutual_info_score(y, algo.labels_, average_method = 'arithmetic'),
		'Homogenity' : metrics.homogeneity_score(y, algo.labels_),
		'Completeness' : metrics.completeness_score(y, algo.labels_),
		'V_measure' : metrics.v_measure_score(y, algo.labels_),
		'Silhouette' : metrics.silhouette_score(X, algo.labels_)}))


results = pd.DataFrame(data = data, columns = ['ARI', 'AMI', 'Homogenity',
											'Completeness', 'V_measure', 'Silhouette'],
											index = ['K-means', 'affinity', 'Spectral', 'Agglomerative'])

print(results)



