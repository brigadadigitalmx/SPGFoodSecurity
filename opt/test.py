import numpy as np
import pandas as pd
from clustering_functions import asigna_entregas


def generate_dataset(n_casas=100, n_centros=2, n_cuadrillas=[15, 15]):
    casas_df = pd.DataFrame({
        'labs_casas': list(range(n_casas)),
        'lon': np.random.rand(n_casas),
        'lat': np.random.rand(n_casas)})

    centros_df = pd.DataFrame({
        'labs_centros': list(range(n_centros)),
        'lon': np.random.rand(n_centros),
        'lat': np.random.rand(n_centros),
        'n': [15, 15]})
    return casas_df, centros_df


if __name__ == '__main__':
    n_casas = 6000
    n_centros = 2
    casas_df, centros_df = generate_dataset(n_casas, n_centros)
    labs_casas, labs_centros, labs_cuadrilla = asigna_entregas(
        casas_df, centros_df)

    df_final = pd.DataFrame({
        'labs_casas': labs_casas,
        'labs_centros': labs_centros,
        'labs_flotilla': labs_cuadrilla
    })
    print(df_final.head())
