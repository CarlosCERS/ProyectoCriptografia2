import oqs
from pprint import pprint

print("Mecanismos KEM:")
kems = oqs.get_enabled_kem_mechanisms()
pprint(kems, compact=True)

# create client and server with sample KEM mechanisms
kemalg = "Kyber512"
with oqs.KeyEncapsulation(kemalg) as cliente:
    with oqs.KeyEncapsulation(kemalg) as server:
        print("\nDetalles del encapsulamiento de llaves:")
        pprint(cliente.details)

        # Cliente genera su llave.
        llavePublicaCliente = cliente.generate_keypair()
        ciphertext, secretoCompartidoServidor = server.encap_secret(llavePublicaCliente)

        # El cliente desencapsula el texto cifrado del servidor y obtiene el secreto
        secretoCompartidoCliente = cliente.decap_secret(ciphertext)

        print("\n¿Coincidencia de secretos compartidos?:", secretoCompartidoCliente == secretoCompartidoServidor)
