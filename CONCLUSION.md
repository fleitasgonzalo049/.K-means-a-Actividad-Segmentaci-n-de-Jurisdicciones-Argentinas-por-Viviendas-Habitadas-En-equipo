# Conclusiones del Trabajo Práctico: Clustering con K-Means

**Integrantes del grupo:**
- Demey, Gustavo
- Fleitas, Gonzalo

---

## 1. Análisis de los Resultados Obtenidos
Al aplicar el algoritmo de **K-Means con $K=3$** sobre el conjunto de datos de viviendas habitadas por jurisdicción (Censo 2022 del INDEC), obtuvimos una distribución de los datos muy marcada:

* **Segmento "Muchas viviendas" (1 jurisdicción):** Provincia de Buenos Aires.
* **Segmento "Cantidad normal de viviendas" (3 jurisdicciones):** CABA, Córdoba y Santa Fe.
* **Segmento "Pocas viviendas" (20 jurisdicciones):** El resto de las provincias del país (desde Mendoza hasta Tierra del Fuego).

---

## 2. ¿Por qué el algoritmo agrupó los datos de esta manera?

1. **El efecto de la Provincia de Buenos Aires (Outlier):**  
   Buenos Aires cuenta con casi 6 millones de viviendas habitadas, una cifra muy alejada del resto del país. Como K-Means busca minimizar las distancias al centroide más cercano, terminó reservando un grupo completo casi de forma exclusiva para esta provincia. Si la hubiera mezclado con CABA o Córdoba, el error cuadrático del grupo habría sido gigantesco.

2. **El bloque urbano intermedio:**  
   CABA, Córdoba y Santa Fe forman un grupo homogéneo de entre 1.27 y 1.39 millones de viviendas. El modelo identificó de forma natural este "escalón intermedio" de jurisdicciones altamente pobladas y las agrupó bajo la etiqueta de **"Cantidad normal de viviendas"**.

3. **La concentración del resto del país:**  
   Al haber tanta diferencia entre Buenos Aires y las provincias más chicas, las 20 jurisdicciones restantes (que van desde las 65 mil hasta las 630 mil viviendas) quedaron agrupadas en el segmento de **"Pocas viviendas"**. Para el algoritmo, la distancia entre Mendoza (639k) y Tierra del Fuego (65k) es mucho menor que la distancia de cualquiera de ellas con Buenos Aires.

---

## 3. Reflexión Final y Aprendizajes

Este ejercicio nos sirvió para entender cómo trabaja K-Means frente a datos reales con una **distribución asimétrica**:

* **Lo positivo:** El modelo es muy rápido y logra separar claramente los polos demográficos más importantes del país sin intervención humana.
* **Aspectos a considerar:** En variables con tanta disparidad como la población o viviendas por provincia, definir $K=3$ hace que la mayoría de los casos caigan en un mismo grupo amplio.
* **Sugerencia de mejora:** Para futuros trabajos, sería interesante trabajar con variables estandarizadas o combinadas (por ejemplo, viviendas habitadas en relación a la superficie o densidad poblacional) para lograr agrupamientos más balanceados entre las provincias.
