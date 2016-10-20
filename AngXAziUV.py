
# -*- coding: cp1252 -*-
import csv,math,numpy as np
from Tkinter import *

# Leitura dos dados
local='c:\\Users\\projetos\\Downloads\\'
#lendo a lista da serie de dados do mapa base
entrada='u10_v10-23.25 -42.75.txt'#tkSimpleDialog.askstring('Pybat','Arquivo de batimetria')
ini=local+entrada # somando os endereços

dados=csv.reader(open(ini),delimiter='\t',lineterminator='\n')
linhas=[]
resultado=[]
for i in dados: #filtragem inicial
    linhas.append(i)

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)

   def state(self):
      return map((lambda var: var.get()), self.vars)

if __name__ == '__main__':
   root = Tk()
   root.title('x')
   input = Checkbar(root,['U,V','AnguloX','Azimute']) #!!!!restringe a area para os pontos de interesse
   output = Checkbar(root,['U,V','AnguloX','Azimute']) #!!!!restringe a area para os pontos de interesse
   input.pack(side=TOP,  fill=X)
   output.pack(side=TOP,  fill=X)
   input.config(relief=RIDGE, bd=5)
   output.config(relief=RIDGE, bd=5)
#   def allstates():
#      print(list(lon.state()), list(lat.state()))
   Button(root,text='OK', command=root.destroy).pack(side=BOTTOM)
   root.mainloop()



for i in range(1,len(linhas)):
    if np.rad2deg(np.arctan2(float(linhas[i][2]),float(linhas[i][1])))>=0:
        AngX=np.rad2deg(np.arctan2(float(linhas[i][2]),float(linhas[i][1])))

    else:
        AngX=360+np.rad2deg(np.arctan2(float(linhas[i][2]),float(linhas[i][1])))
    if (270-AngX)>0:
        Az=270-AngX
    else:
        Az=360+270-AngX
    Intens=(float(linhas[i][2])**2+float(linhas[i][1])**2)**0.5
    resultado.append([linhas[i][0],AngX,Az,Intens])
arq_saida=open(local+'AngXAzi'+entrada+'.txt','w')
saida=csv.writer(arq_saida,delimiter='\t',lineterminator='\n')
saida.writerow(['t','AngX','Azimute','Intensidade'])
for n in resultado:
    saida.writerow(n)
arq_saida.close()