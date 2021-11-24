import os
import cv2
import matplotlib.pyplot as plt

DATADIR = "E:\\repoGit\\memoria\\experimentos_memoria\\imagenes"
CATEGORIAS = ["otrosp","tiuque"]
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    dataFinal = []
    for categoria in CATEGORIAS:
        path = os.path.join(DATADIR, categoria)
        print("soy el path:"+path)
        valor = CATEGORIAS.index(categoria)
        for imagen in os.listdir(path):
            try:
                imagenRuta = os.path.join(path, imagen)
                img = cv2.imread(imagenRuta, cv2.IMREAD_COLOR)
                #buscar como leer los colores dependiendo de la imagen
                img= cv2.resize(img,(1000,800))
                plt.imshow(img)
                plt.show()
                dataFinal.append([img,valor])
            except Exception as e:
                pass
    # Use a breakpoint in the code line below to debug your script.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
