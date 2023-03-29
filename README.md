# Quaternionic python: a (small) Python 3.11 resource
### Perform quaternionic arithmetic easily in Python

:dragon: Author: Samuele Ferri (@ferrixio)

:star: Version 2.2.2

:scroll: Check [this useful file](https://github.com/ferrixio/Quaternionic-beasts/blob/main/How%20to%20assemble%20a%20quaternion.md) and [this other file](https://github.com/ferrixio/Quaternionic-beasts/blob/main/How%20to%20plot%20quaternions.md).

## TABLE OF CONTENTS 

1. [FEATURES](#1-features)
2. [HOW TO USE](#2-how-to-use)
3. [KNOWN ISSUES](#3-known-issues)
4. [FUTURE IDEAS](#4-future-ideas)
5. [DESCRIPTION](#5-description)
6. [CHANGELOG](#6-changelog)


## 1. FEATURES

This class allows user to emulate quaternionic algebra in Python. The class can do:

	> internal and external sums
	> scalar multiplications
	> internal left-multiplications
	> internal right-multiplications
	> integer powers
	> divisions
	> floordivisions
	> modulos
	> normalizations
	> conjugations
	> inversions
	> algebric prints
	> type casting (int, float, complex)
	> random generations
	> exponential and logarithmic functions
	> dot product, cross product and commutator
	> extraction or generation from 3D rotations
	> rotate points in 3D
	> plotting quaternions

I used mostly magic methods to allow users to write `x+y`, `x*y`, `x/y`, ..., directly.

I recommend reading [this file](https://github.com/ferrixio/Quaternionic-beasts/blob/main/How%20to%20assemble%20a%20quaternion.md) to better understand how to construct a quaternion.

Every value below 1e-13 is treated as 0, especially during logical checks. This does NOT imply that the value is set to 0!

I'm coding the class `Hplot` to plot quaternions in different ways. Also, I invite you to read [this file](https://github.com/ferrixio/Quaternionic-beasts/blob/main/How%20to%20plot%20quaternions.md) to have an idea of how I decide to plot them. 

## 2. HOW TO USE

Open the file `test_me.py` and try it, or simply copy and paste the class in the file you want to use and then import it. (Don't forget to __cite me__ if you are using this in a project!)

## 3. KNOWN ISSUES

+ The in_place operations +=, -=, *= and so on, don't work if on the left side there isn't a quaternion.
+ There is a little chance that the method `Hplot.__getColors` returns negative numbers.

## 4. FUTURE IDEAS

+ :o: Add colorbar in plot to represent the real parts
+ :o: Study the topology of lists of quaternions
+ :white_check_mark: Vector representation
+ :white_check_mark: Add complex compatibility
+ :white_check_mark: Quaternionic functions
+ :white_check_mark: Floor division
+ :white_check_mark: Add @ operator
+ :white_check_mark: Plotting quaternions
+ :white_check_mark: Autogeneration of versors
+ :white_check_mark: Literally use LaTeX to write the .md files
+ :warning: Implementing rotation of 3D objects
+ :warning: Create a library

### Legend:
:o: = solution not (yet) found

:white_check_mark: = solution found and implemented

:warning: = solution found but the implementation needs to be improved

## 5. DESCRIPTION

The [quaternion number system](https://en.wikipedia.org/wiki/Quaternion) is an extended version of the complex numbers, firstly introduced by Rowan Hamilton in 1843. A quaternion is a 4-tuple of informations $q := a + bi + cj + dk$, where $a$, $b$, $c$, $d$ are real numbers, and $i$, $j$, $k$ are the basic quaternions.

Instead of having a single imaginary part, as a complex number, quaternions have three imaginary parts, that is, there are three elements, namely $i$, $j$ and $k$, such that
$$i^2 = j^2 = k^2 = ijk = -1$$

Addition works componentwise and it is commutative, and so is the scalar multiplication.
The Hamilton product, that is the multiplication between two quaternions, follows the expression:

$$
\begin{align*}
	(a_1 + b_1i + c_1j + d_1k)*(a_2 + b_2i + c_2j + d_2k) &= a_1a_2 - b_1b_2 - c_1c_2 - d_1d_2 \\
	&+ (b_1a_2 + b_1a_2 + c_1d_2 - d_1c_2)i \\
	&+ (a_1c_2 - b_1d_2 + c_1a_2 + d_1b_2)j \\
	& + (a_1d_2 + b_1c_2 - c_1b_2 + d_1a_1)k
\end{align*}
$$

and sadly it is not commutative since $ij = k$, $ji = -k$, $jk = i$, $kj = -i$, $ki = j$, $ik = -j$.

This set is denoted with the letter $\mathbb{H}$.

## 6. CHANGELOG

### Version 2.2.2

Added the subclass `Versor(Quaternion)` to build unitary quaternion directly.

Corrected a type error in `Hplot.__stereo_prj`

Fixed a bug in `Quaternion.__init__` which doesn't create the attribute `ACCURACY` when a quaternion is build with an iterable.

Added the method `Hplot.getPath` to get a matrix of connections among quaternions in `pathplot`.

### Version 2.2.1

Added the multiprocessing in `Hplot`. Edited some strings.

Now `pathplot` draws multiple segments if a quaternion is in the middle between two or more. Added the plots using stereographic projections.

### Version 2.2
Removed the possibility to set strings as parameters.

Added more descriptions in functions and typing. Added the possibility to set the accuracy using the standard initializator. 

Change the output of `rotation` function.

Created the class `Hplot` to plot quaternions in three ways: 3D-colored points, mutual distances, 3D-colored points connected according to the minimal mutual distance.

### Version 2.1.8
Extended the random number generator to float numbers. Renamed `random` to `random_unit` and `randint` to `random`.

Added the variable `ACCURACY` to easily handle the floating point during logical checks. The user can edit it with the method `change_bound`.

### Version 2.1.7
Implemented some elements of 3D geometry. Added the property `rotation` which returns a tuple with the four elements of a rotation: the angle and the 3D axis. By the equivalence `3D rotation == versor quaternion`, the method automatically normalizes the quaternion if it is not unitary (and raises a warning to the user).

Added the classmethod `from_rotation()` which generates a quaternion from a rotation.

### Version 2.1.6
Corrected the // and % operations. In the real numbers, `x / y = (k, r)`, where `k = x // y` is the quotient and `r = x % y` is the reminder. Since in H this kind of operations don't exist, I move the problem in HP1 and look for two quaternions `k` and `r` such that the previous relation is fullfilled. With this method, `k` belongs to the same equivalence class of `q` in HP1, that is, it lies on the same line that starts from the origin and passes through `q`.

Added the magic method `__matmul__`: `x @ y` performs an homotethy on x to the sphere of radius y.

Fixed a little bit of floating point in `__bool__`, `__eq__` and `__str__`.

### Version 2.1.5
Added // operation. x // y performs an homotethy of x to a quaternion with norm y.
Changed the default decimals of `round()` to 3.

Added the classmethod `randint()`, that generates a random quaternion with integer values.

Fixed a bug in `random()` method.

### Version 2.1.4
Added modulo operation %.

### Version 2.1.3
Minor change: used `isinstance()` instead of `type()`.

### Version 2.1.2
Added the method `check_other` to handle with unsupported type errors in arithmetic.

### Version 2.1.1
Added geodesic distance calculator. Riarranged the code in a more understandable way. Discovered the floating point issue in random number generator.

### Version 2.1
Added dot/cross product, commutator and exponential/logarithmic function.

### Version 2.0.1
Corrected a type error in the using of property `norm`. Removed methods `__floor__` and `__ceil__`.

### Version 2.0
Major changes in everything. Now the object quaternion is initialized with the list of its components. A quaternion can be built from four numbers, from a list, from a tuple or from a complex number, using the classmethod `from_complex`. In the latter case, the user can specify which quaternion-imaginary part is the complex-imaginary one. The optional argument `to_real` has been removed.

Added the classmethod `random()`, that generates a uniformly random unitary quaternion.

Now, the real part, i, j, k and the norm are defined as `properties` of the Quaternion. Added the property `vector` to return the list of imaginary parts of the Quaternion.

Every operation is compatible with complex numbers.

Added the conversion from Quaternion to complex number. Added `__repr__` magic method.

Boolean magic methods have been improved, and the methods `is_real` and `is_imagy` have been added.

### Version 1.6.1
Minor changes. Added the method `is_real` to check if a quaternion is a real number.

### Version 1.6
The norm method evaluate the square-root using math.sqrt (more accuracy and time-saving).
Added an optional argument `to_real` in the initialization of the quaternion. If it is True, the creation returns real_part as int/float number; this means that the item lives outside from the class Quaternion. 
Added

```py
__int__ 	== to cast a quaternion in integer
__float__ 	== to cast a quaternion in float
```

### Version 1.5.2
Minor bug fixed (again).

### Version 1.5.1
Minor bug fixed (arised after the implementation of `__new__`).

### Version 1.5
Minor bug fixed. Added the magic method `__new__` to return real numbers when `Quaternion(x,0,0,0)` is initialized.

### Version 1.4

Minor bug fixed. Added right sum and subtraction. Added the method `__inverse_ip__`, that inverse the quaternion in place. Changed the name of conj to conjugate_ip.

### Version 1.3

Minor changes, saved some computational cost (thx to @Scarlet06).

### Version 1.2

Lowered execution time for all operations, removed `__scalarProduct__` and `__algebricPrint__` (thx to @Scarlet06).

### Version 1.1

Minor changes in the boolean magic methods (thx to @Scarlet06).

### Version 1.0

Created the class Quaternion. It stores four elements: the real part and the three imaginary parts i, j, k.
Build-in methods (ordered by utility):

+ Components:
Returns a 4-tuple with the components of the quaternions.

+ Algebric print:
Prints the algebric form of the quaternion, that is a+bi+cj+dk. The magic method `__str__` calls this function to see it writing `print(x)` directly.

+ Norm:
Returns the norm of the quaternion. The magic method `__abs__` grants user to get the norm writing `abs(x)`.

+ Normalize:
Returns the normalized quaternion.

+ Conj and Conjugate:
Conjugates quaternion, that is, if q = a+bi+cj+dk, then q* = a-bi-cj-dk. Moreover, x.conj().conj() = x.

+ Inverse:
Returns the inverse quaternion, that is, a quaternion h such that qh=hq=1. The magic method __inverse__ allows the user to get the inverse writing ~x.

+ Internal sum:
Componentwise sum between quaternions. Also there are the magic methods

```py
__add__ 	== x + y
__iadd__ 	== x += y
__sub__ 	== x - y
__isub__	== x -= y
```

+ Scalar product:
Performs componentwise scalar multiplication.

+ Multiplications:
Since multiplication between quaternions is not commutative, I have to distinquish between left and right multiplication. If the second argument of the multiplication is a scalar number, they return the standard scalar product. Magic methods:

```py
__mul__		== x * y
__rmul__	== y * x
__imul__	== x *= y
__pow__		== x ** c, where c is an integer
__ipow__	== x **= c, where c is an integer
```

+ Division:
Performs left-division between quaternions, that is, x / y = x * y^-1. Magic methods:

```py
__truediv__	== x / y
__itruediv__	== x /= y
```

+ Booleans methods:
is_unit		== checks if the quaternion has norm 1. Magic methods:

```py
__eq__		== performs the componentwise check x == y
__ne__		== performs the componentwise check x != y
__bool__	== checks if the quaternion is non zero
```

+ Unary operations:

```py
__pos__		== performs unary operation +x
__neg__		== returns -x, that is, -a-bi-cj-dk (it's not the conjugate!)
__round__	== rounds quaternion's decimals
__floor__	== applies floor to each components of the quaternion
__ceil__	== applies ceil to each components of the quaternion
```
