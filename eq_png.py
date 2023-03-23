import numpy as np
from sympy.plotting import plot,PlotGrid
from sympy import *
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy.parsing.latex import parse_latex
import io
from io import BytesIO
import os
from os.path import join
import shutil
import tempfile
from PIL import ImageTk, Image  
x,y,z,t,j,k = symbols('x y z t j k') 


def c_Numerador(a,b,c,d):
   return Add(Mul(Integer(a), Pow(Symbol('x'), Integer(3))),Mul(Integer(b), Pow(Symbol('x'), Integer(2))),Mul(Integer(c), Pow(Symbol('x'), Integer(1))),Mul(Integer(d), Pow(Symbol('x'), Integer(0))))

def c_Denominador(b,c,d,e):
   return Add(Mul(Integer(b), Pow(Symbol('x'), Integer(3))),Mul(Integer(c), Pow(Symbol('x'), Integer(2))),Mul(Integer(d), Pow(Symbol('x'), Integer(1))),Mul(Integer(e), Pow(Symbol('x'), Integer(0))))

def det_signo(cadena):
   signo = ''
   words = cadena.split(",") #lista
   #print(words)
   for word in words: 
      if word.startswith("Mul") or word.startswith("Add(Mul"):
         if word.find("-") < 1 :
            signo='+'
         else:
            signo =''
      else:
         signo='+'
      break
   return signo 


def limpiar_signo():
   str_signo = "+"
   return str_signo

def limpiar_listas():
   list_cont = []
   list_int = []
   return list_cont,list_int 

expreciones = []
integrales = []
c = []
f = []
signos= []
fin = ''
constante = '+C'
#coloque los coeficientes en orden ax^3+bx^2+cx+d,
numerador = c_Numerador(0,1,4,1) 
#b es el primer, c es el segundo y d es el ultimo parámetro
denominador = (x-1)*(x+1)*(x+3)#c_Denominador(0,1,-2,-3)
fraccion = numerador/denominador
#preview(fraccion, viewer='file', filename='imag1.png',dvioptions=['-D','300'])
fracciones_parciales = apart(fraccion)
#preview(fracciones_parciales, viewer='file', filename='imag2.png',dvioptions=['-D','300'])


contenido = fracciones_parciales.args
for i in contenido:
   expreciones.append(i)
   print(latex(i))
print('------------------------')
for i in range(len(expreciones)):
   for j in range(len(expreciones[i].args)):
      if (j%2)==0:
         c.append(expreciones[i].args[j]) #0,2,4
         print(latex(expreciones[i].args[j]))
         #print(type(expreciones[i].args[j]))

print('------------------------')
for i in range(len(expreciones)):
   for j in range(len(expreciones[i].args)):
      if(j%2)==1:
         f.append(expreciones[i].args[j])#1,3,5
         print(latex(expreciones[i].args[j]))
         #print(type(expreciones[i].args[j]))

print('------------------------')
print('cosntates')
print(latex(c))

print('------------------------')
print('funciones')
print(latex(f))
print('------------------------')
for i in range(len(c)):
   if(c[i]>0):
      signos.append('+')
   else:
      signos.append(' ')

print("Fracciones parciales")
r =' '
for i in range(len(c)):
   #d = c[i]*f[i]
   if(i == 0 and c[i]>0):
      r = r + latex(c[i])+latex(f[i])
   elif(i == 0 and c[i]<0):
      r = r + latex(c[i])+latex(f[i], x)
   else:
      r = r + signos[i]+latex(c[i])+latex(f[i])

print(r)

preview("$$"+r+"$$", viewer='file', filename='imag1.png',dvioptions=['-D','400'])

print("Las integrales a realizar son: ")

funcion =' '
for i in range(len(c)):
	#d = c[i]*f[i]
   if(i == 0 and c[i]>0):
      funcion = funcion + latex(c[i])+latex((Integral(f[i], x)))
   elif(i == 0 and c[i]<0):
      funcion = funcion + latex(c[i])+latex((Integral(f[i], x)))
   else:
      funcion = funcion + signos[i]+latex(c[i])+latex((Integral(f[i], x)))

print(funcion)

preview("$$"+funcion+"$$", viewer='file', filename='imag2.png',dvioptions=['-D','400'])

print('------------------------')
print("integrando")
for i in range(len(c)):
   #d = c[i]*f[i]
   integrales.append(integrate(f[i],x))


solve =' '
for i in range(len(c)):
   #d = c[i]*f[i]
   if(i == 0 and c[i]>0):
      solve = solve + latex(c[i])+latex(integrales[i])
   elif(i == 0 and c[i]<0):
      solve = solve + latex(c[i])+latex(integrales[i])
   else:
      solve = solve + signos[i]+latex(c[i])+latex(integrales[i])

print(solve)

preamble = r'\renewcommand{\log}{\mathrm{\,ln\,}}'+'\n'
preamble = preamble +'\n'+ r'\renewcommand{\sin}{\mathrm{\,sen\,}}'+'\n'

preview(preamble+"$$"+solve+"$$", viewer='file', filename='imag3.png',dvioptions=['-D','400'])#,extra_preamble = preamble)
#preview(preamble+"$$"+solve+"$$", outputTexFile="eq.tex")

#from sympy import sin
#extra_preamble = r"\frac{1}{x^2}"
#preview(sin(x), output='png', extra_preamble=extra_preamble)
#preview(expr, viewer='file', filename='imag.png',dvioptions=['-D','300'])
#preview(expr, viewer='file', filename='water.png', euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600", "-bg", "Transparent"])
#preview(expr, output = "png",viewer='file',filename='imag.png',dvioptions=['-D','300'])
'''
for i in f:
   integrales.append(integrate(i))

'''
#preview(expr, viewer='file', filename='imag.png',dvioptions=['-D','300'])

