from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(700, 400)
parties = []
parties.append("Challenger \n(chooses k from K)")
parties.append("Adversary")

connections = []
connections.append("m_1, m_2,...,m_q from M")
connections.append("t_1, t_2,...,t_q where t_i = S(k, m_i)")
connections.append("(m, t)")

protocol.draw_protocol(parties, connections)
protocol.save("../img/secure_mac.png")


