from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(1050, 170)
parties = []
parties.append("Function f:G->H is a q-one-way homomorphism.\n Prover knows u such that f(v) = u. \n Prover at the beginning \n chooses random r from G.")
parties.append("Verifier \n at the end verifies \n that f(z) = m * u^e")

connections = []
connections.append("m = f(r)")
connections.append("random q where 0 <= e < q")
connections.append("z = r * v^e")

protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/q-one-way_protocol.png")





