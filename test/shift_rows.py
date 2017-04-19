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

