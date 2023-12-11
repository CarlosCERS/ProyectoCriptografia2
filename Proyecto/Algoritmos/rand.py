import platform  # Para comprender el sistema operativo en el que trabaja
import oqs.rand as oqsrand  # Se debe importar explícitamente

# Se crea un valor entrópico para las variables.
semillaEntropia = [0] * 48
for i in range(0, 48):
    semillaEntropia[i] = i

oqsrand.randombytes_nist_kat_init_256bit(bytes(semillaEntropia))
oqsrand.randombytes_switch_algorithm("NIST-KAT")
print('{:17s}'.format("NIST-KAT:"), ' '.join('{:02X}'.format(x) for x in oqsrand.randombytes(32)))

# we do not yet support OpenSSL under Windows
if platform.system() != "Windows":
    oqsrand.randombytes_switch_algorithm("OpenSSL")
    print('{:17s}'.format("OpenSSL:"), ' '.join('{:02X}'.format(x) for x in oqsrand.randombytes(32)))

oqsrand.randombytes_switch_algorithm("system")
print('{:17s}'.format("System (default):"), ' '.join('{:02X}'.format(x) for x in oqsrand.randombytes(32)))
