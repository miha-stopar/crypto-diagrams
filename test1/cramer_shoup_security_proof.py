from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(1090, 200, font_size=14)
parties = []
parties.append("I, who can break Cramer-Shoup \n and would like to break DDH as well. \n Given a tuple (g_1, g_2, g_1^r_1, g_2^r_2) \n I would like to see whether r1 = r2.")
parties.append("Simulator gets g_1^r_1 and g_2^r_2, \n and chooses x1, x2, y1, y2, z1, z2. \n When it receives two messages, \n it chooses k from {0, 1} and encrypts m_k.")

connections = []
connections.append("m_0, m_1")
connections.append("(g_1^r_1, g_2^r_2, (g_1^r_1)^x1 * (g_2^r_2)^x2 * m_k, \n (g_1^r_1)^x1 * (g_2^r_2)^x2 * (g_1^r_1)^(h * y1) * (g_2^r_2)^(h * y2))")
connections.append("kk (0 or 1 - which message was encrypted)")
connections.append("true if k = kk, false otherwise")

protocol.draw_protocol(parties, connections, box_height=140)
protocol.save("../img/cramer_shoup_security_proof.png")





