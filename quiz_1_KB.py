class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_min_max(self):
        flat_matrix = [item for row in self.matrix for item in row]
        return min(flat_matrix), max(flat_matrix)

    def transpose_matrix(self):
        return [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

    def multiply_with_transpose(self):
        transpose = self.transpose_matrix()
        result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in transpose] for row_a in self.matrix]
        return result

    def add_with_transpose(self):
        transpose = self.transpose_matrix()
        result = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.matrix, transpose)]
        return result


if __name__ == "__main__":
    # Contoh matriks
    matrix_a = [
        [34, 100, 12],
        [72, 24, 55],
        [61, 20, 19]
    ]

    # Membuat objek dari kelas MatrixOperations
    matrix_operations = MatrixOperations(matrix_a)

    # Operasi 1: Menghitung elemen terbesar dan terkecil
    min_val, max_val = matrix_operations.find_min_max()
    print(f"Elemen terkecil: {min_val}, Elemen terbesar: {max_val}")

    # Operasi 2: Transpose matriks
    transposed_matrix = matrix_operations.transpose_matrix()
    print("Matriks Transpose:")
    for row in transposed_matrix:
        print(row)

    # Operasi 3: Menghitung perkalian matriks dengan transpose
    multiplication_result = matrix_operations.multiply_with_transpose()
    print("Hasil Perkalian Matriks dengan Transpose:")
    for row in multiplication_result:
        print(row)

    # Operasi 4: Menghitung penjumlahan matriks dengan transpose
    addition_result = matrix_operations.add_with_transpose()
    print("Hasil Penjumlahan Matriks dengan Transpose:")
    for row in addition_result:
        print(row)
        