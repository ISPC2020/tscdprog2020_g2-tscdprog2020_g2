# librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def analisis(datos):
    salarios = []
    fechas = []

    # Separacion de datos
    for i in datos:
        fecha = str(i[1])
        fecha = fecha[:4]

        fechas.append(int(fecha))
        salarios.append(int(i[0]))

    # Operaciones con DataFrame
    df = pd.DataFrame()
    df['Salarios'] = salarios
    df['Fechas'] = fechas
    print(f'Analisis del salario historico del empleado'.center(50, '-'))
    print(df.describe())

    # Creacion de los arrays
    x = df['Fechas'].to_numpy()
    y = df['Salarios'].to_numpy()

    # Agregar una dimencion extra a x
    x_entrenamiento = x.reshape((-1, 1))

    # Creando el modelo
    model = LinearRegression()

    # Entrenando en modelo
    model.fit(x_entrenamiento, y)

    # Valuando el modelo
    r_sq = model.score(x_entrenamiento, y)

    print(f'Precision del modelo: {r_sq}')

    # Prediccion
    y_pred = model.predict(x_entrenamiento)

    # Predecir nuevos datos desde el ultimo año del registro + 6 años
    x_nuevo = np.arange(x[-1], x[-1] + 6).reshape((-1, 1))
    y_futuro = model.predict(x_nuevo)

    # Grafico
    plt.scatter(x, y)
    plt.scatter(x_nuevo, y_futuro, color='g', label='Estimacion futura')
    plt.plot(x_entrenamiento, y_pred, color='r', label='Regresion lineal')
    plt.legend(loc='lower right')
    plt.xlabel('Año')
    plt.ylabel('Salario')
    plt.show()


