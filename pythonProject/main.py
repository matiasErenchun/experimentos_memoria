import os
import PIL
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mti
import random
import csv
import numpy as np
import pandas as pd

# revisar esto https://www.it-swarm-es.com/es/python/conversion-de-imagenes-archivo-csv-en-python/837845450/

DATADIR = "E:\\repoGit\\memoria\\experimentos_memoria\\imagenes"  # directorio donde estan nuestros datos
CATEGORIAS = ["otrosp", "tiuque"]  # categorias correspondientes alos nombre sde las carpetas de nuestros datos


def print_hi():
    dataFinal = []
    imanges = []
    etiquetas = []
    for categoria in CATEGORIAS:  # recorremos cada carpeta de categoria
        path = os.path.join(DATADIR, categoria)  # estoe s para entrar a la carpeta
        valor = CATEGORIAS.index(
            categoria)  # obtenemso el indice de la categorias (asi la categoria se asocia aun valor numerico)
        for imagen in os.listdir(path):
            try:
                imagenRuta = os.path.join(path, imagen)
                img = cv2.imread(imagenRuta, cv2.COLOR_BGR2RGB)
                # buscar como leer los colores dependiendo de la imagen
                img = cv2.resize(img, (1000, 800))
                dataFinal.append([img, valor])
            except Exception as e:
                pass
    print(dataFinal.pop(0))
    random.shuffle(dataFinal)
    # dataFrame = pd.DataFrame(dataFinal)
    # dataFrame.to_csv('dataSetPrueba.csv')


# Press the green button in the gutter to run the script.
def readData():
    # dataFrame = pd.read_csv('dataSetPrueba.csv')
    # print(dataFrame.shape)
    # print(dataFrame.head(3))
    with open('dataSetPrueba.csv') as csvfile:
        reader = pd.read_csv(csvfile)
        print(reader.shape[0])
        fila = reader.iloc[1]
        print(fila)
        imagen = fila['imagen']
        print(len(imagen))
        img = np.array(imagen.split())
        img = img.reshape(1000, 800)  # dimensions of the image
        image = np.zeros((1000, 800, 3))  # empty matrix
        image[:, :, 0] = img
        image[:, :, 1] = img
        image[:, :, 2] = img

        image.astype(np.uint8)
        cv2.imshow("imagen", image)


def readData2():
    datos=[]
    for categoria in CATEGORIAS:  # recorremos cada carpeta de categoria
        path = os.path.join(DATADIR, categoria)  # estoe s para entrar a la carpeta
        valor = CATEGORIAS.index(
            categoria)  # obtenemso el indice de la categorias (asi la categoria se asocia aun valor numerico)
        for imagen in os.listdir(path):
            try:
                imagenRuta = os.path.join(path, imagen)
                print(imagenRuta)
                imagenn = np.array(PIL.Image.open(imagenRuta))
                otherimagen = cv2.resize(imagenn, (1000, 800))
                print(otherimagen.shape)
                otherimage = otherimagen.reshape(otherimagen.shape[0], -1)
                # print(otherimagen.shape)
                # img = cv2.imread(imagenRuta, cv2.IMREAD_REDUCED_COLOR_4)
                # buscar como leer los colores dependiendo de la imagen
                # img = cv2.resize(img, (1000, 800))
                # plt.imshow(imagenn)
                datos.append([otherimage,valor])
            except Exception as e:
                print(e)
                pass
            break
        break
    with open('some.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(datos)

def loaderImage():
    imagen = np.loadtxt('imangenprueba.csv')
    print(imagen.shape)
    print(imagen.shape[0])
    print(imagen.shape[1])
    print(imagen.shape[2])
    loaded_mat = imagen.reshape(imagen.shape[0],
                                imagen.shape[1] // imagen.shape[2],
                                imagen.shape[2])
    value = np.array(loaded_mat).astype(int)
    print(value)
    plt.imshow(value)
    plt.show()


if __name__ == '__main__':
    # readData()
    #print_hi()
    readData2()
    # loaderImage()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
