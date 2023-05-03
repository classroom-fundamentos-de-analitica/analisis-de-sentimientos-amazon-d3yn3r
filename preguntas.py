"""
Análisis de Sentimientos usando Naive Bayes
-----------------------------------------------------------------------------------------

El archivo `amazon_cells_labelled.txt` contiene una serie de comentarios sobre productos
de la tienda de amazon, los cuales están etiquetados como positivos (=1) o negativos (=0)
o indterminados (=NULL). En este taller se construirá un modelo de clasificación usando
Naive Bayes para determinar el sentimiento de un comentario.

"""
import numpy as np
import pandas as pd


def pregunta_01():
    """
    Carga de datos.
    -------------------------------------------------------------------------------------
    """

    # Lea el archivo `amazon_cells_labelled.tsv` y cree un DataFrame usando pandas.
    # Etiquete la primera columna como `msg` y la segunda como `lbl`. Esta función
    # retorna el dataframe con las dos columnas.
    df = pd.read_csv(
        'amazon_cells_labelled.txt',
        sep='\t',
        header=None,
        names=['mensaje','numero'],
    )

    # Separe los grupos de mensajes etiquetados y no etiquetados.
    df_tagged = df[df["numero"].notnull()]
    df_untagged = df[df["numero"].isna()]

    x_tagged = df["mensaje"]
    y_tagged = df["numero"]

    x_untagged = df["mesanje"]
    y_untagged = df["numero"]

    # Retorne los grupos de mensajes
    return x_tagged, y_tagged, x_untagged, y_untagged