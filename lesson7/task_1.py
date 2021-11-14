class Matrix:

    def __init__(self, my_lists):
        self.my_lists = my_lists

    def __str__(self):
        return '\n'.join(map(str, self.my_lists))

    def __add__(self, other):
        matrix_three = []
        for i in range(len(self.my_lists)):
            matrix_three.append([])
            for j in range(len(self.my_lists[i])):
                matrix_three[i].append(self.my_lists[i][j] + other.my_lists[i][j])
        return '\n'.join(map(str, matrix_three))


matrix_one = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_two = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(matrix_one, '\n')
print(matrix_two, '\n')
print(matrix_one + matrix_two)
