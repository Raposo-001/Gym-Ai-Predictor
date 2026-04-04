import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

# Criando o "cérebro"
modelo_ia = RandomForestRegressor(n_estimators=100)