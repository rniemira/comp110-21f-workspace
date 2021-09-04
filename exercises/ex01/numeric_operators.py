"""Practicing concatenation with numeric operators."""

__author__ = "730329962"

Left: str = input("Left-hand side: ")
Right: str = input("Right-hand side: ")
x = int(Left)
y = int(Right)
raise_to_power = str(x ** y)
divide = str(x / y)
divide_integer = str(x // y)
modulus = str(x % y)
print(Left + " ** " + Right + " is " + raise_to_power)
print(Left + " / " + Right + " is " + divide)
print(Left + " // " + Right + " is " + divide_integer)
print(Left + " % " + Right + " is " + modulus)