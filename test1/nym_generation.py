from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(1200, 170)
parties = []

parties.append("Chooses random gamma from Z_q*, \ncompute a_tilde = g^gamma, b_tilde = g^(gamma * x).\n After receiving a, compute b = a^x.\n Execute dlog equality proof protocol to show\n that log_a(b) = log_a_tilde(b_tilde).")
parties.append("After receiving a_tilde and b_tilde chooses random r from Z_q* \nand compute a = a_tilde^r.")

connections = []
connections.append("a_tilde, b_tilde")
connections.append("a")


protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/nym_generation.png")





