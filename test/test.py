from cdiagrams.matrix_operation import MatrixOperation

matrix_operation = MatrixOperation(230, 130)
matrices = []

texts = ['k_0', 'k_4', 'k_8', 'k_12',
         'k_1', 'k_5', 'k_9', 'k_13',
         'k_2', 'k_6', 'k_10', 'k_14',
         'k_3', 'k_7', 'k_11', 'k_15']
#texts = ['w_0', 'w_1', 'w_2', 'w_3']
matrix = [4, texts]
matrices.append(matrix)

matrix_operation.draw_matrices(matrices)
matrix_operation.save("../img/key_expansion1.png")



