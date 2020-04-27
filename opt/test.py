import numpy as np
import pandas as pd
import requests


def generate_dataset(n_casas=100, n_centros=2, n_cuadrillas=[15, 15]):
    casas_df = pd.DataFrame({
        'labs_casas': list(range(n_casas)),
        'lon': np.random.rand(n_casas),
        'lat': np.random.rand(n_casas)})

    centros_df = pd.DataFrame({
        'labs_centros': list(range(n_centros)),
        'lon': np.random.rand(n_centros),
        'lat': np.random.rand(n_centros),
        'n': n_cuadrillas})
    return casas_df, centros_df


if __name__ == '__main__':
    n_casas = 600
    n_centros = 2
    n_cuadrillas = [15, 15]
    casas_df, centros_df = generate_dataset(n_casas, n_centros, n_cuadrillas)
    r = requests.post('http://0.0.0.0:5000/get_best_routes',
                      json={
                          'hogares': casas_df.to_dict(orient='records'),
                          'centros': centros_df.to_dict(orient='records')
                      })
    print(pd.DataFrame(r.json()))
