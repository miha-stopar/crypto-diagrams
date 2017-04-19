from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(1040, 170)
parties = []
parties.append("Dealer \n at the beginning \n chooses random w from Z_q \n (y = h^z (mod p) is P_i's public key, \n enc_P_i(s_i) = (h^alpha, s_i_inv * y^alpha), \n U = S_i^(s_i_inv * y^alpha)) = g^(s_i * s_i_inv * y^alpha) = g^(y^alpha)")
parties.append("Verifier \n at the end verifies \n that g^r = g^w * (g^alpha)^c (mod p) \n and (g^y)^r = (g^y)^w * U^c)")

connections = []
connections.append("g^w % p, (g^y)^w")
connections.append("random c")
connections.append("r = (w + alpha*c) % q")

protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/stadler_verifiable_encryption.png")





