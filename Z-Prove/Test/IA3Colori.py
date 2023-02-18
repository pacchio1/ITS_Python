import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

# chiedi all'utente di inserire il percorso dell'immagine
path = input("Inserisci il percorso dell'immagine: ")

# carica l'immagine
img = Image.open(path)

# converti l'immagine in un array NumPy
img_data = np.array(img)

# ridimensiona l'array in un array bidimensionale
img_data = img_data.reshape((img_data.shape[0] * img_data.shape[1], 3))

# usa K-means per identificare i 3 cluster principali nel dataset di pixel
kmeans = KMeans(n_clusters=3)
kmeans.fit(img_data)

# ottieni i centroidi dei 3 cluster principali identificati da K-means
colors = kmeans.cluster_centers_

# converti i valori dei centroidi dei cluster in interi compresi tra 0 e 255
colors = colors.astype(int)

# visualizza l'immagine e i 3 colori principali identificati
# plt.imshow(img)
# plt.show()
plt.imshow([colors])
plt.show()
