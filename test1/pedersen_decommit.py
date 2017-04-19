from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(900, 170)
parties = []
parties.append("Sender")
parties.append("Verifier\n checks whether c = (g^x * h^r) % p")

connections = []
connections.append("x, r")

protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/pedersen_decommit.png")





