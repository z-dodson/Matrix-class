# Matrix-class
A class for storing matrices  

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
```python
mat1 = Matrix([1, 2, 2], [4, 5, 6], [7, 8, 9])
mat2 = Matrix_string("1 2 2", "4 5 6", "7 8 9")
inverse1 = mat1.inverse()
inverse2 = mat2.inverse()
inverse1 == inverse2  # True
print(inverse1)
```

## Vectors
Vectors function in a similar way to matrices. There are no dedicated vector functions, but they can be used like a matrix

## Simultaneous Equations
Can solve simultaneous equations if given in matrix form. E.g.
```
x + y - z = 1
8x + 3y -6 = 1
-4x -y + 3z= 1

|‾ 1 1 -1 ‾|   |‾ x ‾|   |‾ 1 ‾|
|  8 3 -6  | * |  y  | = |  1  |
|_-4 -1 3 _|   |_ z _|   |_ 1 _|
```
```python
mat = Matrix([1, 1, -1],
             [8, 3, -6],
             [-4, -1, 3])

vec = Vector([1, 1, 1])

ans = simultaneous_eq(mat, vec)
print(ans)
```
Output:
```
|‾ 2.0 ‾|
|  3.0  |
|_ 4.0 _|
```

## Colaborators
Please create a new branch for any changes
