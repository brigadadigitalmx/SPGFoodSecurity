import pandas as pd
import numpy as np
from sklearn.cluster import KMeans as km


def array_to_single_df(array_of_dfs):
    # INPUT
    # array of dfs
    # Transforms it into single df
    # OUTPUT
    # df
    df = pd.concat(array_of_dfs, axis=0)
    return df


def crea_rutas(X, labs_cuadrilla):
    # INPUT
    # X - df con la información de las entregas
    # labs_cuadrilla - Cuantos cuadrilla por centro hay
    #                  como columna del dataframe
    # OUTPUT
    # labs_rutas
    # df que entrega las casas que le corresponden a cada camión
    dataframes_by_zone = []
    for x in X.labs_centros.unique():
        new_df = X[X.labs_centros == x]
        cuadrilla = new_df.labs_cuadrilla
        new_df = new_df.loc[:, new_df.columns != labs_cuadrilla]
        kmeans = km(n_clusters=cuadrilla.iloc[0])
        kmeans.fit(new_df)
        new_df['labs_ruta'] = kmeans.labels_
        dataframes_by_zone.append(new_df)
    final_df = array_to_single_df(dataframes_by_zone)
    return final_df


if __name__ == '__main__':
    df_input = pd.DataFrame({
        'labs_casas': [np.random.randint(5, 20) for x in range(0, 1000)],
        'labs_centros': [np.random.randint(5, 20) for x in range(0, 1000)],
        'labs_cuadrilla': [np.random.randint(5, 20) for x in range(0, 1000)],
    })
    df_output = crea_rutas(df_input, 'labs_cuadrilla')
    print(df_output)
