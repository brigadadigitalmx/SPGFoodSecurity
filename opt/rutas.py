import pandas as pd
import numpy as np
from math import cos, asin, sqrt, pi


def orden(puntos, centro_x, centro_y):
    p = pi/180
    dists = []
    for x in range(0, len(puntos)):
        a = 0.5 - cos((centro_x-puntos.lat.iloc[x])*p)/2 +\
                cos(puntos.lat.iloc[x]*p) * cos(centro_x*p) *\
                (1-cos((centro_y-puntos.lon.iloc[x])*p))/2
        a = 12742 * asin(sqrt(a))
        dists.append(a)
    puntos['labs_ruta'] = dists
    puntos = puntos.sort_values('labs_ruta')
    return puntos


def crea_rutas(casas_df, df_final, centros_df):
    # INPUT
    # df_casas - df con las coordenadas de las casas
    # df_final -  df con los clusters generados
    # centros_df - df con las ubicaciones de los centros
    # OUTPUT
    # labs_rutas
    # df que entrega el orden a repartir por casas
    df_rutas = casas_df.join(df_final, on='ReporteId', lsuffix='_ll')
    df_rutas = df_rutas.drop('ReporteId_ll', axis=1)
    df_rutas = df_rutas.join(centros_df, on='labs_centros', rsuffix='_centros')
    df_rutas = df_rutas.drop('labs_centros_centros', axis=1)
    dataframes_ordered = []
    for x in df_rutas.labs_cuadrilla.unique():
        new_df = df_rutas[df_rutas.labs_cuadrilla == x]
        centro_x = new_df.lat_centros.iloc[0]
        centro_y = new_df.lon_centros.iloc[0]
        puntos = new_df[['ReporteId', 'labs_centros', 'labs_cuadrilla', 'lat', 'lon']]
        puntos_ordenados = orden(puntos, centro_x, centro_y)
        dataframes_ordered.append(puntos_ordenados)
    final_df = pd.concat(dataframes_ordered, axis=0)
    final_df = final_df[['ReporteId', 'labs_centros', 'labs_cuadrilla', 'labs_ruta']]
    return final_df


if __name__ == '__main__':
    casas_df = pd.DataFrame({
        'ReporteId': list(range(100)),
        'lon': np.random.rand(100),
        'lat': np.random.rand(100)})

    centros_df = pd.DataFrame({
        'labs_centros': list(range(5)),
        'lon': np.random.rand(5),
        'lat': np.random.rand(5),
        'n': [5, 2, 6, 3, 2]})
    df_final = pd.DataFrame({
        'ReporteId': list(range(100)),
        'labs_centros': [np.random.randint(0, 5) for x in range(0, 100)],
        'labs_cuadrilla': [np.random.randint(0, 5) for x in range(0, 100)]
        })

    df_output = crea_rutas(casas_df, df_final, centros_df)
