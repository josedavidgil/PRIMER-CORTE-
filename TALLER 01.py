#TALLER 01
'PRIMER PUNTO'



l_paises1 = ['Colombia','Mexico','Turquía','Polonia','serbia','dinamarca','holanda','Alemania']
l_vacia = []
txt=open('Ejercicio1.txt','w')
espacios=(', ')
for i in l_paises1:
    i=i.capitalize()
    l_vacia.append(i)
for j in l_vacia:
    ju=j+espacios
    txt.write(ju)
txt.close()


'SEGUNDO PUNTO'


variablenueva=open('Ejercicio1.txt','r')
for m in l_vacia:
    print(m)

'TERCER PUNTO'
def f_calBin (s_num):
  lista_vacia=[]
  while s_num!=0:
    mod=s_num%2
    coc=s_num//2
    lista_vacia.append(mod)
    s_num=coc
  s_bin=(lista_vacia)
  return s_bin
assert f_calBin (1) == [1]
#assert f_calBin (4) == 100            #SE MARCA ERROR DEBIDO A QUE IMPRIME EL RESULTADO AL REVÉS.
#assert f_calBin (10) == 1010
#assert f_calBin (1.25) == 1.01
'CUARTO PUNTO'
import numpy as np
import statistics

def f_stat (l_valores):
    s_mean, s_median, s_STD = 0,0,0
    s_mean=np.mean(l_valores)
    s_median=statistics.median(l_valores)
    s_STD=np.std(l_valores)
    return s_mean,s_median,s_STD
'QUINTO PUNTO'
assert f_stat([10, 10, 10])== (10, 10, 0)
assert f_stat([100, 100, 100])==(100,100,0)
assert f_stat([100, 200])==(150, 150, 50)
