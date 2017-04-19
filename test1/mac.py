from cdiagrams.protocol import Protocol

protocol = Protocol(420, 50)

# derivation of persistent key:
connections = []
connections.append(["Alice (knows k)", "message m, tag t", "Bob (knows k)"])

protocol.draw_connections(connections)
protocol.save("../img/mac.png")


