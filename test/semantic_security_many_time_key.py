from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(700, 170)
parties = []
parties.append("Challenger \nchooses k from K\nchooses b from {0,1}")
parties.append("Adversary\ntries to guess b")

connections = []
connections.append("for i = 1,...,q: m_i0, m_i1 from M: |m_i0| = |m_i1|")
connections.append("c_i = E(k, m_ib)")

protocol.draw_protocol(parties, connections, box_height=100, first_arrow_to_right=False)
protocol.save("../img/semantic_security_many_time_key.png")

