import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import random

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
print("----------------------------------")
integers = []
for i in numbers:
   if(i.is_integer):
      integers.append(i)

for i in integers:
   print(latex(i))


print("----------------------------------")

attem = 0
flag = False
while(flag == False):# existe el numero ramdon en numbes
   gg=random.randint(0, 50)
   if(gg in integers):
      flag = True
      index = 0
      flag_while = False 
      flag = True
   attem = attem+1
   print('attem: ',attem)
   print('gg: ',gg)

print("----------------------------------")
attem = 0
while(flag_while == False):# buscamos el index
   for i in range(len(integers)):
      if(integers[i] == gg):
         print('iteration: ',i)
         print('gg=',gg, 'integers[%d]='%(i),integers[i],'OK')
         index = i
         print('index: ',index)
         flag_while = True
      else:
         print('iteration: ',i)
         print('gg=',gg, 'integers[%d]='%(i),integers[i],'Error')
   attem = attem+1
   print('attem: ',attem)



print('numbers is: ',integers[index], 'index: ',index)
old = str(integers[index])
new = str(gg*2)

if(flag== true):
   x = solve_latex.replace(old, new,1)
   print(x)
   preview("$$"+x+"$$", viewer='file', filename='imag3.png',dvioptions=['-D','400'])



#preview("$$"+r+"$$", viewer='file', filename='imag1.png',dvioptions=['-D','400'])
