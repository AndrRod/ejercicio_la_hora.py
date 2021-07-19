# CASO 5
# Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada indicando: los tres atributos, sólo la hora y minuto,o sólo la hora. Crear además los métodos necesarios para modificar la hora en cualquier momento de forma manual. Mantenga la integridad de los datos en todo momento definiendo de tipo “private”. Crear  una  clase prueba_tiempo que  prueba  una  hora  concreta  y  la  modifique  a  su  gusto  mostrándola  por pantalla.

import datetime as d
import time as t
import random as r



import os



if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"

os.system(var)  



class Tiempo():
    def __init__(self, hora = t.strftime('%H', t.localtime()), minuto = t.strftime('%M', t.localtime())):
        self._hora, self._minuto, self._segundo = hora, minuto, t.strftime('%S', t.localtime())

    def __str__(self):
        return f'La hora es: {self._hora} : {self._minuto} : {self._segundo}'



class prueba_tiempo():
    def __init__(self):
        self._hora = r.randint(0, 24)
        self._minuto = r.randint(0, 60)
        self._segundo = r.randint(0, 60)
        self.tiempo = t.strftime(f'{self._hora} : {self._minuto} : {self._segundo}', t.localtime())
    def __str__(self):
        return f'La hora al azar es: {self.tiempo}'

def Digito_o_Espacio(cadena):
    while cadena.isalpha():
        cadena = input('ingrese un número: ')
    return cadena


prueba_hora = prueba_tiempo()
# print(prueba)



while True:
    opciones = input('Elija una opcion: \n\t1. Mostrar la hora que quiera. \n\t2. Mostrar una hora al azar. \n\t3. Salir\n\n')
    prueba_hora = prueba_tiempo()
    if opciones == '1':
        print('para ver la hora actual dejar vacio los campos: \n')
        hora = Digito_o_Espacio((input('Ingrese hora: ')))
        minuto = Digito_o_Espacio((input('Ingrese minuto: ')))
        

        if hora != '':
            hora = int(hora)
        if minuto != '':
            minuto = int(minuto)

        
        
        if hora == '' and minuto == '':
            horario = Tiempo()
            print(horario, '\n\n')
        elif minuto == '':
            horario = Tiempo(hora, t.strftime('%M', t.localtime()))
            print(horario, '\n\n')
        elif hora == '':
            horario = Tiempo(t.strftime('%H', t.localtime()), minuto)
            print(horario, '\n\n')
        else:
            horario = Tiempo(hora, minuto)
            print(horario, '\n\n')

    elif opciones == '2':
        print(prueba_hora, '\n\n')
    elif opciones== '3': 
        print('Vuelta pronto. Muchas gracias')
        break

    else: print('No existe la opcion vuelva a intentarlo')
    t.sleep(3)
    os.system(var)          