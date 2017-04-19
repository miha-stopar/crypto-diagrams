from cdiagrams.protocol import Protocol

protocol = Protocol(900, 70)

# derivation of persistent key:
connections = []
connections.append(["passphrase", "BLAKE2 (hash)", "passphrase hash"])
connections.append(["", "scrypt (KDF)", "private key"])
connections.append(["", "curve25519-xsalsa20-poly1305", "public key"])

# encryption:
connections = []
#connections.append(["fileInfo", "curve25519-xsalsa20-poly1305 asymmetric encryption \n(using sender's private key and recipient's public key)", "encrypted fileInfo"])
connections.append(["encrypted fileInfo", "curve25519-xsalsa20-poly1305 asymmetric decryption \n(using sender's public key and recipient's private key)", "fileInfo"])
#connections.append(["decryptInfo", "curve25519-xsalsa20-poly1305 asymmetric encryption \n(using sender's ephemeral private key and recipient's (persistent) public key)", "encrypted decryptInfo"])

#connections.append(["encrypted decryptInfo", "curve25519-xsalsa20-poly1305 asymmetric decryption \n(using sender's ephemeral public key and recipient's (persistent) private key)", "decryptInfo"])
#connections.append(["encrypted sender's\n ID", "curve25519-xsalsa20-poly1305 asymmetric decryption \n(using sender's ephemeral public key and recipient's (persistent) private key)", "sender's ID"])


protocol.draw_connections(connections)
protocol.save("../img/minilock.png")


