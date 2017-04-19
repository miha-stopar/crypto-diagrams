from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(700, 170)
parties = []
parties.append("Challenger \nchooses k from K\nchooses b from {0,1}")
parties.append("Adversary\ntries to guess b")

connections = []
connections.append("m_0, m_1 from M: |m_0| = |m_1|")
connections.append("c = E(k, m_b)")

protocol.draw_protocol(parties, connections, box_height=100, first_arrow_to_right=False)
protocol.save("../img/semantic_security.png")





