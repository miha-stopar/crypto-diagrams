from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(1050, 170)
parties = []
parties.append("Signer \n at the beginning \n chooses random r from Z_q; m is message to be signed")
parties.append("Verifier \n at the end verifies \n that g^y = g^r * (g^s)^hash(m ||x) mod p")

connections = []
connections.append("x = g^r % p \n y = (r + s * hash(m || x)) % q \n signature = (y, hash(m || x))")

protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/schnorr_signature.png")





