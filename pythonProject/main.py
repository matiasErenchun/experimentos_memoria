import os
import cv2
import matplotlib.pyplot as plt

DATADIR = "E:\\repoGit\\memoria\\experimentos_memoria\\imagenes"
CATEGORIAS = ["otrosp","tiuque"]
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    for categoria in CATEGORIAS:
        path = os.path.join(DATADIR, categoria)
        print("soy el path:"+path)
        for imagen in os.listdir(path):
            imagenRuta = os.path.join(path, imagen)
            img = cv2.imread(imagenRuta, cv2.IMREAD_COLOR)
            #buscar como leer los colores dependiendo de la imagen
            plt.imshow(img)
            plt.show()
    # Use a breakpoint in the code line below to debug your script.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
