# Matrix-class
A class for storing matrices
Can also be used to solve simultaneous equations in matrix form

## Matrix
The standard class for matrices
Input a matrix string separating each value with a space
Each row is separated by a new string

## Matrix_List
This class allows matrices to be entered as a series of lists
This inherits all other functions from the Matrix class.

## Functions
- dimensions -> tuple (returns the dimensions of the matrix)
- determinant -> float (calculates the determinant)
- transpose -> Matrix (transposes the matrix)
- inverse -> Matrix (finds the inverse of the matrix. Can also be called with **-1)
- cofactors -> Matrix (finds the matrix of cofactors)
- minors -> Matrix (finds the matrix of minors)

Standard functions such as +-* can also be used

## Example
    mat1 = Matrix("1 2 2", "4 5 6", "7 8 9")
    mat2 = Matrix_List([1, 2, 2], [4, 5, 6], [7, 8, 9])
    inverse1 = mat1.inverse()
    inverse2 = mat2.inverse()
    inverse1 == inverse2  # Is True
    print(inverse1)
