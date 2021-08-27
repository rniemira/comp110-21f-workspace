"""Practicing concatenation with relational operators."""

__author__ = "730329962"

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
x = int(left)
y = int(right)
less_than = str(x < y)
greater_or_equal = str(x >= y)
equal = str(x == y)
not_equal = str(x != y)
print(left + " < " + right + " is " + less_than)
print(left + " >= " + right + " is " + greater_or_equal)
print(left + " == " + right + " is " + equal)
print(left + " != " + right + " is " + not_equal)