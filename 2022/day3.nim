import sugar, math, algorithm
include prelude

import rationals
var
 x1 = Rational[int](num: 1, den: 2)
 x2 = Rational[int](num: 1, den: -2)
 x3 = Rational[int](num: -1, den: 2)
 x4 = Rational[int](num: -1, den: -2)

assert &"{x1} {x2} {x3} {x4}" == "1/2 1/-2 -1/2 -1/-2"
x1.reduce; x2.reduce; x3.reduce; x4.reduce
assert &"{x1} {x2} {x3} {x4}" == "1/2 -1/2 -1/2 1/2"
