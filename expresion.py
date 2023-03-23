import numpy as np
from sympy import *
import matplotlib.pyplot as plt
x,y,z,t,j,k = symbols('x y z t j k') 

print("Hola Ismael")
expr = (5*x)/(sqrt(1+2*x**2))
print(latex(expr))
expr_latex = latex(expr)
integral_latex = latex(Integral(expr, x))
print(integral_latex)

preview("$$"+integral_latex+"$$", viewer='file', filename='imag1.png',dvioptions=['-D','400'])

solve = integrate(expr,x)
solve_latex = latex(solve)
print(solve_latex)

preview("$$"+solve_latex+"$$", viewer='file', filename='imag2.png',dvioptions=['-D','400'])

print("----------------------------------")

#x = solve_latex.replace("2", "3",1)
#print(x)
#preview("$$"+x+"$$", viewer='file', filename='imag3.png',dvioptions=['-D','400'])

print("----------------------------------")
contend = solve.args
print("len contend: ",len(contend))
for i in contend:
   print(latex(i))
   subcontend = i.args
   print("len subcontend: ",len(subcontend))
   for j in subcontend:
   	print(latex(j))
   	print("******")
   print("++++")
print("----------------------------------")

numbers = {atom for atom in solve.atoms() if atom.is_number}
for i in numbers:
	print(latex(i))
	
#preview("$$"+r+"$$", viewer='file', filename='imag1.png',dvioptions=['-D','400'])
