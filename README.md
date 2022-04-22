# Matrix-class
A class for storing matrices
Can also be used to solve simultaneous equations in matrix form

Input a matrix string separating each value with a space
Each row is separated by a new string

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
    inverse = mat1.inverse()
    print(inverse)
