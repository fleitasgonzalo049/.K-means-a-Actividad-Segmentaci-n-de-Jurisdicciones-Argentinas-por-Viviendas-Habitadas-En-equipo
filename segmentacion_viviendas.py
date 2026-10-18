import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Configuración de estilo visual
sns.set_theme(style="whitegrid")

# 1. Carga de Datos (INDEC Censo 2022)
datos = {
    'Jurisdicción': [
        'Ciudad Autónoma de Buenos Aires', 'Buenos Aires', 'Catamarca', 'Chaco',
        'Chubut', 'Córdoba', 'Corrientes', 'Entre Ríos', 'Formosa', 'Jujuy',
        'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 'Neuquén', 'Río Negro',
        'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe',
        'Santiago del Estero', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur',
        'Tucumán'
    ],
    'Viviendas Habitadas': [
        1391258, 5970702, 131978, 368728, 213317, 1378237, 370958, 494473,
        194689, 238141, 140879, 124149, 639467, 420101, 254545, 276371,
        404504, 241436, 182886, 118047, 1273460, 311361, 65535, 493794
    ]
}

df = pd.DataFrame(datos)

# 2. Aplicar K-Means con 3 clusters
N_CLUSTERS = 3
kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=10)
df['Cluster_ID'] = kmeans.fit_predict(df[['Viviendas Habitadas']])

# 3. Asignación de Etiquetas Interpretables
centroides = kmeans.cluster_centers_.flatten()
indices_ordenados = np.argsort(centroides)

mapeo_etiquetas = {
    indices_ordenados[0]: 'Pocas viviendas',
    indices_ordenados[1]: 'Cantidad normal de viviendas',
    indices_ordenados[2]: 'Muchas viviendas'
}

df['Categoria'] = df['Cluster_ID'].map(mapeo_etiquetas)

# 4. Mostrar resultados en consola
df_ordenado = df.sort_values(by='Viviendas Habitadas', ascending=False).reset_index(drop=True)
print("--- CLASIFICACIÓN DE JURISDICCIONES ---")
print(df_ordenado[['Jurisdicción', 'Viviendas Habitadas', 'Categoria']].to_string())

# 5. Visualización gráfica
plt.figure(figsize=(12, 7))
colores = {'Muchas viviendas': '#e74c3c', 'Cantidad normal de viviendas': '#f39c12', 'Pocas viviendas': '#3498db'}

sns.scatterplot(
    data=df,
    x='Viviendas Habitadas',
    y='Jurisdicción',
    hue='Categoria',
    palette=colores,
    s=130,
    style='Categoria',
    markers={'Muchas viviendas': 's', 'Cantidad normal de viviendas': 'D', 'Pocas viviendas': 'o'}
)

for idx in indices_ordenados:
    plt.axvline(x=centroides[idx], color=colores[mapeo_etiquetas[idx]], linestyle='--', alpha=0.6)

plt.title('Segmentación K-Means (K=3): Viviendas Habitadas por Jurisdicción (Censo 2022)', fontsize=13, fontweight='bold')
plt.xlabel('Cantidad de Viviendas Habitadas', fontsize=11)
plt.ylabel('Jurisdicción', fontsize=11)
plt.ticklabel_format(style='plain', axis='x')
plt.legend(title='Segmentos', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
