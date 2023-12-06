import os
import matplotlib.pyplot as plt

# Grafica las comparaciones de encriptado y desencriptado.
def GraficarEncriptadoDesencriptado(archivo, titulos, tiemposCifrado, tiemposDescifrado, ciclos):

    # Colores.
    colors = ['pink', 'yellow', 'blue', 'green', 'red', 'orange']

    # Tamaño o número de gráficas a crear.
    tamanio = len(titulos)

    # Obtener el nombre del archivo.
    file_name = os.path.basename(archivo)

    if(tamanio>1):
        # Declaramos el número de barras a crear.
        fig, ax = plt.subplots(1, tamanio, figsize=(25, 5), sharey=True)

        for i in range(tamanio):
            # Graficar tiempos de encriptación
            ax[i].bar(0, tiemposCifrado[i], color=colors[i])

            # Graficar tiempos de desencriptación
            ax[i].bar(1, tiemposDescifrado[i], color=colors[i])

            ax[i].set_xticks([0, 1])
            ax[i].set_xticklabels(["Cifrado", "Descifrado"])
            ax[i].set_title(f'{titulos[i]}')

        ax[0].set_ylabel("Tiempo promedio (s)")
        # Título
        fig.suptitle(f'Gráficas de tiempo de ejecución de algorítmos de encriptación y desencriptación: {ciclos} ciclos para: {file_name}', fontsize=16)
        plt.show()
    else:
        # Declaramos el número de barras a crear.
        fig, ax = plt.subplots(1, tamanio, figsize=(15, 5), sharey=True)

        # Graficar tiempos de encriptación
        ax.bar(0, tiemposCifrado[0], color=colors[0])

        # Graficar tiempos de desencriptación
        ax.bar(1, tiemposDescifrado[0], color=colors[0])

        ax.set_xticks([0, 1])
        ax.set_xticklabels(["Cifrado", "Descifrado"])
        ax.set_title(f'{titulos[0]}')

        ax.set_ylabel("Tiempo promedio (s)")
        # Título
        fig.suptitle(f'Gráficas de tiempo de ejecución de algorítmos de encriptación y desencriptación: {ciclos} ciclos para: {file_name}', fontsize=16)
        plt.show()