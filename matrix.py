# TODO:
# [X] Add a new class that takes a list of lists and creates a matrix
# [X] Change the print function to print the matrix in a nice way:
#       e.g.
#        |‾ 1 2 3 ‾|      / 1 2 3 \     / 1 2 \    |‾ 1 2 ‾|
#        |  4 5 6  |     |  4 5 6  |    \ 3 4 /    |_ 3 4 _|
#        |_ 7 8 9 _|      \ 7 8 9 /     

class Matrix:
    '''
    Base matrix class
    Input a matrix string separating each value with a space
    Each row is separated by a new string
    Functions:
        - dimensions
        - determinant
        - transpose
        - inverse
        - cofactors (finds the matrix of cofactors)
        - minors (finds the matrix of minors)
    Can also add, subtract, multiply, and raise to a power
    If using slice notation, the row is selected first
    Alegbra not supported
    '''
    def __init__(self, *matrix_string, vector=False):
        self.matrix = [[float(num) for num in row.split()] for row in matrix_string]

    def dimensions(self):
        return (len(self.matrix[0]), len(self.matrix))

    def determinant(self):
        if self.dimensions() == (3, 3):
            # a(ei − fh) − b(di − fg) + c(dh − eg)
            self.det = self.matrix[0][0]*(self.matrix[1][1]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][1]) - self.matrix[0][1]*(self.matrix[1][0]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][0]) + self.matrix[0][2]*(self.matrix[1][0]*self.matrix[2][1] - self.matrix[1][1]*self.matrix[2][0])
            return self.det
        elif self.dimensions() == (2, 2):
            # ad − bc
            self.det = (self.matrix[0][0]*self.matrix[1][1]) - (self.matrix[0][1]*self.matrix[1][0])
            return self.det
        elif self.dimensions() == (1, 1):
            self.det = self.matrix[0][0]
            return self.det
        else:
            raise Unknow_Determinant(*self.dimensions())

    def transpose(self):
        new_matrix = []
        for i in range(len(self.matrix[0])):
            new_row = []
            for j in range(len(self.matrix)):
                new_row.append(str(self.matrix[j][i]))
            new_matrix.append(' '.join(new_row))
        return Matrix(*new_matrix)

    def inverse(self):
        if self.dimensions() == (3, 3):
            if self.determinant() == 0:
                raise No_Inverse()
            else:
                mat_minors = self.minors()

                mat_cofactors = self.cofactors(mat_minors)
                
                mat_tranposed = mat_cofactors.transpose()

                inverse_matrix = (1/self.determinant())*mat_tranposed
                return inverse_matrix
            
        elif self.dimensions() == (2, 2):
            if self.determinant() == 0:
                raise No_Inverse()
            else:
                a, b, c, d = self.matrix[0][0], self.matrix[0][1], self.matrix[1][0], self.matrix[1][1]
                new_matrix = [f"{d} {-b}", f"{-c} {a}"]
                inverse_matrix = (1/self.determinant())*Matrix(*new_matrix)
                return inverse_matrix

        elif self.dimensions() == (1, 1):
            reciprocal = 1/self.matrix[0][0]
            return Matrix(str(reciprocal))

        else:
            raise Unknow_Inverse(*self.dimensions())

    def cofactors(self, mat_minors):
        mat_cofactors = []
        for i in range(len(mat_minors.matrix)):
            new_row = []
            for j in range(len(mat_minors.matrix[i])):
                if (i+j) % 2 == 0:
                    new_row.append(str(int(mat_minors.matrix[i][j])))
                else:
                    new_row.append(str(mat_minors.matrix[i][j] * -1))
            mat_cofactors.append(' '.join(new_row))
        mat_cofactors = Matrix(*mat_cofactors)
        return mat_cofactors

    def minors(self):
        mat_minors = []
        for i in range(len(self.matrix)):
            new_row = []
            for j in range(len(self.matrix[i])):
                if j == 0:
                    if i == 0:
                        matrix2x2 = [f'{self.matrix[1][1]} {self.matrix[1][2]}', f'{self.matrix[2][1]} {self.matrix[2][2]}']
                    elif i == 1:
                        matrix2x2 = [f'{self.matrix[0][1]} {self.matrix[0][2]}', f'{self.matrix[2][1]} {self.matrix[2][2]}']
                    elif i == 2:
                        matrix2x2 = [f'{self.matrix[0][1]} {self.matrix[0][2]}', f'{self.matrix[1][1]} {self.matrix[1][2]}']
                elif j == 1:
                    if i == 0:
                        matrix2x2 = [f'{self.matrix[1][0]} {self.matrix[1][2]}', f'{self.matrix[2][0]} {self.matrix[2][2]}']
                    elif i == 1:
                        matrix2x2 = [f'{self.matrix[0][0]} {self.matrix[0][2]}', f'{self.matrix[2][0]} {self.matrix[2][2]}']
                    elif i == 2:
                        matrix2x2 = [f'{self.matrix[0][0]} {self.matrix[0][2]}', f'{self.matrix[1][0]} {self.matrix[1][2]}']
                elif j == 2:
                    if i == 0:
                        matrix2x2 = [f'{self.matrix[1][0]} {self.matrix[1][1]}', f'{self.matrix[2][0]} {self.matrix[2][1]}']
                    elif i == 1:
                        matrix2x2 = [f'{self.matrix[0][0]} {self.matrix[0][1]}', f'{self.matrix[2][0]} {self.matrix[2][1]}']
                    elif i == 2:
                        matrix2x2 = [f'{self.matrix[0][0]} {self.matrix[0][1]}', f'{self.matrix[1][0]} {self.matrix[1][1]}']
                matrix2x2 = Matrix(*matrix2x2)
                new_row.append(str(matrix2x2.determinant()))
            mat_minors.append(' '.join(new_row))
        mat_minors = Matrix(*mat_minors)
        return mat_minors

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix)):
            new_row = []
            for j in range(len(self.matrix[i])):
                new_row.append(str(self.matrix[i][j] + other.matrix[i][j]))
            new_matrix.append(' '.join(new_row))
        return Matrix(*new_matrix)

    def __sub__(self, other):
        new_matrix = []
        for i in range(len(self.matrix)):
            new_row = []
            for j in range(len(self.matrix[i])):
                new_row.append(str(self.matrix[i][j] - other.matrix[i][j]))
            new_matrix.append(' '.join(new_row))
        return Matrix(*new_matrix)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_matrix = []
            for i in range(self.dimensions()[1]):
                new_row = []
                for j in range(self.dimensions()[0]):
                    new_row.append(str(self.matrix[i][j] * other))
                new_matrix.append(' '.join(new_row))
            return Matrix(*new_matrix)
        # check that matrices are compatible
        elif self.dimensions()[0] == other.dimensions()[1]:
            new_matrix = []

            for i in range(self.dimensions()[1]):
                new_row = []
                for j in range(other.dimensions()[0]):
                    new_row.append(str(sum([self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[i]))])))
                new_matrix.append(' '.join(new_row))

            return Matrix(*new_matrix)
        else:
            raise Not_Compatible_Error()

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__mul__(other)

    def __pow__(self, power):
        if power == -1:
            return self.inverse()
        elif power <= 0 or power % 1 != 0:
            raise Power_Not_Positive_Error()
        new_matrix = self
        for _ in range(power-1):
            new_matrix = self.__mul__(new_matrix)
        return new_matrix

    def __str__(self):
        dim = self.dimensions()
        matrix_string = ""
        if dim[1] == 1:
            matrix_string = "(" + " ".join(str(num) for num in self.matrix[0]) + ") "
        else:
            for i in range(len(self.matrix)):
                if i == 0:
                    matrix_string += " / "
                elif dim[1]-1 == i:
                    matrix_string += " \\ "
                else:
                    matrix_string += "|  "
                for j in range(len(self.matrix[i])):
                    matrix_string += str(self.matrix[i][j])
                    matrix_string += " "
                if i == 0:
                    matrix_string += "\\"
                elif dim[1]-1 == i:
                    matrix_string += "/"
                else:
                    matrix_string += " |"
                matrix_string += "\n"
        return matrix_string[:-1]

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, index):
        return self.matrix[index]

