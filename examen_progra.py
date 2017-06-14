# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:52:34 2017

@author: 22B
"""



from tkinter import *
import random
import time
import turtle

class App:
 
 def __init__(self, master):
        tk=Tk()
        canvas = Canvas(tk, width=640, height=480)
        canvas.pack()
        
        self.button = Button(tk, text="EJERCICIO 1 (presionar 2 veces para activar la tortuga)", fg="red",command=self.ejercicio_1) 
        self.button.pack(side=BOTTOM) 
        
        
        self.slogan = Button(tk,text="EJERCICIO 2",command=self.ejercicio_2)
        self.slogan.pack(side=BOTTOM)  
        
        
 def ejercicio_1(self):
        t=turtle.Pen()
        tk=Tk()
        canvas = Canvas(tk, width=640, height=480, bd=0, highlightthickness=0)
        canvas.pack()
        n=int(input("Ingrese el numero de lados"))
        
        if(n==3):
         
            l=int(input("Ingrese lado del triangulo"))   
            b=int(input("Ingrese la base del triangulo"))
            h=int(input("Ingrese la altura del triangulo"))
            a=((b*h)/2)
            p=l+l+l
            print("El area del triangulo es:"+str(a))
            print("El perimetro es:"+str(p))
            
            for x in range(1, 4):
                t.forward(l)
                t.left(120)
            
           
        elif (n==4):
            
              l=int(input("Ingrese lado del cuadrado"))
            
              a = l**2
              p=4*l
            
              print("El area del cuadrado es:"+str(a))
              print("El perimetro es:"+str(p))
              for x in range(1,5):
                t.forward(100)
                t.left(90)
            
        elif (n==5):
             l=int(input("Ingrese el tamaño del lado del poligono"))
             a=int(input("Ingrese el apotema del poligono "))
             
             area=((n*l*a)/2)
             
             print("El area del poligono es:"+str(area))
             for x in range (1,6):
                 t.forward(l)
                 t.left(72)
        elif (n==6):
              l=int(input("Ingrese el tamaño del lado del hexagono"))
              a=int(input("Ingrese el apotema del hexagono "))
              p=n*l
              print("El perimetro del hexagono es:"+str(p))
              ap=((p*a)/2)
              print("El area del hexagono es:"+str(ap))
              for x in range (1,7):
                 t.forward(l)
                 t.left(60)
        
 def ejercicio_2(self,canvas,color):
        print("ej 2") 
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id,245,300)
        
 def draw(self):
    self.canvas.move(self.id, 0, -1)
            
root = Tk() 
app = App(root) 
root.mainloop() 

#canvas = Canvas(tk, width=640, height=480, bd=0, highlightthickness=0)
#canvas.pack()

