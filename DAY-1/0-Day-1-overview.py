''' 
DAY 1 :- Python basics - Variables, data types, operators 
'''

'''
VARIABLES

variables = varaibles is name that refers to a value 
varaibles can be assigned using simple syntax:
           name = value 
'''
x = 10
y = 5
name = "Adinath"
_is_valid = True      #boolean declaration
a, b, c = 1, 2, 3     # multiple assignment
x, y = y, x           # swap
PI = 3.14159          # constant by convention


'''

Data types (short)

Numbers
int — integers (-5, 0, 42)
float — floating point (3.14, 2.0)
complex — complex numbers (1+2j)

Boolean
bool — True, False

Text
str — strings: "hello", 'hi'

Binary
bytes, bytearray

Collections
list — ordered, mutable: [1,2,3]
tuple — ordered, immutable: (1,2,3) or 1,2,3
set — unordered, unique: {1,2,3}
dict — mapping: {'a':1, 'b':2}
'''

# syntax to Check type:
type(123)     # <class 'int'>
print(type([1,2]))   # <class 'list'>

# Conversions examples :
int("42")      # 42 string to int 
float("3.5")   # 3.5
str(100)       # "100"
bool(0)        # False; bool(1) -> True
list((1,2))    # [1, 2]
tuple([1,2])   # (1, 2)

'''
Operators

Arithmetic
+ - * / // % **

Examples:
5 + 2      # 7
5 - 2      # 3
5 * 2      # 10
5 / 2      # 2.5   (always float)
5 // 2     # 2     (floor division)
5 % 2      # 1     (remainder)
2 ** 3     # 8     (power)

'''

'''
Assignment
= += -= *= /= //= %= **=

Examples:
x = 5
x += 3  # x = x + 3
'''
'''
Comparison
== != > < >= <=

Examples:
3 == 3    # True
3 != 4    # True
You can chain: 1 < x <= 10.

'''

'''
Logical
and or not

Examples:
True and False   # False
not (x > 0)      # negate

'''

'''
Bitwise (operate on ints at bit-level)
& | ^ ~ << >>

Examples:
5 & 3   # 1
5 << 1  # 10

'''

'''
Membership
in, not in

Examples:
"p" in "python"     # True
3 in [1,2,3]        # True
'''

'''
Identity
is, is not — checks whether two names refer to the same object (not just equal value)

Examples:
a = [1,2]
b = a
c = [1,2]
a is b   # True
a is c   # False (equal but different object)
a == c   # True

'''