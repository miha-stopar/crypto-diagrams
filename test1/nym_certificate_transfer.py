from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(1200, 180)
parties = []
parties.append("User first authenticates with a nym (a1, b1).\n He holds a credential:\n(a', b', A', B', T1, T2).")
parties.append("Organization checks whether (a1, b1) is registered. \n At the end it verifies whether \na1^y = a1^r * (a1^s)^c % p and a'^y = a'^r * (a'^s)^c % p. \n This way the user proved the knowledge of \n dlog_a1(b1), dlog_a'(b') and that it is the same. \nOrganization then checks whether both transcripts are valid.")

connections = []
connections.append("a1, b1, a1^r, a'^r where r is random from Z_q*")
connections.append("random c")
connections.append("y = r + s*c")

protocol.draw_protocol(parties, connections, box_height=120)
protocol.save("../img/nym_certificate_transfer.png")





