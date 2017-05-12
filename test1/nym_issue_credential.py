from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(1100, 300, arrow_offsets=[40, 40, 40, 60, 40, 40])
parties = []

parties.append("User first authenticates with his nym (a, b).\n It then acts as a verifier in two dlog equality proofs \n and stores both blinded transcripts: T1, T2.\n The credential is:\n (a^gamma, b^gamma, A^gamma, B^gamma, T1, T2).")
parties.append("Organization checks whether (a, b) is registered \n and then verifies that the user knows log_a(b).\nThen it provides A, B and proves that\n log_b(A)=log_g(h2) and log_a*A(B)=log_g(h1).")

connections = []
connections.append("a, b, a^r where r random from Z_q*")
connections.append("random c")
connections.append("y = r + s*c")
connections.append("A = b^s2, B = (a*b^s2)^s1, \n g^r1, b^r1, g^r2, (a*A)^r2")
connections.append("random c1, c2")
connections.append("y1 = r1 + s2*c1, y2 = r2 + s1*c2")


protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/nym_credential_issue.png")





