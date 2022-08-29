## EJERCICIO 01
'''
Los ejercicios son de caracter obligatorio, sin embargo no se les asignará una calificación, el objetivo de estos
es que ustedes practiquen y mejoren sus habilidades.
estos los deben subir de manera individual en su cuenta de Git
'''
'''
se les darán multiples funciones (por ahora no importa qué son), así como la documentación correspondiente
 deben completar las tareas marcadas como TODO
'''
##
def f_suma (a,b):
     a=a+b
     return a
# Se genera un error si no funciona de manera adecuada
assert f_suma(3,5) == 8
assert f_suma(3,-5) == -2
assert f_suma(-7,-5) == -12
#NOTA ESTUDIANTE: El punto ya fue completado.
## modulo

def f_mod(a,b):

    b=b%a

    return b

# Se genera un error si no funciona de manera adecuada
assert f_mod(3,5) == 2
assert f_mod(3,-5) == -1       #Fallo
assert f_mod(4,10) == 2
#NOTA ESTUDIANTE: El punto tiene un fallo en únicamente una línea (30), ya que el módulo resultante es 1 no -1.
## Cadenas de caracteres
def f_str_01 (str_01):
    str_03 = str_01.split()
    count = 1
    str_04 = []
    for i in str_03:
        if count == 2:
            ij = i.upper()
            str_04.append(ij)
        if count < 2 or count > 2:
            str_04.append(i)
        count += 1
        str_02 = "".join(str_04)
    return str_02
assert f_str_01('Hola Mundo') == 'HolaMUNDO'
assert f_str_01('tengo un dinosaurio') == 'tengoUNdinosaurio'
#NOTA ESTUDIANTE: El punto ya fue completado.