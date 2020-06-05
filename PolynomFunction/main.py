import math
import sys
import os
clear = lambda: os.system('cls')

#------------------------------#
# Quadratic Function
#------------------------------#

class QuadraticFunction:
  def __init__(self):
    self.a = float(input("coefficient a: "))
    while (self.a==0):
      print("Coefficient can not equal 0")
      self.a = float(input("coefficient a: "))
    self.b = float(input("coefficient b: "))
    self.c = float(input("constant c: "))
    self.xs = -(self.b/(2*self.a))
    self.ys = ((4 * self.a * self.c - pow(self.b,2)) / (4*self.a))
    pass


  def vertex(self):
    print("S("+str(self.xs)+"|"+str(self.ys)+")")
    print("y = " + str(self.a) + "(x -(" + str(self.xs) + "))^2 + (" + str(self.ys) + ")")
    print(input(str("Press entry to continue")))
    clear()
    pass


  def find_y(self):
    x = float(input("Coordinate x: "))
    y = self.a * pow((x),2) + (self.b*x) + (self.c)
    print("y exact: " + str(y))
    y = round(y,2)
    print("y rounded: " + str(y))
    print("the y coordinate equal: "+str(y))
    print(input(str("Press entry to continue")))
    clear()
    pass


  def PonParabel(self):
    x_input = float(input("Coordinate x: "))
    y_input = float(input("Coordinate y: "))
    x_output = (self.a * (x_input - self.xs) * (x_input - self.xs)) + self.ys
    rx_output = round(x_output, 10)
    if (y_input == rx_output): 
      print("True -> The point is on the Parabola")
      print("Because "+str(y_input)+" = "+str(x_output))
    else: 
      print("False - > The point is not on the Parabola")
      print("Because "+str(y_input)+" != "+str(x_output))
    print(input(str("Press entry to continue")))
    clear()
    pass


  def zero(self):
    D = pow(self.b, 2) - 4 * self.a * self.c
    if(D>0): 
      nL = (-self.b - math.sqrt(D))/(2*self.a)
      pL = (-self.b + math.sqrt(D))/(2*self.a)
      print ("Have two solution")
      print ("L = {"+str(nL)+"; "+str(pL)+"}")
    elif(D==0): 
      pL = (-self.b + math.sqrt(D))/(2*self.a)
      print ("Have one solution")
      print ("L = {"+str(pL)+"}")
    else: 
      print ("Solution do not exist")
      print ("L = {"+"}")
    print(input(str("Press entry to continue")))
    clear()
    pass
    

  def describeFunction(self):
    print("The Graph is a: ")
    if (self.a>1 or self.a<-1): print("stretched Parabola")
    else: print("hosed Parabola")
    if (self.a>0): print("which opens upwards")
    else: print("which opens downwards")
    print("and the Parabola is moved "+str(self.xs)+" units along the x-axis\nand "+str(self.ys)+" units along the y-axis")
    print(input(str("Press entry to continue")))
    clear()
    pass
    

  def menu(self):
    print ("\n\nQuadrictic Menu - Current Equation:  y = ("+str(self.a)+")*x^2 + ("+str(self.b)+")*x + ("+str(self.c)+")")
    print ("==============================")
    print ("1. The vertex of Parabola")
    print ("2. Find the Y-Coordinate")
    print ("3. Point on Parabola")
    print ("4. Find the Zero-Coordinates")
    print ("5. Describe the Parabola")
    print ("0. Change the Equation")
    print ("Press -1 to exit")
    print ("-----------------------------")
    choice = str(input("Select: "))
    if choice == "0":
      self.__init__
      self = QuadraticFunction()
      self.menu()
    if choice == "1":
      self.vertex()
      self.menu()
    if choice == "2": 
      self.find_y()
      self.menu()
    if choice == "3":
      self.PonParabel()
      self.menu()
    if choice == "4":
      self.zero()
      self.menu()
    if choice == "5":
      self.describeFunction()
     
      self.menu()
    if choice == "-1":
      sys.exit()
    pass


#------------------------------#
# Linear Function              
#------------------------------#

class LinearFunction:
  def __init__(self):
    self.a = float(input("A: "))
    while (self.a==0):
      print("A can not equal with 0")
      self.a = float(input("A: "))
    self.b = float(input("B: "))
    self.c = float(input("C: "))
    self.m = -self.a/self.b
    self.yb = -self.c/self.b
    pass


  def slopeForm(self):
    rm = round(self.m,2)
    ry = round(self.yb,2)
    print("rounded slope-intercept form: y = " + str(rm) + "x + (" + str(ry) + ")")
    print("exact slope-intercept from: y= " + str(self.m) + "x + (" + str(self.yb) + ")")
    print(input(str("Press entry to continue")))
    clear()
    pass


  def menu(self):
    print('Linear Menu - Curret Equation: ')
    print('1. Slope Form')
    choice = str(input("Select: "))
    if choice == "1":
      self.slopeForm()
      self.menu()
    if choice == "-1":
      sys.exit()
    pass


#------------------------------#
# Polynom of 3rd Degree        
#------------------------------#

class Poly3rd:
  def __init__(self):
    self.a = float(input(""))
    self.b = float(input(""))
    self.c = float(input(""))
    self.d = float(input(""))
  def menu(self):
    print('Polynom not available temporary')




#######################################################################
# Input #
print('Choose you Function')
print('===========================================')
print('1. Linear Function')
print('2. Quadratic Function')
print('3. Polynome of 3rd Degree')
print('-------------------------------------------')
select = int(input("Select your Polynom Degree: "))
clear()
if select == 1: 
  print("\nInitialize your Linear in General Form: ")
  print("==========================================")
  poly1st = LinearFunction()
  poly1st.menu()

if select == 2:
  print("\nInitialize your Parabole in General Form: ") 
  print("==========================================")
  poly2sd = QuadraticFunction()
  
  poly2sd.menu()

if select == 3:
  print("\nInitialize your Polynom of 3rd Degree: ")
  print("==========================================")
  poly3rd= Poly3rd()
  poly3rd.menu()




# Copyrighted 2020
# Layt-Lyffski
 