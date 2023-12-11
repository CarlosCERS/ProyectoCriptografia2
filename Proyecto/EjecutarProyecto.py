import os
import oqs

################# Cifrado y Descifrado ######################
Vector = "Proyecto/Vectores/Texto.txt"
print(f"Procesando encriptaciónes post-cuánticos")
print("Versión del liboqs:", oqs.oqs_version())
print("Versión del liboqs-python:", oqs.oqs_python_version())
print("\n\n")

# ML-KEM Scheme
print('Ejecutando ML-KEM Scheme')
os.system('py Proyecto/Algoritmos/kem.py')
print('Ejecución terminada exitosamente\n\n')

# ML-DSA Signature Scheme
print('Ejecutando ML-DSA Signature Scheme')
os.system('py Proyecto/Algoritmos/rand.py')
os.system('py Proyecto/Algoritmos/sig.py')
print('Ejecución terminada exitosamente\n\n')

# SLH-DSA Signature Scheme
print('Ejecutando SLH-DSA Signature Scheme')
os.system('py Proyecto/Algoritmos/sig2.py')
print('Ejecución terminada exitosamente\n\n')

print('Fin del programa.')
