class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_list]))

    def __add__(self, other):
        matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                matr[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


matrix1 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix1)
print()
print(matrix2)
print()
print()
print(matrix1 + matrix2)
