import os

################# Cifrado y Descifrado ######################
Vector = "Proyecto/Vectores/Texto.txt"
print(f"Procesando encriptaciónes post-cuánticos")

# ML-KEM Scheme
print('Ejecutando ML-KEM Scheme')
os.system('py Proyecto/Algoritmos/kem.py')
print('Ejecución terminada exitosamente\n\n')

# ML-DSA Signature Scheme
print('Ejecutando ML-DSA Signature Scheme')
os.system('py Proyecto/Algoritmos/rand.py')
print('Ejecución terminada exitosamente\n\n')

# SLH-DSA Signature Scheme
print('Ejecutando SLH-DSA Signature Scheme')
os.system('py Proyecto/Algoritmos/sig.py')
print('Ejecución terminada exitosamente\n\n')

print('Fin del programa.')
