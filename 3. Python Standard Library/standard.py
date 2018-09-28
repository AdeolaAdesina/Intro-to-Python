#Python comes with a standard library - referred to as batteries included

#You can gain access to the standard library using the 'import' keyword

#E.g
import module_name

#Let's use the standard library's maths module to compute square root

module.name_of_attribute
import maths
math.sqrt(81)
9

#How to find out which attribute is available for each module
help()
help(math)

#Use the space bar to scroll down and press Q to go back to the repl when you notice the factorial attribute
help(math.factorial)

math.factorial(5)
120

math.factorial(6)
720

#Let's use factorial to see how we can arrange 3 fruits from a set of 5 fruits

n = 5
k = 3

math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
10.0

from maths import factorial
factorial(n) / (factorial(k) * factorial(n - k))
10.0

from maths import factorial as fac
fac(n) / (fac(k) * fac(n - k))
10.0

#We can improve our expression by using a double forward slash //
fac(n) // (fac(k) * fac(n - k))
10