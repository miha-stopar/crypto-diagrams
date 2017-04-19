from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(900, 240)
parties = []
parties.append("Prover \n")
parties.append("Verifier \n at the end accepts \n if and only if the trapdoor is valid \n and (a, e, z) is accepting")

connections = []
connections.append("chooses random e and commits to it via commitment protocol")
connections.append("first message a of sigma protocol")
connections.append("reveals e by decommitting")
connections.append("z, trapdoor (if decommitment is valid)")

protocol.draw_protocol(parties, connections, box_height=140, first_arrow_to_right=False)
protocol.save("../img/zk_from_sigma_protocol.png")





