# Matrix-class
A class for storing matrices  

## Matrix
The standard class for matrices  
Input a matrix in a list, separating each row with a new list

### Functions
- dimensions -> tuple (returns the dimensions of the matrix)
- determinant -> float (calculates the determinant)
- transpose -> Matrix (transposes the matrix)
- inverse -> Matrix (finds the inverse of the matrix. Can also be called with **-1 or abs(matrix))
- cofactors -> Matrix (finds the matrix of cofactors)
- minors -> Matrix (finds the matrix of minors)

Standard functions such as +-* can also be used

### Example
```python
mat1 = Matrix([1, 2, 2], [4, 5, 6], [7, 8, 9])
mat2 = Matrix([2, 6, 4], [7, 3, 5], [8, 2, 5])
ans1 = mat1*mat2
ans2 = mat2*mat1
ans1 == ans2 # False
print(ans1)
```

## Vectors
Vectors function in a similar way to matrices.

### Functions
- dot -> This performs the dot product of two vectors (syntax: `vector1.dot(vector2)`)
- cross -> This performs the cross product of two vectors (syntax: `vector1.cross(vector2)`)

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
print(ans) -> |‾ 2.0 ‾|
              |  3.0  |
              |_ 4.0 _|
```
