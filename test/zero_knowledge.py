from cdiagrams.matrix_operation import MatrixOperation

matrix_operation = MatrixOperation(230, 150)
matrices = []

texts = ['0', '0', '0', '...', '1', '0',
         '0', '1', '0', '...', '0', '0',
         '0', '0', '0', '...', '0', '0',
         '0', '0', '1', '...', '0', '0',
         '0', '0', '0', '...', '0', '0']
matrix = [6, texts]
matrices.append(matrix)

matrix_operation.draw_matrices(matrices)
matrix_operation.save("../img/zero_knowledge.png")



