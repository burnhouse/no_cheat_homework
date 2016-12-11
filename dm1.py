# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:58:56 2016

@author: user
"""
import random
import os


def decompose (n): 
    liste=[]
    i=2 
    while n>1: 
        while n%i==0: 
            liste.append(i)
            n=n/i
        i=i+1
    print(liste) #saut de ligne 
    return liste

class Exercice1:
    
    
    def __init__(self,nom_):
        #define all the parameters that will be written in the homework
        self.nom=nom_
        self.pourcent_prioritaire=""
        self.num_pair=""
        self.deno_pair=""
        self.pourcent_impair=""
        self.tot_vehi=""
        
        self.sta=""
        self.stb=""
        
        self.case1=""
        self.case2=""
        self.case3="" 
        self.case4=""
        self.case5=""
        self.case6=""
        self.case7=""
        self.case8=""
        
        self.numeropairpourcent=""
        self.pa=""
        self.pb=""
        self.ainterb=""
        self.nbaunionb=""
        self.paunionb=""
        self.probainterdit=""
        
        self.ccase1=""
        self.ccase2=""
        self.ccase3=""
        self.ccase4=""
        self.ccase5=""
        self.ccase6=""
        
        self.probaste=""
        
        
        
    def lire_save(self,ligne,classe):
        
        #read the parameters form the save file
        save_file=open(classe,'r')
        save_file=save_file.read().split('\n')
        
        self.nom=save_file[ligne]
        print save_file[ligne]
        self.sta=int(save_file[ligne+1])
        self.stb=int(save_file[ligne+2])
        self.pourcent_prioritaire=int(save_file[ligne+3])
        self.num_pair=int(save_file[ligne+4])
        self.deno_pair=int(save_file[ligne+5])
        self.pourcent_impair=int(save_file[ligne+6])
        self.tot_vehi=int(save_file[ligne+7])
        
        corec='dmm_correc_'
        #write the anwser sheet
        self._set_correc(corec)
        
        
    def _set_correc(self,corrige):
        
        corrig=open(corrige,'a')
        
        #write the parameters of the answer sheet
        self.case7=self.pourcent_prioritaire*self.tot_vehi/100
        self.case4=self.pourcent_impair*self.case7/100
        self.case1=self.case7-self.case4
        self.case8=self.tot_vehi-self.case7
        self.case2=self.case8*self.num_pair/self.deno_pair
        
        self.case5=self.case8-self.case2
        
        
        self.case3=self.case1+self.case2
        self.case6=self.tot_vehi-self.case3
        
        
        self.pa=float(self.pourcent_prioritaire)/100   
        self.numeropairpourcent=100-self.pourcent_impair
        self.pb=float(int(100*float(self.case3)/self.tot_vehi))/100
        
        self.ainterb=float(self.case1)/float(self.tot_vehi)
        
        
        self.nbaunionb=self.case1+self.case4+self.case2
        self.paunionb=float(int(100*float(self.nbaunionb)/self.tot_vehi))/100
        
        self.probainterdit=float(int(100*float(self.case2)/self.tot_vehi))/100
        
        self.ccase1=float(int(100*40*float(self.sta)/100))/100
        self.ccase3=float(int(100*60*self.stb/100))/100
        
        self.ccase2=40-self.ccase1
        self.ccase4=60-self.ccase3
        
        self.ccase5=self.ccase1+self.ccase3
        self.ccase6=100-self.ccase5
        
        self.probaste=self.ccase5/100
        
        #open the template of the answer sheet
        template=open('correction_temp','r')
        template=template.read()
        #writite the answers
        template=template.format(nom=self.nom,\
            case1=self.case1,\
            case2=self.case2,\
            case3=self.case3,\
            case4=self.case4,\
            case5=self.case5,\
            case6=self.case6,\
            case7=self.case7,\
            case8=self.case8,\
            prioritair=self.pourcent_prioritaire,\
            numeroimpair=self.pourcent_impair,\
            numeropairpourcent=self.numeropairpourcent,\
            pa=self.pa,\
            pb=self.pb,\
            cent='[100]',
            nbcasfavo="[nombre-de-cas-favorables]",\
            nbtot="[nombre-de-cas-total]",\
            ainterb=self.ainterb,\
            nbaunionb=self.nbaunionb,\
            paunionb=self.paunionb,\
            probainterdit=self.probainterdit,\
            c2case1=self.ccase1,\
            c2case2=self.ccase2,\
            c2case3=self.ccase3,\
            c2case4=self.ccase4,\
            c2case5=self.ccase5,\
            c2case6=self.ccase6,\
            stea=self.sta,\
            steb=self.stb,\
            totalvehicule=self.tot_vehi,\
            probaste=self.probaste)
        #replace [ by { for the latex lyx
        template=template.replace("[","{")
        template=template.replace("]","}")
        #write to the fuul sheet
        corrig.write(template)
        corrig.close()
        
        
    def _set_param(self):
        #trouve un nombre de véhucule entre 3000 et 54 000
        self.tot_vehi=random.randint(3,54)*1000
        
        #trouve le pourcentage de vehicules prioritaires
        self.pourcent_prioritaire=2*random.randint(1,4)
        
        #cherche le denominateur de la fraction des non prio
        toto=decompose(self.tot_vehi-self.pourcent_prioritaire*self.tot_vehi/100)
        deno=1
        index_alea=random.randint(1,len(toto)-1)
        index_alea2=random.randint(1,len(toto)-1)
        deno=toto[index_alea]*toto[index_alea2]
        self.deno_pair=deno
        self.num_pair=random.randint(1,deno/2)
        
        #poucentage de impair
        self.pourcent_impair=50
        
        #correction exo1
        self.case7=self.pourcent_prioritaire*self.tot_vehi/100
        self.case8=self.tot_vehi-self.case7
        self.case2=self.case8*self.num_pair/self.deno_pair
        self.case5=self.case8-self.case2
        self.case4=self.pourcent_impair*self.tot_vehi/100
        self.case1=self.case7-self.case4
        
        self.pa=self.pourcent_prioritaire/100
        
        
        
    def ecrire_dm(self,dm,save):
        #write the homework
        sta=str(random.randint(2,21))
        stb=str(random.randint(10,25))
        
        temp=open('template','r')
        
        debut=open('prelude','r')
        debut=debut.read()
        
        fin=open('epilogue','r')
        fin=fin.read()
        
        sav=open(save,'a')
        
        ecri=open(dm,'a')
        temp=temp.read()
        
        temp=temp.format(nom=self.nom,prioritaire=self.pourcent_prioritaire,\
                                franum='{'+str(self.num_pair)+'}',\
                                 fracdeno='{'+str(self.deno_pair)+'}',\
                                 numeroimpair=self.pourcent_impair,\
                                 totalvehicule=self.tot_vehi,\
                                 ste_A=sta,ste_B=stb)
        
        ecri.write(temp)
        
        ecri.close()
        
        sav.write(self.nom)
        sav.write('\n')
        sav.write(sta)
        sav.write('\n')
        sav.write(stb)
        sav.write('\n')
        sav.write(str(self.pourcent_prioritaire))
        sav.write('\n')
        sav.write(str(self.num_pair))
        sav.write('\n')
        sav.write(str(self.deno_pair))
        sav.write('\n')
        sav.write(str(self.pourcent_impair))
        sav.write('\n')
        sav.write(str(self.tot_vehi))
        sav.write('\n')
        sav.close()
        


#open the output 
a=open('dmm_from_list','w')
#write the lyx prologue
debut=open('prelude','r')
debut=debut.read()
a.write(debut)
a.close()

#create a save file for all the paramters for all students (safety)
b=open('savv_','w')
b.close()

#open the list of names of the students
liste_nom=open('student_list','r')
liste_nom=liste_nom.read()
liste_nom=liste_nom.split('\n')

#for every name write a sample homework
for nom in liste_nom:
    exo=Exercice1(nom)
    exo._set_param()
    exo.ecrire_dm('dmm_from_list','savv_')

#write the lyx epilogue
fin=open('epilogue','r')
fin=fin.read()
a=open('dmm_from_list','a')
a.write(fin)
a.close()



#create the output for answers
a=open('dmm_correc_','w')

#write the lyx prologue
debut=open('prelude','r')
debut=debut.read()
a.write(debut)
a.close()
#
#open the save sheet
b=open('savv_','r')
liste_nom=b.read()

cpt_ligne=0
#from the save file write the answers for every student
while(cpt_ligne<len(liste_nom.split('\n'))-24):
    print cpt_ligne
    exo=Exercice1('')
    exo.lire_save(cpt_ligne,'savv_')
    cpt_ligne+=8

#write the lyx epilogue
a=open('dmm_correc_','a')
fin=open('fin_correc','r').read()
a.write(fin)
a.close()






