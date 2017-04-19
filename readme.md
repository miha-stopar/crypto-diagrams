# cryptodiagrams

A tiny library for quickly drawing cryptograhic protocols and some other cryptographic objects. Used for [crypto-notes](https://github.com/miha-stopar/crypto-notes).

### Schnorr protocol

```
from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(900, 170)
parties = []
parties.append("Prover \n at the beginning \n chooses random r from Z_q")
parties.append("Verifier \n at the end verifies \n that g^y = g^r * (g^s)^c mod p")

connections = []
connections.append("x = g^r % p")
connections.append("random c")
connections.append("y = (r + s*c) % q")

protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/schnorr_protocol.png"
```

![schnorr protocol](https://raw.github.com/miha-stopar/crypto-diagrams/master/img/schnorr_protocol.png)

### Schnorr Signature

```
from cdiagrams.protocol2 import Protocol2

protocol = Protocol2(1050, 170)
parties = []
parties.append("Signer \n at the beginning \n chooses random r from Z_q; m is message to be signed")
parties.append("Verifier \n at the end verifies \n that g^y = g^r * (g^s)^hash(m ||x) mod p")

connections = []
connections.append("x = g^r % p \n y = (r + s * hash(m || x)) % q \n signature = (y, hash(m || x))")

protocol.draw_protocol(parties, connections, box_height=100)
protocol.save("../img/schnorr_signature.png")
```

![schnorr signature](https://raw.github.com/miha-stopar/crypto-diagrams/master/img/schnorr_signature.png)

### AES S-box bit scrambling

```
from cdiagrams.matrix_operation import MatrixOperation

matrix_operation = MatrixOperation(450, 240)
matrices = []
cols = 8
texts = ['1', '0', '0', '0', '1', '1', '1', '1',
         '1', '1', '0', '0', '0', '1', '1', '1',
         '1', '1', '1', '0', '0', '0', '1', '1',
         '1', '1', '1', '1', '0', '0', '0', '1',
         '1', '1', '1', '1', '1', '0', '0', '0',
         '0', '1', '1', '1', '1', '1', '0', '0',
         '0', '0', '1', '1', '1', '1', '1', '0',
         '0', '0', '0', '1', '1', '1', '1', '1']
matrix = [cols, texts]
matrices.append(matrix)


texts = ['b_0', 'b_1', 'b_2', 'b_3', 'b_4', 'b_5', 'b_6', 'b_7']
cols = 1
matrix = [cols, texts]
matrices.append(matrix)


matrices.append([1, "+"])

matrix = [1, ['1', '1', '0', '0', '0', '1', '1', '0']]
matrices.append(matrix)

matrix_operation.draw_matrices(matrices)
matrix_operation.save("../img/sbox3.png")
```
![sbox](https://raw.github.com/miha-stopar/crypto-diagrams/master/img/sbox3.png)

### Shifting rows in AES S-box

```
from cdiagrams.matrix_operation import MatrixOperation

matrix_operation = MatrixOperation(420, 130)
matrices = []

texts = ['s_00', 's_01', 's_02', 's_03',
         's_10', 's_11', 's_12', 's_13',
         's_20', 's_21', 's_22', 's_23',
         's_30', 's_31', 's_32', 's_33']
matrix = [4, texts]
matrices.append(matrix)

matrices.append([1, "=>"])

texts = ['s_00', 's_01', 's_02', 's_03',
         's_11', 's_12', 's_13', 's_10',
         's_22', 's_23', 's_20', 's_21',
         's_33', 's_30', 's_31', 's_32']
matrix = [4, texts]
matrices.append(matrix)

matrix_operation.draw_matrices(matrices)
matrix_operation.save("../img/sbox4.png")
```

![sbox](https://raw.github.com/miha-stopar/crypto-diagrams/master/img/sbox4.png)

### Cramer-Shoup encryption security proof

```
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
```

![Cramer-Shoup](https://raw.github.com/miha-stopar/crypto-diagrams/master/img/cramer_shoup_security_proof.png)


## Installation

TBD
