from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(1210, 240)
parties = []
parties.append("I, who can break ElGamal \n and would like to break DDH as well. \n Given a tuple (g, g^a, g^b, Z) I would like to see whether Z = g^(ab).")
parties.append("Simulator gets g^b and Z, \n it encrypts message m as (g^b, Z * m). \n When it receives two messages, \n it chooses k from {0, 1} and encrypts m_k.")

connections = []
connections.append("m_0, m_1")
connections.append("(g^b, Z * m_k)")
connections.append("kk (0 or 1 - which message was encrypted)")
connections.append("true if k = kk, false otherwise")

protocol.draw_protocol(parties, connections, box_height=140)
protocol.save("../img/elgamal_security_proof.png")





