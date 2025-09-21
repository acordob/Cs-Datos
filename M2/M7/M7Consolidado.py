# EVALUACIÓN FINAL M7: ANÁLISIS DE PREFERENCIAS MUSICALES A NIVEL GLOBAL
# Alumna: Alejandra Córdoba Sepúlveda

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Cargar los datos y exploración de los datos
df = pd.read_csv("dataset_generos_musicales.csv")

# Estadísticas descriptivas
print(df.describe())

# Visualización
sns.pairplot(df.drop(columns='País'))
plt.suptitle("Distribución de géneros musicales por país", y=1.02)
plt.show()

# Algoritmo de Clusterización con K-Means

X = df.drop(columns='País')
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Método del codo y silueta
sse = []
silhouette = []
for k in range(2, 6):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)
    silhouette.append(silhouette_score(X_scaled, kmeans.labels_))

# Visualización
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(range(2,6), sse, marker='o')
plt.title("Método del codo")
plt.xlabel("K")
plt.ylabel("SSE")

plt.subplot(1,2,2)
plt.plot(range(2,6), silhouette, marker='o')
plt.title("Coeficiente de silueta")
plt.xlabel("K")
plt.ylabel("Score")
plt.tight_layout()
plt.show()

# Aplicar K=3
kmeans = KMeans(n_clusters=3, random_state=42)
df['KMeans'] = kmeans.fit_predict(X_scaled)

# Clustering Jerárquico y DBSCAN
linked = linkage(X_scaled, method='ward')
plt.figure(figsize=(10,6))
dendrogram(linked, labels=df['País'].values)
plt.title("Dendrograma")
plt.show()

# Agrupamiento
df['Jerárquico'] = fcluster(linked, 3, criterion='maxclust')

dbscan = DBSCAN(eps=1.5, min_samples=2)
df['DBSCAN'] = dbscan.fit_predict(X_scaled)

# Reducción de Dimensionalidad PCA y t-SNE
pca = PCA(n_components=0.9)
X_pca = pca.fit_transform(X_scaled)
print("Varianza explicada:", pca.explained_variance_ratio_)

# Visualización 2D
pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X_scaled)
sns.scatterplot(x=X_pca_2d[:,0], y=X_pca_2d[:,1], hue=df['KMeans'], palette='Set2', s=100)
plt.title("Clusters en espacio PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

tsne = TSNE(n_components=2, perplexity=5, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)
sns.scatterplot(x=X_tsne[:,0], y=X_tsne[:,1], hue=df['KMeans'], palette='Set2', s=100)
plt.title("Clusters en espacio t-SNE")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.show()