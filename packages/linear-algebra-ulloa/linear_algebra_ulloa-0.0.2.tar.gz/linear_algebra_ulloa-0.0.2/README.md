# linear-algebra-ulloa
implemented vector and matrix classes with reST-formatted docstrings in Python 3+

## General Layout


    
The Vector class imitates the m x 1 vector from linear algebra and
contains many useful functions for dealing and interacting with Vectors.

Getting values directly from the vector should be done using the get(index)
function or [] operator since the comp vector location in memory may change with functions
like mag() or zero() (those which change current vector comp).

    class Vector
    
    __init__(comp)          - takes in a list of components or a valid mx1 Matrix
    
    resize(length)          - while preserving current elements or filling with 0's, changes current vector length
    
    set(comp, index=-1)     - sets entire list at once or one specific index/value
    
    get(index)              - returns item at specified index of vector
    
    zero()                  - turns the current vector into a zero vector and returns it
    
    mag()                   - returns the magnitude of current vector
    
    normalize(change=False) - returns normalized current vector, if change=True, internal vector is updated
    
    same_normalized(other)  - returns True/False depending on equality of the two vectors once normalized
    
    dot(other)              - returns the dot product of th two vectors
    
    cross(other)            - returns the cross product of u x v (u is current vector, v is other)
    
    perp(other)             - returns True/False if current and other are/aren't perpendicular
    
    parallel(other)         - returns True/False if current and other are/aren't parallel
    
    indep(other)          - returns True/False if curr vector and other vector(s) are linearly independent
    
    operator +              - returns sum of two vectors, component wise addition
    
    operator -              - returns difference of two vectors, component wise subtraction
    
    operator *              - alternate for dot product, or can use for vector scaling
    
    operator **             - returns original vector with its components raised to power
    
    operator ==             - checks to see if lists are equal
    
    to string method        - format: "<elem1, elem2, ...>"
    
    len() method            - can use len() to get vector length
    
    get and set []          - user can get and set values in vector with index based operations []

    
    comp = vector composition, list of components
    
    length = number of components in vector
    
    rows = same as length, used with cols for backwards compatibility with Matrix
    
    cols = 1 (num of columns)
    
    
The Matrix class imitates the matrix concept from linear algebra and allows
for different ways of dealing and interacting with matrices and vectors.
    
Getting values directly from the vector should be done using the get(row, col)
function or [], [][] operator since the matrix comp location in memory may change with functions
that change the underlying data type.
    
    class Matrix
  
    __init__(comp)          - takes in a list of components or a valid Vector
  
    resize(rows, cols)      - while preserving current elements or filling with 0's, changes current vector length
  
    set(comp, index=None)   - sets entire list at once or one specific index/value (tuple or array as (row, col))
  
    get(row=None,col=None)  - can get a specific row, column, or entire matrix composition (no args for matrix)
  
    zero()                  - replaces values in current matrix with all zeroes and returns it
  
    det()                   - takes the determinant of the current NxN matrix
  
    transpose()             - transposes the current mxn matrix to an nxm matrix (1st row becomes 1st col, etc.)
  
    row_echelon()           - returns the current matrix in row echelon form
  
    row_reduce()            - returns the current matrix to reduced row echelon form
  
    identity(n)             - static method that returns the nxn identity matrix
    
    combine(first, second)  - static method that combines two matrices by concatenation
    
    inverse()               - returns the inverse of current nxn matrix, or None if singular
    
    operator +              - returns sum of two matrices, component wise addition
  
    operator -              - returns difference of two matrices, component wise subtraction
  
    operator *              - matrix multiplication, matrix-vector product, scalar multiplication
  
    operator **             - returns original matrix with its components raised to power
  
    operator ==             - checks to see if internal lists are equal
  
    to string method        - format: "[row1\n row2\n row3\n ...]" and floats are shown as fractions
  
    len() method            - returns tuple formatted as (row, col)
  
    get and set [][]        - can get rows and specific values with [] or [][], and set specific values with [][]


    comp = matrix composition, list of lists where each list is a row
  
    rows = number of rows in matrix
  
    cols = number of columns in matrix
    
## Tests

There is a file for writing tests. At the moment, it is only a series of assertions. In the future, I will update the testing file to use a more standardized version/library for testing.

## Docstrings/Documentation

There is thorough documentation throughout the library. Python library contains a help() function that could be used to view the docstrings for a specific class/method.

Class: help(classname)

Method: help(classname.methodname)

For example, help(Vector.resize) shows you ...

    resize(self, length)

        Re-sizes the vector to the specified length. If length is greater than

        current size, the new components are initialized with 0, otherwise if length

        is less than current size, the last few components are lost.

        :param length: new length of vector

        :type length: int

        :return: current vector, now resized

        :rtype: Vector

and vice versa. help(Vector) and help(Matrix) return major class overviews.

## Using library

pip:
    
    pip install linear-algebra-ulloa

or 

    pip3 install linear-algebra-ulloa
    
Use

    from linear_lib.linear import *
    
to be able to create and utilize vector and matrix classes without
the linear.Vector or linear.Matrix prefix.

## Potential additions to library in future

### Vector Class

* ~~Method for checking if current vector and other vector are orthogonal~~

* Support for plotting/graphing a certain amount of 2D maybe 3D vectors using matplotlib or a similar library

* ~~Cross products~~

### Matrix Class

* ~~Determinant~~

* ~~Row Reducing Matrices~~

* ~~Finding inverse of Matrices~~

* ~~Transposing matrices~~

* Standalone function for fitting a straight line with least squares approximation

* General least squares method as part of matrices class

### Additional

* ~~index access with [] [][] operator~~

* ~~identify whether a set of vectors are linearly independent~~

* ~~identify whether two vectors are parallel~~

* ~~static method for generating arbitrarily sized identity matrix~~

* ~~static method for concatenating two matrices~~

* ~~floats are shown as proper fractions when printed~~

* ~~equality tests account for floating point error~~





