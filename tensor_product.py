from sympy import Matrix
from sympy.physics.quantum import TensorProduct

# simple tensor product
m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[1,0],[0,1]])
TensorProduct(m1,m2)
TensorProduct(m2,m1)

# tensor product non-commutative symbols
from sympy import Symbol
A = Symbol('A',commutative=False)
B = Symbol('B',commutative=False)
tp = TensorProduct(A, B)
tp

#We can take the dagger of a tensor product (note the order 
#does NOT reverse like the dagger of a normal product):

from sympy.physics.quantum import Dagger
Dagger(tp)

# expand to distribute tensor product across addition
C = Symbol('C',commutative=False)
tp = TensorProduct(A+B,C)
tp
tp.expand(tensorproduct=True)