class Matrix_List(Matrix):
    def __init__(self, *mat_list):
        matrix = []
        for i in range(len(mat_list)):
            row = ' '.join(str(num) for num in mat_list[i])
            matrix.append(row)
        super().__init__(*matrix)

class Vector(Matrix):
    def __init__(self, *vector_list):
        vector = [str(num) for num in vector_list]
        super().__init__(*vector)

    def determinant(self):
        pass

    def transpose(self):
        pass

    def inverse(self):
        pass
    
    def minors(self):
        pass

    def cofactors(self):
        pass


class Not_Compatible_Error(Exception):
    def __init__(self):
        raise Exception('Matrices are not compatible')

class Power_Not_Positive_Error(Exception):
    def __init__(self):
        raise Exception('Power must be positive integer')

class Unknow_Determinant(Exception):
    def __init__(self, dimx, dimy):
        raise Exception('Cannot calculate the determinant for a {}x{} matrix'.format(dimx, dimy))

class Unknow_Inverse(Exception):
    def __init__(self, dimx, dimy):
        raise Exception('Cannot calculate the inverse for a {}x{} matrix'.format(dimx, dimy))

class No_Inverse(Exception):
    def __init__(self):
        raise Exception('The matrix does not have an inverse')

def simultaneous_eq(matrix, vector):
    if matrix.dimensions()[1] != (vector.dimensions()[1]):
        raise Not_Compatible_Error()
    else:
        new_matrix = matrix.inverse()*vector
        return new_matrix