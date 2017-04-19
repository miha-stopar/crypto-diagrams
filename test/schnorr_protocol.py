from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(650, 170)
parties = []
parties.append("Prover \n at the beginning \n chooses random r from Z_q")
parties.append("Verifier \n at the end verifies \n that g^y = g^r * (g^s)^c mod p")

connections = []
connections.append("x = g^r % p")
connections.append("random c")
connections.append("y = (r + s*c) % q")

protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/schnorr_protocol.png")





