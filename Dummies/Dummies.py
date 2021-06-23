"""
Machine Learning Python
Esta clase me permite realizar operaciones básicas sobre Dummies

Los Dummies son columnas nuevas que se crean en un archivo, basadas en una columna del archivo
Ejm:
Columna: sexo
Se crean 2 columnas nuevas
    sex_hombre
    sex_mujer

En cada fila del archivo cuando sex_hombre es 1, sex_mujer es 0
y al contrario, cuando sex_mujer es 1, sex_hombre es 0
"""


def create(panda, data_frame, name_column):
    dummy = panda.get_dummies(data_frame[name_column], prefix=name_column)
    data_frame = data_frame.drop(name_column, axis=1)
    data_frame = panda.concat([data_frame, dummy], axis=1)
    return data_frame

