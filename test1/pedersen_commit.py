from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(900, 170)
parties = []
parties.append("Sender \n chooses random x from Z_q \n (h = g^a % p; values p, q, g, h are public, a is secret)")
parties.append("Verifier")

connections = []
connections.append("c = (g^x * h^r) % p")

protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/pedersen_commit.png")





