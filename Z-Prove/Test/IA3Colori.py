# librerie
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image
# Caricare l'immagine
img = Image.open('path/to/image')
# Convertire l'immagine in un array NumPy
img_data = np.array(img)
# Reshape dell'array in un array bidimensionale
img_data = img_data.reshape((img_data.shape[0] * img_data.shape[1], 3))
# Usare K-means per identificare i 3 cluster principali nel dataset di pixel.
# K-means è un algoritmo di clustering non supervisionato che può essere utilizzato per raggruppare i dati in cluster basati sulla loro somiglianza.
# In questo caso, stiamo cercando di identificare i cluster principali di pixel nell'immagine.
kmeans = KMeans(n_clusters=3)
kmeans.fit(img_data)
# Ottenere i centroidi dei 3 cluster principali identificati da K-means.
# I centroidi sono i punti medi di ogni cluster e rappresentano il colore principale di ogni cluster.
colors = kmeans.cluster_centers_
# Convertire i valori dei centroidi dei cluster in interi compresi tra 0 e 255 per poterli visualizzare come colori.
colors = colors.astype(int)
# Visualizzare l'immagine e i 3 colori principali identificati usando la libreria matplotlib
plt.imshow(img)
plt.show()
plt.imshow([colors])
plt.show()
