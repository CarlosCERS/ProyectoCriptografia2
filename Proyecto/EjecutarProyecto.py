import json
from Herramientas import Graficar

with open("Proyecto/Claves.json","r") as f:
    my_dict=json.load(f)

Key = my_dict["Key"]
Ciclos = int(my_dict["Ciclos"])
Resultado = open('Proyecto/Resultados.txt','w')

################# Cifrado y Descifrado ######################
Vector = "Proyecto/Vectores/Texto.txt"
titulos=[]
tiemposEncriptacion=[]
tiemposDesencriptacion=[]
print(f"Procesando encriptaciónes post-cuánticos")

# ML-KEM Scheme
titulos.append('ML-KEM Scheme')
# Encriptado, Desencriptado = chacha20.calcularTiempo(Vector,Ciclos,Key)
# tiemposEncriptacion.append(Encriptado)
# tiemposDesencriptacion.append(Desencriptado)
tiemposEncriptacion.append(0)
tiemposDesencriptacion.append(2)

# ML-DSA Signature Scheme
titulos.append('ML-DSA Signature Scheme')
# Encriptado_AES_ECB, Desencriptado_AES_ECB = aes_ecb.calcularTiempo(Vector,Ciclos,Key)
# tiemposEncriptacion.append(Encriptado_AES_ECB)
# tiemposDesencriptacion.append(Desencriptado_AES_ECB)
tiemposEncriptacion.append(3)
tiemposDesencriptacion.append(4)

# SLH-DSA Signature Scheme
titulos.append('SLH-DSA Signature Scheme')
# Encriptado_AES_GCM, Desencriptado_AES_GCM = aes_gcm.calcularTiempo(Vector,Ciclos,Key)
# tiemposEncriptacion.append(Encriptado_AES_GCM)
# tiemposDesencriptacion.append(Desencriptado_AES_GCM)
tiemposEncriptacion.append(6)
tiemposDesencriptacion.append(7)

Resultado.write(f'Encriptacion y desencriptacion: {Vector}, {Ciclos} ciclos\n')
for i in range(len(titulos)):
    Resultado.write(f'{titulos[i]} \n\t Encriptacion:{tiemposEncriptacion[i]} \n\t Desencriptacion:{tiemposDesencriptacion[i]}\n')
Resultado.write('\n')
# Graficar.
Graficar.GraficarEncriptadoDesencriptado(Vector,titulos,tiemposEncriptacion,tiemposDesencriptacion,Ciclos)

# Finalización.
Resultado.close()
print('Fin del programa.')
