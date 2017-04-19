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

