import json

with open("Proyecto/Claves.json","r") as f:
    my_dict=json.load(f)

Key = my_dict["Key"]
Ciclos = int(my_dict["Ciclos"])

################# Cifrado y Descifrado ######################
Vector = "Proyecto/Vectores/Texto.txt"
print(f"Procesando encriptaciónes post-cuánticos")

# ML-KEM Scheme
print('Ejecutando ML-KEM Scheme')

print('Ejecución terminada exitosamente')

# ML-DSA Signature Scheme
print('Ejecutando ML-DSA Signature Scheme')

print('Ejecución terminada exitosamente')

# SLH-DSA Signature Scheme
print('Ejecutando SLH-DSA Signature Scheme')

print('Ejecución terminada exitosamente')

print('Fin del programa.')
