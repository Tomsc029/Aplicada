#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde'] # Crea una lista con 6 colores
#input()
print(my_lista) # Muestra la lista completa
print(type(my_lista)) # type() nos dice qué tipo de dato es la variable (en este caso será <class 'list'>)
print(my_lista[2]) # Muestra el color o elemento en la posicion 2 (se empieza a contar desde el 0)

# len() nos da el número total de elementos en la lista
print("my_lista size: ", len(my_lista))  # Imprime 6 
# REBANADAS (SLICING): obtener una porción de la lista
print(my_lista[0:2])  # Elementos desde posición 0 hasta 1 (el 2 se excluye)
                      # Esto imprime: ['Rojo', 'Azul']
print(my_lista[:2])   # Igual que arriba: desde el inicio hasta posición 1
                      # Si omites el número antes de :, empieza desde 0
my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista) # Muestra la lista completa con el nuevo elemento 

my_lista.insert(3, 'Negro')  # Agrega un elemento en la posición indicada 
print(my_lista) # Muestra la lista completa con el nuevo arreglo

# extend() agrega VARIOS elementos de otra lista al final
# Es como append() pero para múltiples elementos a la vez
my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista) # Muestra la lista completa

print(my_lista.index('Azul')) # .index() nos dice EN QUÉ POSICIÓN está un elemento

#my_lista.remove('Magenta')
my_lista.remove('Marron')  # Elimina la primera aparición de Marron
print(my_lista) # Muestra la lista completa

my_lista.insert(8, 'Marron') # Agrega un elemento en la posición indicada
print(my_lista) # Muestra la lista completa

print(my_lista.pop()) # pop() elimina y RETORNA el último elemento de la lista
size = len(my_lista) # Calcular el nuevo tamaño de la lista
print("size = ", size)  # Muestra el tamaño de la lista
#print(my_lista.pop(size))

my_lista_3 = my_lista*3 # Multiplicar una lista por un número crea una nueva lista con los elementos repetidos
print("my_lista_3: ", my_lista_3) # Muestra mi_lista_3

print("Sort:") # sort() modifica la lista original y retorna None
print()
my_listaSort = my_lista.sort() # sort() retorna None, no la lista ordenada
print(my_listaSort) # MUestra my_listaSort

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1] # Crear lista de números para demostrar ordenamiento
print("Ordering my_NumList: ") 
my_NumList.sort() # Ordenar de menor a mayor (orden ascendente)
print(my_NumList) 
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)








#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)