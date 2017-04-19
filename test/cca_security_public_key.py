from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(700, 340)
parties = []
parties.append("Challenger \ngenerates (pk, sk)\nchooses b from {0,1}")
parties.append("Adversary\ntries to guess b")

connections = []
connections.append("pk")

connections.append("c_i from C")
connections.append("m_i = D(k, c_i)")

connections.append("m_0, m_1 from M: |m_0| = |m_1|")
connections.append("c = E(k, m_b)")

connections.append("c_i from C (c_i must not be c)")
connections.append("m_i = D(k, c_i)")

protocol.draw_protocol(parties, connections, box_height=270)
protocol.save("../img/cca_security_public_key.png")





