import oqs
from pprint import pprint

print("Mecanismos de signature:")
sigs = oqs.get_enabled_sig_mechanisms()
pprint(sigs, compact=True)

message = "This is the message to sign".encode()

# Se crea un firmante y un verificador.
sigalg = "SPHINCS+-SHA2-256s-simple"
with oqs.Signature(sigalg) as firmante:
    with oqs.Signature(sigalg) as verificador:
        print("\nSignature details:")
        pprint(firmante.details)

        # Firmannte genera su llave pública.
        llavePublicaFirmante = firmante.generate_keypair()
       
        # Se firma el mensaje.
        firma = firmante.sign(message)

        # El verificador verifica la firma.
        esValido = verificador.verify(message, firma, llavePublicaFirmante)

        print("\n¿Firma válida?:", esValido)
