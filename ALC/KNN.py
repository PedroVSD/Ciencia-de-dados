import pandas as pd
from sklearn.model_selection import train_test_split


def main():

    data = pd.read_csv('D:\Cursos\Códigos\Treinando\Faculdade\AL computacional\wine.data',names=['classe', 'atr1', 'atr2', 'atr3', 'atr4', 'atr5', 'atr6', 'atr7', 'atr8', 'atr9', 'atr10', 'atr11', 'atr12', 'atr13'])

    x_train,x_teste = train_test_split(data, test_size=0.2, shuffle=True)

    y_train = x_train['class']
    del x_train['class']

    y_test = x_teste['class']
    del x_teste['class']

    print(data)


main()