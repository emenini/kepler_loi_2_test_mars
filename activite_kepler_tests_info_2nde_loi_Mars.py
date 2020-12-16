
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from math import *



pl,dates,RA,DEC,distance,H, duree,aires,rayon=[],[],[],[],[],[],[],[],[] #définition des variables temps et distance
deltaT=86400 #durée entre deux valeurs à convertir en secondes
cpt=0

#récupération des valeurs des dates, des angles (RA et DEC) et des distances du fichier .txt
with open("F:/em/CLASSES/TERMINALE/TLE_MECA/activite_kepler_tests_info_2nde_loi_Mars_data_1j.txt","r") as fichierTexte:
    i=1
    for ligne in fichierTexte :
        if i > 5:
            pli,datesi,RAi,DECi,distancei,Hi=[d for d in ligne.split(",")]
            dates.append(datesi),distance.append(float(distancei)*149.6e9),RA.append(RAi),DEC.append(DECi)
            cpt=cpt+1
        i=i+1


#conversion des angles RA, de DD:MM:SS en Dd
ddra,mmra,ssra,angleRA=[],[],[],[]
for i in range(len(RA)):
    ddrai,mmrai,ssrai = RA[i].split()
    angleRA.append(float(ddrai)+float(mmrai)/60+float(ssrai)/3600)

#fonction de calcul d'aire si on donne un angle en degrés et un rayon en m
def aire(angle,r):
    aire=(pi*angle*r**2)/360
    return aire

#fonction calculant l'aire balayée entre deux mesures successives à partir du point j pour un angle croissant
def aireDeltaT(j):
    aireBalayee=0
    if angleRA[j+1]>angleRA[j]:
        angle=angleRA[j+1]-angleRA[j]
    else:
        angle=angleRA[j]-angleRA[j-1]
    r=distance[j]*149.6e9
    aireBalayee=aire(angle,r)
    return aireBalayee

#calcul des aires, des rayons-vecteurs et des dates
for i in range(len(dates)-1):
    aires.append(aireDeltaT(i))
    rayon.append(distance[i])
    duree.append(i*deltaT)

#affichage
plt.clf
plt.figure('aires et rayons en fonction du temps')
plt.plot(duree,aires,'+',color='r',label='aire balayée \n en fonction du temps')
plt.legend(loc='center right')
plt.ylim(0,6e42)
#╠plt.ylim(0,3e11) #pour tracer le rayon (changer alors aires par rayon dans le plt.plot
plt.xlabel('durée (s)')
plt.ylabel('aires balayées pendant $\Delta$t = ' +str('{0:.2e}'.format(deltaT))+" s")
plt.show()

