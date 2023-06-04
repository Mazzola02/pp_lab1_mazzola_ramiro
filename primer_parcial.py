import re
import csv
import json
import os

with open(r"C:\Users\Ramiro\Documents\Programacion_1\PRIMER_PARCIAL\dt.json", encoding="utf-8" ) as archivo:
    data_nba = json.load(archivo)

lista_nba = data_nba["jugadores"]

def mostrar_menu():
    """
    Imprime todas las opciones del menu para que el usuario elija.
    """
    print("1. Mostrar todos los jugadores y su posicion.")
    print("2. Mostrar estadisticas de jugador.")
    print("3. Guardar las estadisticas del jugador seleccionado en un archivo CSV.")
    print("4. Buscar jugador por nombre y mostrar sus logros.")     
    print("5. Mostrar el promedio de puntos por partido de todo el equipo del Dream Team.")
    print("6. Ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.")
    print("7. Mostrar el jugador con la mayor cantidad de rebotes totales.")
    print("8. Mostrar el jugador con el mayor porcentaje de tiros de campo.")
    print("9. Mostrar el jugador con la mayor cantidad de asistencias totales.")
    print("10. Mostrar los jugadores que han promediado más PUNTOS por partido que x.")
    print("11. Mostrar los jugadores que han promediado más REBOTES por partido que x.")
    print("12. Mostrar los jugadores que han promediado más ASISTENCIAS por partido que x.")
    print("13. Mostrar el jugador con la mayor cantidad de ROBOS totales.")
    print("14. Mostrar el jugador con la mayor cantidad de BLOQUEOS totales.")
    print("15. Mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a x.")
    print("16. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
    print("17. Mostrar el jugador con la mayor cantidad de logros obtenidos.")
    print("18. Mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a x.")
    print("19. Mostrar el jugador con la mayor cantidad de temporadas jugadas.")
    print("20. Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.")
    print("1e. Mostrar la cantidad de jugadores que hay por cada posición")
    print("2e. Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.")
    print("3e. Mostrar qué jugador tiene las mejores estadísticas en cada valor.")
    print("4e. Mostrar qué jugador tiene las mejores estadísticas de todos.")
    print("0. SALIR.")

def ordenar_lista_ascendente(lista):
    """
    recibe una lista y la ordena utilizando el metodo de burbujeo.
    """
    hubo_swap = True
    while hubo_swap == True:
        hubo_swap = False
        for indice_a in range(0, len(lista)-1):
            indice_b = indice_a+1
            if lista[indice_a] > lista[indice_b]:
                aux = lista[indice_a]
                lista[indice_a] = lista[indice_b]
                lista[indice_b] = aux
                hubo_swap = True

def ordenar_lista_por_estadistica_descendente(lista,key):
    """
    Recibe la lista de jugadores y una key de las estadisticas para ordenar la lista de forma descendente
    con tal de que el jugador con la estadistica mas alta quede en primer lugar.
    """
    for indice_a in range(len(lista)):
        for indice_b in range(indice_a + 1, len(lista)):
            if lista[indice_a]["estadisticas"][key] < lista[indice_b]["estadisticas"][key]:
                lista[indice_a], lista[indice_b] = lista[indice_b], lista[indice_a]
    return lista

def ordenar_lista_dics_descendente(lista: list, clave: str):
    """
    Ordena una lista de diccionarios en orden descendente según el valor de una clave.
    Devuelve la lista ordenada utlizando el metodo de burbujeo.
    """
    for indice_a in range(len(lista)):
        for indice_b in range(indice_a + 1, len(lista)):
            if lista[indice_a][clave] < lista[indice_b][clave]:
                lista[indice_a], lista[indice_b] = lista[indice_b], lista[indice_a]
    return lista

# ---- PUNTO 1 ----
def mostrar_jugadores(lista:list): 
    """
    recibe por parametro la lista de jugadores recorre la lista por indice 
    usando un bucle for e imprime indice, nombre y posicion de cada jugador.
    """
    for indice in range(len(lista)):
        print("{}. {} - {}".format(indice, lista[indice]["nombre"], lista[indice]["posicion"]))
    
# ---- PUNTO 2 ----
def mostrar_estadisticas_por_indice(lista:list): 
    #Pide al usuario que ingrese el indice de un jugador y muestra sus estadisticas.
    while True:
        indice_jugador = input("Indicar índice de jugador (0-11): ")
        if indice_jugador.isdigit():
            indice_jugador = int(indice_jugador)
            if 0 <= indice_jugador <= 11:
                break
        print("Entrada inválida. Por favor, ingrese un número entre 0 y 11.")
    nombre_jugador = lista[indice_jugador]["nombre"]
    estadisticas_jugador = lista[indice_jugador]["estadisticas"]
    print(nombre_jugador)
    for key in estadisticas_jugador:
        key_modificada = key.replace("_", " ").capitalize()
        print("{}: {}".format(key_modificada,estadisticas_jugador[key]))

# ---- PUNTO 3 ---- 
def gurdar_estadisticas_jugador_por_indice(lista:list):
    #Permite seleccionar un jugador de la lista por su índice y guardar sus estadísticas en un archivo CSV.
    while True:
        indice_jugador = input("Indicar índice de jugador (0-11): ")
        if indice_jugador.isdigit():
            indice_jugador = int(indice_jugador)
            if 0 <= indice_jugador <= 11:
                break
        print("Entrada inválida. Por favor, ingrese un número entre 0 y 11.")

    lista_estadisticas_csv = []
    nombre_jugador = lista[indice_jugador]["nombre"]
    estadisticas_jugador = lista[indice_jugador]["estadisticas"]

    for key in estadisticas_jugador:
        key_modificada = key.replace("_", " ").capitalize()
        lista_estadisticas_csv.append("{}: {}".format(key_modificada,estadisticas_jugador[key]))

    archivo_csv = "estadisticas.csv"
    with open(archivo_csv, "w") as file:
        file.write(nombre_jugador + ": \n")
        file.write("Posicion: {}".format(lista[indice_jugador]["posicion"] + "\n"))
        for estadistica in lista_estadisticas_csv:
            file.write(estadistica + "\n")

    print("Jugador '{}' cargado con exito.".format(nombre_jugador))

# ---- PUNTO 4 ----
def mostrar_logros_por_nombre(lista:list):
    #Recibe la lista por parametro, permite buscar un jugador en la lista por su nombre e imprimir sus logros.
    while True:
        nombre = (input("Ingresar el nombre del jugador: ")).title()
        lista_jugadores = []
        for jugador in lista:
            lista_jugadores.append(jugador["nombre"])
            if nombre == jugador["nombre"]:
                print(nombre)
                for logros in jugador["logros"]:
                    print(logros)
        if nombre not in lista_jugadores:
            print("El nombre no se ingreso correctamente, intentelo de nuevo: ")
        else:
            break

# ---- PUNTO 5 ----
def mostrar_promedio_de_puntos_por_partido_del_dream_team(lista:list): 
    #recibe la lista de jugadores por parametro, ordena los nombres e imprime el promedio total de puntos por partido del Dream Team.
    lista_jugadores_ordenada  = []
    for jugador in lista: 
        lista_jugadores_ordenada.append(jugador["nombre"])
    ordenar_lista_ascendente(lista_jugadores_ordenada)
    for nombre_jugador in lista_jugadores_ordenada:
        for jugador in lista:
            if jugador["nombre"] == nombre_jugador:
                print("{} - {}".format(nombre_jugador, jugador["estadisticas"]["promedio_puntos_por_partido"])) 

# ---- PUNTO 6 ----
def mostrar_si_pertenece_salon_de_la_fama(lista:list):
    #recibe la lista de jugadores por parametro pide al usuraio que ingrese el nombre de un jugador y devuelve si pertenece o no pertenece al salon de la fama.
    nombre = (input("Ingresar el nombre del jugador: ")).title()
    lista_jugadores = []
    lista_logros = []
    logro_salon_de_la_fama = "Miembro del Salon de la Fama del Baloncesto"
    for jugador in lista:
        lista_jugadores.append(jugador["nombre"])
        if nombre == jugador["nombre"]:
            for logro in jugador["logros"]:
                lista_logros.append(logro)
    if nombre not in lista_jugadores:
        print("El nombre no se ingreso correctamente :(")
    elif logro_salon_de_la_fama not in lista_logros:
            print("{} NO es miembro del Salon de la Fama del Baloncesto".format(nombre))
    else:
            print("{} es miembro del Salon de la Fama del Baloncesto".format(nombre))

# ---- PUNTO 7 ----
def mostrar_jugador_con_mas_rebotes_totales(lista:list): 
    #recibe la lista de jugadores por parametro y calcula e imprime al jugador con mas rebotes totales.
    mayor_cantidad_de_rebotes = lista[0]["estadisticas"]["rebotes_totales"]
    for indice_jugador in range(len(lista)):
        if lista[indice_jugador]["estadisticas"]["rebotes_totales"] > mayor_cantidad_de_rebotes:
            mayor_cantidad_de_rebotes = lista[indice_jugador]["estadisticas"]["rebotes_totales"]
            jugador_con_mas_rebotes_totales = lista[indice_jugador]["nombre"]
    print("El jugador con la mayor cantidad de rebotes totales es {} con {} rebotes.".format(jugador_con_mas_rebotes_totales,mayor_cantidad_de_rebotes))

# ---- PUNTO 8 ----
def mostrar_jugador_con_mas_tiros_de_campo(lista:list): 
    #recibe la lista de jugadores por parametro y calcula e imprime al jugador con el mayor porcentaje de tiros de campo.
    mayor_porcentaje_tiros_de_campo = lista[0]["estadisticas"]["porcentaje_tiros_de_campo"]
    for indice_jugador in range(len(lista)):
        if lista[indice_jugador]["estadisticas"]["porcentaje_tiros_de_campo"] > mayor_porcentaje_tiros_de_campo:
            mayor_porcentaje_tiros_de_campo = lista[indice_jugador]["estadisticas"]["porcentaje_tiros_de_campo"]
            jugador_con_mas_tiros_de_campo = lista[indice_jugador]["nombre"]
    print("El jugador con el mayor porcentaje de tiros de campo es {} con {}%.".format(jugador_con_mas_tiros_de_campo,mayor_porcentaje_tiros_de_campo))
    
# ---- PUNTO 9 ----
def mostrar_jugador_con_mas_asistencias(lista:list): 
    #recibe la lista de jugadores por parametro y calcula e imprime al jugador con el mayor porcentaje de tiros de campo.
    mayor_asistencias = lista[0]["estadisticas"]["asistencias_totales"]
    for indice_jugador in range(len(lista)):
        if lista[indice_jugador]["estadisticas"]["asistencias_totales"] > mayor_asistencias:
            mayor_asistencias = lista[indice_jugador]["estadisticas"]["asistencias_totales"]
            jugador_con_mas_asistencias = lista[indice_jugador]["nombre"]
    print("El jugador con el mayor numero de asistencias totales es {} con {}.".format(jugador_con_mas_asistencias,mayor_asistencias))

# ---- PUNTO 10 ----
def listar_jugadores_con_promedio_de_puntos_por_partido_mayor_a_x(lista:list): 
    #recibe la lista de jugadores por parametro, pide al usuario que ingrese un valor mayor a 0 y lista a los jugadores que tengan un promedio de puntos por partido mayor al valor ingresado.
    valor_ingresado = float(input("Ingrese el valor a comparar: "))
    if valor_ingresado < 0:
        print("El valor tiene que ser mayor a 0")
    else:
        print("Los jugadores con un promedio de PUNTOS por partido mayor a {} son:".format(valor_ingresado))
        for jugador in lista:
            if jugador["estadisticas"]["promedio_puntos_por_partido"] > valor_ingresado:
                print("{} - {}".format(jugador["nombre"],jugador["estadisticas"]["promedio_puntos_por_partido"]))

# ---- PUNTO 11 ----
def listar_jugadores_con_promedio_de_rebotes_por_partido_mayor_a_x(lista:list): 
    #recibe la lista de jugadores por parametro, pide al usuario que ingrese un valor mayor a 0 y lista a los jugadores que tengan un promedio de rebotes por partido mayor al valor ingresado.
    valor_ingresado = float(input("Ingrese el valor a comparar: "))
    if valor_ingresado < 0:
        print("El valor tiene que ser mayor a 0")
    else:
        print("Los jugadores con un promedio de REBOTES por partido mayor a {} son:".format(valor_ingresado))
        for jugador in lista:
            if jugador["estadisticas"]["promedio_rebotes_por_partido"] > valor_ingresado:
                print("{} - {}".format(jugador["nombre"], jugador["estadisticas"]["promedio_rebotes_por_partido"]))

# ---- PUNTO 12 ----
def listar_jugadores_con_promedio_de_asistencias_por_partido_mayor_a_x(lista:list): 
    #recibe la lista de jugadores, pide al usuario que ingrese un valor mayor a 0 y lista a los jugadores que tengan un promedio de asistencias por partido mayor al valor ingresado.
    valor_ingresado = float(input("Ingrese el valor a comparar: "))
    if valor_ingresado < 0:
        print("El valor tiene que ser mayor a 0")
    else:
        print("Los jugadores con un promedio de ASISTENCIAS por partido mayor a {} son:".format(valor_ingresado))
        for jugador in lista:
            if jugador["estadisticas"]["promedio_asistencias_por_partido"] > valor_ingresado:
                print("{} - {}".format(jugador["nombre"], jugador["estadisticas"]["promedio_asistencias_por_partido"]))

# ---- PUNTO 13 ----
def mostrar_jugador_con_mas_robos(lista:list):
    #recibe la lista de jugadores y calcula e imprime al jugador con el mayor numero de robos totales. 
    mayor_cantidad_robos = lista[0]["estadisticas"]["robos_totales"]
    for indice_jugador in range(len(lista)):
        if lista[indice_jugador]["estadisticas"]["robos_totales"] > mayor_cantidad_robos:
            mayor_cantidad_robos = lista[indice_jugador]["estadisticas"]["robos_totales"]
            jugador_con_mas_robos = lista[indice_jugador]["nombre"]
    print("El jugador con el mayor numero de ROBOS totales es {} con {}.".format(jugador_con_mas_robos,mayor_cantidad_robos))

# ---- PUNTO 14 ----
def mostrar_jugador_con_mas_robos(lista:list): 
    #recibe la lista de jugadores y calcula e imprime al jugador con el mayor numero de bloqueos totales.
    mayor_cantidad_bloqueos = lista[0]["estadisticas"]["bloqueos_totales"]
    for indice_jugador in range(len(lista)):
        if lista[indice_jugador]["estadisticas"]["bloqueos_totales"] > mayor_cantidad_bloqueos:
            mayor_cantidad_bloqueos = lista[indice_jugador]["estadisticas"]["bloqueos_totales"]
            jugador_con_mas_bloqueos = lista[indice_jugador]["nombre"]
    print("El jugador con el mayor numero de BLOQUEOS totales es {} con {}.".format(jugador_con_mas_bloqueos,mayor_cantidad_bloqueos))
    
# ---- PUNTO 15 ----
def listar_jugadores_con_porcentaje_tiros_libres_mayor_a_x(lista:list): 
    #recibe la lista de jugadores, pide al usuario que ingrese un valor mayor a 0 y lista a los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.
    valor_ingresado = float(input("Ingrese el valor a comparar: "))
    if valor_ingresado < 0:
        print("El valor tiene que ser mayor a 0")
    else:
        print("Los jugadores con un porcentaje de tiros libres superior a {} son:".format(valor_ingresado))
        for jugador in lista:
            if jugador["estadisticas"]["porcentaje_tiros_libres"] > valor_ingresado:
                print("{} - {}%".format(jugador["nombre"], jugador["estadisticas"]["porcentaje_tiros_libres"]))

# ---- PUNTO 16 ----
def mostrar_promedio_puntos_dream_team_sin_el_menor(lista:list):
    #recibe la lista de jugadores por parametros y calcula el promedio de puntos por partido del dream team exeptuando al jugador con menos puntos.
    lista_puntos = []
    for jugador in lista:
        lista_puntos.append(jugador["estadisticas"]["promedio_puntos_por_partido"])
    minimo_puntos = min(lista_puntos)
    promedio_puntos = (sum(lista_puntos) - minimo_puntos) / (len(lista_puntos)-1)
    print("El promedio de puntos por partido del Dream Team excluyendo al jugador con la menor cantidad de puntos es: {}".format(promedio_puntos))

# ---- PUNTO 17 ----
def mostrar_jugador_con_mas_logros(lista:list):
    #recibe la lista por parametro y muestra al jugador con la lista mas larga de logros.
    mayor_cantidad_logros = len(lista[1]["logros"])
    for indice in range(len(lista)):
        if len(lista[indice]["logros"]) > mayor_cantidad_logros:
            mayor_cantidad_logros = len(lista[indice]["logros"])
            jugador_con_mas_logros = lista[indice]["nombre"]
            lista_con_mas_logros = lista[indice]["logros"]
    print("El jugador con mayor cantidad de logros es {} con {} logros: ".format(jugador_con_mas_logros,mayor_cantidad_logros))
    for indice_logros in range(len(lista_con_mas_logros)):
        print("{}. {}".format(indice_logros+1,lista_con_mas_logros[indice_logros]))

# ---- PUNTO 18 ----
def listar_jugadores_con_porcentaje_tiros_triples_mayor_a_x(lista:list): 
    #recibe la lista por parametro, pide al usuario que ingrese un valor y lista aquellos jugadores que tengan un porcentaje de tiros triples superior a ese valor.
    valor_ingresado = float(input("Ingrese el valor a comparar: "))
    if valor_ingresado < 0:
        print("El valor tiene que ser mayor a 0")
    else:
        print("Los jugadores con un porcentaje de tiros TRIPLES superior a {} son:".format(valor_ingresado))
        for jugador in lista:
            if jugador["estadisticas"]["porcentaje_tiros_triples"] > valor_ingresado:
                print("{} - {}%".format(jugador["nombre"], jugador["estadisticas"]["porcentaje_tiros_triples"]))

# ---- PUNTO 19 ----
def mostrar_jugador_con_mas_temporadas(lista:list): 
    #recibe la lista de jugadores y calcula e imprime al jugador con el mayor numero de temporadas jugadas.
    mayor_asistencias = lista[0]["estadisticas"]["temporadas"]
    for indice_jugador in range(len(lista)):
        if lista[indice_jugador]["estadisticas"]["temporadas"] > mayor_asistencias:
            mayor_asistencias = lista[indice_jugador]["estadisticas"]["temporadas"]
            jugador_con_mas_asistencias = lista[indice_jugador]["nombre"]
    print("El jugador con el mayor numero de temporadas jugadas es {} con {} temporadas.".format(jugador_con_mas_asistencias,mayor_asistencias))

# ---- PUNTO 20 ----
def ordenar_y_listar_jugadores_con_mas_tiros_de_campo_que_x(lista:list):
    #recibe la lista por parametro e imprime a los jugadores que superen el valor ingresado con su posicion ordenada de forma alfabetica y sus recpectivos porcentajes.
    valor_ingresado = float(input("Ingrese el valor a comparar: "))
    if valor_ingresado > 0:
        lista_jugadores_ordenada = []
        for jugador in lista:
            lista_jugadores_ordenada.append(jugador)

        for indice_a in range(len(lista_jugadores_ordenada)):
            for indice_b in range(indice_a + 1, len(lista_jugadores_ordenada)):
                if lista_jugadores_ordenada[indice_a]["posicion"] > lista_jugadores_ordenada[indice_b]["posicion"]:
                    lista_jugadores_ordenada[indice_a], lista_jugadores_ordenada[indice_b] = lista_jugadores_ordenada[indice_b], lista_jugadores_ordenada[indice_a]
        
        for jugador in lista_jugadores_ordenada:
            if jugador["estadisticas"]["porcentaje_tiros_de_campo"] > valor_ingresado:
                print("{} - {}: {}%".format(jugador["nombre"], jugador["posicion"], jugador["estadisticas"]["porcentaje_tiros_de_campo"]))
    else:
        print("El valor tiene que ser mayor a 0")       

# ---- PUNTO 23 ----
def mostrar_posicion_jugador_estadistica(lista:list):
    """
    Muestra el nombre de los jugadores y permite seleccionar un jugador y una estadística 
    para mostrar la posición del jugador en el ranking correspondiente.
    """
    for indice in range(len(lista)):
        nombre_jugador = lista[indice]["nombre"]
        print("{}. {}".format(indice, nombre_jugador))

    while True:
        indice_jugador = input("Indicar índice de jugador: ")
        
        if indice_jugador.isdigit():
            indice_jugador = int(indice_jugador)
            if 0 <= indice_jugador <= 11:
                break
        print("Entrada inválida. Por favor, ingrese un número entre 0 y 11.")
    nombre_jugador = lista[indice_jugador]["nombre"]
    while True:
        ranking = input("Seleccione un ranking(1-4): \n1. Puntos.\n2. Rebotes.\n3. Asistencias.\n4. Robos.")
        if ranking == "1":
            ordenar_lista_por_estadistica_descendente(lista,"puntos_totales")
            for posicion in range(len(lista)):
                if lista[posicion]["nombre"] == nombre_jugador:
                    os.system('cls')
                    print("{} es el jugador Nro {} en el ranking de puntos, con {} puntos.".format(nombre_jugador,posicion+1,lista[posicion]["estadisticas"]["puntos_totales"]))
            break
        elif ranking == "2":
            ordenar_lista_por_estadistica_descendente(lista,"rebotes_totales")
            for posicion in range(len(lista)):
                if lista[posicion]["nombre"] == nombre_jugador:
                    os.system('cls')
                    print("{} es el jugador Nro {} en el ranking de rebotes, con {} rebotes.".format(nombre_jugador,posicion+1,lista[posicion]["estadisticas"]["rebotes_totales"]))
            break
        elif ranking == "3":
            ordenar_lista_por_estadistica_descendente(lista,"asistencias_totales")
            for posicion in range(len(lista)):
                if lista[posicion]["nombre"] == nombre_jugador:
                    os.system('cls')
                    print("{} es el jugador Nro {} en el ranking de asistencias, con {} asistencias.".format(nombre_jugador,posicion+1,lista[posicion]["estadisticas"]["asistencias_totales"]))
            break
        elif ranking == "4":
            ordenar_lista_por_estadistica_descendente(lista,"robos_totales")
            for posicion in range(len(lista)):
                if lista[posicion]["nombre"] == nombre_jugador:
                    os.system('cls')
                    print("{} es el jugador Nro {} en el ranking de robos, con {} robos.".format(nombre_jugador,posicion+1,lista[posicion]["estadisticas"]["robos_totales"]))
            break
        else:
            print("Opcion invalida, intentelo de nuevo.")

#---- PUNTO EXTRA 1 ----
def mostrar_cantidad_por_posicion(lista:list):
    # Recibe la lista por parametro y muestra la cantidad de jugadores por cada posición.
    contador_escolta = 0
    contador_alapivot = 0
    contador_alero = 0
    contador_base = 0
    contador_pivot = 0
    for jugador in lista_nba:
        if jugador["posicion"] == "Escolta":
            contador_escolta += 1
        elif jugador["posicion"] == "Ala-Pivot":
            contador_alapivot += 1
        elif jugador["posicion"] == "Base":
            contador_base += 1
        elif jugador["posicion"] == "Alero":
            contador_alero += 1
        elif jugador["posicion"] == "Pivot":
            contador_pivot += 1

    print("Base: {}".format(contador_base))
    print("Alero: {}".format(contador_alero))
    print("Escolta: {}".format(contador_escolta))
    print("Ala-Pivot: {}".format(contador_alapivot))
    print("Pivot: {}".format(contador_pivot))

#---- PUNTO EXTRA 2 ----
def mostrar_logro_all_star(lista: list):
    #Muestra los jugadores y sus logros All-Star de forma descendiente con tal de que el primero sea el que mas tiene.
    jugadores_allstar = []
    for jugador in lista:
        nombre = jugador["nombre"]
        logros = jugador["logros"]
        for logro in logros:
            if "All-Star" in logro:
                seleccion = int(logro.split()[0])
                jugadores_allstar.append({"nombre": nombre, "seleccion": seleccion})
    jugadores_allstar = ordenar_lista_dics_descendente(jugadores_allstar, "seleccion")
    for jugador in jugadores_allstar:
        print("{}: {} veces All-Star".format(jugador["nombre"], jugador["seleccion"]))
                    
#---- PUNTO EXTRA 3 ----
def mostrar_mejor_jugador_por_valor(lista:list):
    #Recibe la lista de jugadores y muestra el mejor jugador en cada estadística.
    for key in lista[0]["estadisticas"]:
        ordenar_lista_por_estadistica_descendente(lista,key)
        key_modificada = key.replace("_", " ").capitalize()
        print("{}: {}({}).".format(key_modificada, lista[0]["nombre"],lista[0]["estadisticas"][key]))

#---- PUNTO EXTRA 4 ----
def mostrar_jugador_con_las_mejores_estadisticas(lista:list):
    #Muestra el jugador con las mejores estadísticas en general.
    mejor_estadistica = 0
    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        total_estadisticas = sum(estadisticas.values())
        if total_estadisticas > mejor_estadistica:
            mejor_estadistica = total_estadisticas
            mejor_jugador = jugador["nombre"]
    print("El jugador con las mejores estadísticas en general es: {}".format(mejor_jugador))

# ---------- APLICACION ----------
def ejecutar_app():
    """
    Despliega todo el menu y pide al usuario que elija una de las opciones, dependiendo de la opcion elejida, llama a la funcion correspondiente.
    Tambien limpia la pantalla cada vez que se realiza una acción y despues de ejecutar cada funcion pide que se oprima ENTER con tal de 
    que el user pueda ver la informacion antes de que se limpie la pantalla
    """
    while True:
        os.system('cls')
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            os.system('cls')
            print("Mostrar todos los jugadores y su posicion.")
            mostrar_jugadores(lista_nba)
            input("Pulse ENTER para volver al menu")

        elif opcion == "2":
            os.system('cls')
            print("Mostrar estadisticas de jugador.")
            mostrar_estadisticas_por_indice(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "3":
            os.system('cls')
            print("Seleccionar un jugador y guardar sus estadisticas en un archivo CSV.")
            gurdar_estadisticas_jugador_por_indice(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "4":
            os.system('cls')
            print("Buscar jugador por nombre y mostrar sus logros.")
            mostrar_logros_por_nombre(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "5":
            os.system('cls')
            print("Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team.")
            mostrar_promedio_de_puntos_por_partido_del_dream_team(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "6":
            os.system('cls')
            print("Ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.")
            mostrar_si_pertenece_salon_de_la_fama(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "7":
            os.system('cls')
            print("Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.")
            mostrar_jugador_con_mas_rebotes_totales(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "8":
            os.system('cls')
            print("Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.")
            mostrar_jugador_con_mas_tiros_de_campo(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "9":
            os.system('cls')
            print("Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.")
            mostrar_jugador_con_mas_asistencias(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "10":
            os.system('cls')
            print("Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.")
            listar_jugadores_con_promedio_de_puntos_por_partido_mayor_a_x(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "11":
            os.system('cls')
            print("Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.")
            listar_jugadores_con_promedio_de_rebotes_por_partido_mayor_a_x(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "12":
            os.system('cls')
            print("Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.")
            listar_jugadores_con_promedio_de_asistencias_por_partido_mayor_a_x(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "13":
            os.system('cls')
            print("Mostrar el jugador con la mayor cantidad de robos totales.")
            mostrar_jugador_con_mas_robos(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "14":
            os.system('cls')
            print("Mostrar el jugador con la mayor cantidad de bloqueos totales.")
            mostrar_jugador_con_mas_robos(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "15":
            os.system('cls')
            print("Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior.")
            listar_jugadores_con_porcentaje_tiros_libres_mayor_a_x(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "16":
            os.system('cls')
            print("Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
            mostrar_promedio_puntos_dream_team_sin_el_menor(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "17":
            os.system('cls')
            print("Mostrar el jugador con la mayor cantidad de logros obtenidos.")
            mostrar_jugador_con_mas_logros(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "18":
            os.system('cls')
            print("Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.")
            listar_jugadores_con_porcentaje_tiros_triples_mayor_a_x(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "19":
            os.system('cls')
            print("Mostrar el jugador con la mayor cantidad de temporadas jugadas.")
            mostrar_jugador_con_mas_temporadas(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "20":
            os.system('cls')
            print("Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.")
            ordenar_y_listar_jugadores_con_mas_tiros_de_campo_que_x(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "23":
            os.system('cls')
            print("Mostrar de cada jugador cuál es su posición en cada estadistica.")
            mostrar_posicion_jugador_estadistica(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "1e":
            os.system('cls')
            print("1e. Mostrarla cantidad de jugadores que hay por cada posición.")
            mostrar_cantidad_por_posicion(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "2e":
            os.system('cls')
            print("2e. Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.")
            mostrar_logro_all_star(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "3e":
            os.system('cls')
            print("3e. Mostrar qué jugador tiene las mejores estadísticas en cada valor.")
            mostrar_mejor_jugador_por_valor(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "4e":
            os.system('cls')
            print("4e. Mostrar qué jugador tiene las mejores estadísticas de todos.")
            mostrar_jugador_con_las_mejores_estadisticas(lista_nba)
            input("Pulse ENTER para volver al menu.")

        elif opcion == "0":
            os.system('cls')
            print("""
            
                                         ██████ ██   ██  █████  ██    ██         ██  
                                        ██      ██   ██ ██   ██ ██    ██     ██   ██ 
                                        ██      ███████ ███████ ██    ██          ██ 
                                        ██      ██   ██ ██   ██ ██    ██     ██   ██ 
                                         ██████ ██   ██ ██   ██  ██████          ██  

             """)
            break
        else:
            os.system('cls')
            print("Opcion Incorrecta, intentelo nuevamente.")
            input("Pulse ENTER para volver al menu")

ejecutar_app()