# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pandas as pd
import numpy as np
from math import sqrt
import pyproj

from dbfread import DBF

lambert=pyproj.Proj("+init=EPSG:3035")

print(lambert)



longitudes=[2.875,-0.69083,5.27083,6.21806,0.17028,4.79056,0.6528,4.75667,2.51667,7.563036,-1.88167,0.84528,2.135,3.51778,0.63528,1.21194,4.75528,1.58349,4.72249]
latitudes=[47.50972,45.25611,45.79833,49.41583,47.2306,50.09,46.45667,44.63306,47.73306,47.903108,49.53639,44.10667,51.01444,48.51528,49.85778,49.97611,45.40444,47.723982,44.335698]


popCentrales_10=[]
popCentrales_20=[]
popCentrales_30=[]

# j sera le numéro de la centrale, i le numéro du carré
for j in range(19):
	print (str(longitudes[j])+ '   ' + str(latitudes[j]))
	xCentrale,yCentrale= lambert(longitudes[j],latitudes[j])
	popCentrale_j_10=0
	popCentrale_j_20=0
	popCentrale_j_30=0
	for i,record in enumerate(DBF('/Users/analutzky/Desktop/data/nucleaire/ECP1KM_09_MET/R_rfl09_LAEA1000.dbf')): # i = nombre de ligne, record = contenu de la ligne
	#	print(record) # printer la ligne qu'on lit (desactivé)
		if i>0:
			if i-10000*(i/10000)==0:
			(print i) # écrire i tous les 10000 lignes pour verifier que ca tourne
			x=record['x_laea']+500
			y=record['y_laea']+500
			pop=record['ind']
			dist=sqrt((x-xCentrale)**2+(y-yCentrale)**2)
	#		print(dist)  # printer les distances (desactivé)
			if dist<10000 :
				popCentrale_j_10=popCentrale_j_10+pop
			if dist<20000 :
				popCentrale_j_20=popCentrale_j_20+pop
			if dist<30000 :
				popCentrale_j_30=popCentrale_j_30+pop
	#	if i==10: break #là c'est pour tester pour 10
	popCentrales_10.append(popCentrale_j_10)
	popCentrales_20.append(popCentrale_j_20)
	popCentrales_30.append(popCentrale_j_30)
	print (popCentrales_10)
	print (popCentrales_20)
	print (popCentrales_30)

