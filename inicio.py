import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

modelo_ia = RandomForestRegressor(n_estimators=100)

data = {
    'repeticoes' : [10, 12, 8, 10, 12, 8, 10, 12, 8, 10, 12, 8, 0],
    'carga' : ['leve', 'leve', 'leve', 'moderada', 'moderada', 'moderada', 'pesada', 'pesada', 'pesada', 'leve', 'moderada', 'pesada', 'nenhuma'],
    'amplitude' : [100, 100, 100, 75, 75, 75, 50, 50, 50, 25, 25, 25, 0],
    'eficiencia' : [0.4, 0.5, 0.3, 0.7, 0.8, 0.6, 1, 1, 0.9, 0.4, 0.8, 0.9, 0]
}

dt = pd.DataFrame(data)

le_carga = LabelEncoder()
dt['carga'] = le_carga.fit_transform(dt['carga'])

x = dt[['repeticoes', 'carga', 'amplitude']]
y = dt['eficiencia']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
modelo_ia = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_ia.fit(x_train, y_train)

