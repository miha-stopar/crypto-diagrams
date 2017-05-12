from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(1200, 170)
parties = []
parties.append("Prover knows a secret s such that h1=g1^s % p and h2=g2^s % p, \n and wants to prove that he knows dlog of h1 and h2,\n and that it is the same. \n At the beginning \n he chooses random r from Z_q")
parties.append("Verifier \n at the end verifies \n that g1^y = g1^r * (g1^s)^c % p and g2^y = g2^r * (g2^s)^c % p")

connections = []
connections.append("g1^r % p, g2^r % p")
connections.append("random c")
connections.append("y = (r + s*c) % q")

protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/dlog_equality.png")





