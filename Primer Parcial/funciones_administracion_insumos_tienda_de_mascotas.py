import re
import os
import json
import random

""" 
1 - Cargar datos desde archivo: Esta opción permite cargar el contenido del archivo "Insumos.csv" en una colección, teniendo en cuenta que las características de los insumos 
deben estar en un tipo de colección integrada.
"""

def leer_csv(ruta: str):
    """Abre el archivo csv, lo lee y lo arregla para poder usarlo

    Args:
        ruta (str): la ruta del archivo csv el cual va a leer

    Returns:
        list: la lista modificada sin todo lo que intefiere
    """
    lista_retorno = []
    lista_aux = []
    with open(ruta, encoding='utf-8') as file:  # El encoding es para que se pueda abrir el archivo csv

        for i in file:
            i = i.replace("\n", "")
            i = i.replace("~", " - ") 
            i = i.replace("$", "")
            lista_aux = i.split(',')
            lista_retorno.append(lista_aux)
        lista_retorno.pop(0) # El pop acá es para sacarle lo que hay en el indice 0 de la lista
        return lista_retorno


def transformar_lista_a_dict(ruta: str, lista: list, key: str, key2: str, key3: str, key4: str, key5: str):
    """Transforma la lista en una lista de diccionarios dandole las keys por la que se tiene que dividir y la lista:

    Args:
        ruta (str): la ruta del archivo csv
        list (list): la lista que viene de la lectura del csv
        key (str): key de id
        key2 (str): key de nombre
        key3 (str): key de marca
        key4 (str): key con valor float
        key5 (str): key de caracteristica

    Returns:
        list: La lista de diccionarios modificada con sus respectivas keys
    """
    lista = list(map(lambda ins: {key: ins[0], key2: ins[1], key3: ins[2], key4: float(ins[3]), key5: ins[4], "stock": random.randint(0, 10)}, leer_csv(ruta)))
    print("==================================")
    print("La lista se guardó correctamente")
    print("==================================")
    return lista

"""
2 - Listar cantidad por marca: Muestra todas las marcas y la cantidad de insumos correspondientes a cada una.
"""


def esta_en_lista(lista: list, key: str) -> bool:
    """Devuelve True si la key ingresada esta en la lista y si no esta devuelve False

    Args:
        lista (list): la lista a recorrer para 
        key (str): key de lo que queres ver si esta en la lista

    Returns:
        bool
    """
    esta_en_lista = False
    for i in lista:
        if i == key:
            esta_en_lista = True
            break
    return esta_en_lista


def listar_cantidad_por_clave(lista: list, key: str) -> None:
    """Si la marca no fue agregada a la lista todavia lo agrega, despues cuenta cuantas veces esta en la lista y muestra cuantas veces esta

    Args:
        lista (list): la lista a recorrer
        key (str): key que va a decir porque tiene que listar

    Returns:
        None
    """
    lista_claves = []

    for insumo in lista:
        if not esta_en_lista(lista_claves, insumo[key]):
            lista_claves.append(insumo[key])

    print("------------------------------------------")
    for marca in lista_claves:
        contador = 0
        for insumo in lista:
            if(insumo[key] == marca):
                contador += 1 # Cuenta cuantas veces esta
        print(f"Hay {contador} producto/s de la marca {marca}")
        print("------------------------------------------")

"""
3 - Listar insumos por marca: Muestra, para cada marca, el nombre y precio de los insumos correspondientes.
"""

# Muestra a todos los insumos, si estan repetidos no los agrega a la lista que va a recorrer:
def listar_insumos_por_clave(lista: list, key: str, key2: str, key3: str):
    """Muestra a todos los insumos, si estan repetidos no los agrega a la lista que va a recorrer

    Args:
        lista (list): la lista a recorrer
        key (str): key la cual va a decidir porque se se listan los insumos
        key2 (str): key con valor float
        key3 (str): key de nombre

    Returns:
        None
    """
    lista_claves = []

    for insumo in lista:
        if not esta_en_lista(lista_claves, insumo[key]): # Hace que no se repitan los productos
            lista_claves.append(insumo[key])

    for marca in lista_claves:
        print("=====================================")
        print(f"Productos de la marca: {marca}")
        print("=====================================")
        for insumo in lista:
            if insumo[key] == marca:
                print(f"""
Nombre: {insumo[key3]}
Precio: ${insumo[key2]}
""")

"""
4 - Buscar insumo por característica: El usuario ingresa una característica (por ejemplo, "Sin Granos") y se listarán todos los insumos que poseen dicha característica.
"""

def buscar_insumo_por_caracteristica(lista: list, key: str, key2: str, key3: str, key4: str, key5: str):
    """Pide al usuario que ingrese una caracteristica y busca todos los insumos que tengan esa caracteristica y los muestra, si no existe no lo busca

    Args:
        lista (list): lista a recorrer
        key (str): la key que decide donde va a buscar la caracteristica
        key2 (str): key de nombre
        key3 (str): key de marca
        key4 (str): key de precio con valor float
        key5 (str): key de id

    Returns:
        None
    """
    flag_while = True # Esta flag es para que el while no quede como bucle infinito
    caract = input("Ingrese la caracteristica que quiere buscar en los insumos: ").capitalize()

    insumos_encontrados = []
    for insumo in lista:
        if re.search(caract, str(insumo[key])):
            insumos_encontrados.append(insumo)

    while flag_while:
        if not insumos_encontrados or caract == "": # Si la lista esta vacia quiere decir que no encontro la caracteristica en ningun lado
            print("No se encontraron insumos con la caracteristica", caract)
            break
        else:
            flag_while = False # Si la flag es falsa quiere decir que encontro la caracteristica entonces el while no se hace infinito
            os.system("cls")

            print("===================================================")
            print("Los insumos con la caracteristica", caract, "son:")
            print("===================================================")
            for insumo in insumos_encontrados:
                print(f"""
ID: {insumo[key5]}
Nombre: {insumo[key2]}
Marca: {insumo[key3]}
Precio: ${insumo[key4]}
Caracteristicas: {insumo[key]}
                    """)
                print("------------------------------------------------------------------------------")

""" 
5 - Listar insumos ordenados: Muestra el ID, descripción, precio, marca y la primera característica de todos los productos, ordenados por marca de forma ascendente (A-Z), 
ante marcas iguales, por precio descendente.
"""

def listar_insumos_ordenados(lista: list, key: str, key2: str, key3: str, key4: str, key5: str):
    lista_temporal  = lista.copy() # Copio la lista en una temporal asi no se rompe el otro codigo cuando hago bubble sort
    """Usa el metodo bubble sort para ordenar los insumos por una key a eleccion y despues usa la key2 para ordenar de manera descendente si tienen la misma key

    Args:
        lista (list): lista a recorrer
        key (str): la key que decide que va a ordenar
        key2 (str): key de valor float
        key3 (str): key de nombre que va a ordenar de manera descendente cuando se cumplen los requisitos
        key4 (str): key de id
        key5 (str): key de caracteristicasa

    Returns:
        None
    """
    tam = len(lista_temporal)

    for i in range(tam - 1): # El tam - 1 es para que cubra todos los indices que haya
        for j in range(i + 1, tam): # el + 1 es para que se ponga adelante del valor de i. El tam es para decirle donde tiene que terminar
            if lista_temporal[i][key] > lista_temporal[j][key]:
                aux = lista_temporal[i]
                lista_temporal[i] = lista_temporal[j]
                lista_temporal[j] = aux

            if lista_temporal[i][key] == lista_temporal[j][key]: # Si las marcas son iguales comparo los precios y los ordeno de manera descendente
                if lista_temporal[i][key2] < lista_temporal[j][key2]:
                    aux = lista_temporal[i]
                    lista_temporal[i] = lista_temporal[j]
                    lista_temporal[j] = aux

    print("==========================================================================================")
    print("Insumos ordenados por marca (A-Z), (precios de misma marca estan ordenados por precio): ")
    print("==========================================================================================")
    for insumo in lista_temporal:
        caracteristicas = insumo[key5].split(" - ") # Hago el split para que queden separados por indices
        print(f"""
ID: {insumo[key4]}
Nombre: {insumo[key3]}
Marca: {insumo[key]}
Precio: ${insumo[key2]}
Caracteristica: {caracteristicas[0]}
                    """) # Ya que estan separados por el split agarrando el indice 0 va a mostrar solo la primera caracteristica
        print("---------------------------------------------------------------------------------------")

"""
6 - Realizar compras: Permite realizar compras de productos. El usuario ingresa una marca y se muestran todos los productos disponibles de esa marca. 
Luego, el usuario elige un producto y la cantidad deseada. Esta acción se repite hasta que el usuario decida finalizar la compra.
Al finalizar, se muestra el total de la compra y se genera un archivo TXT con la factura de la compra, incluyendo cantidad, producto, subtotal y el total de la compra.
"""

def crear_recibo_txt(lista: str, precio_final: float):
    """Crea el archivo recibo.txt y escribe todo lo que va a ir en el recibo

    Args:
        lista (list): lista a recorrer
        precio_final (float): el precio final de la compra

    Returns:
        None
    """
    file = open("D:\\Usuarios\\mylov\\Escritorio\\UTN\\Castelli Felix Parcial 1-A Laboratorio\\Primer Parcial\\Recibo.txt", 'a', encoding='utf-8')

    file.write("                                            ====================================\n")
    file.write("                                                      RECIBO DE COMPRA\n")
    file.write("                                            ====================================\n")
    for i in lista:
        file.write(f"""
                                                        Nombre: {i['nombre']}
                                                        Marca: {i['marca']}
                                                        Precio: ${i['precio']}
                                                        Cantidad: {i['cantidad']}
                                                        Precio Total: ${i['precio_acumulado']:.2f}
""")
        file.write("-------------------------------------------------------------------------------------------\n")

    file.write("                                             ======================================\n")
    file.write(f"                                                      Precio Final: ${precio_final:.2f}\n")
    file.write("                                             ======================================\n")

    file.close()


def mostrar_productos(productos: list, key: str, key2: str, key3: str, key4: str, key5: str):
    """Recibe una marca a eleccion y muestra todos los productos de esa marca

    Args:
        productos (list): lista de productos de la marca indicada que va a ser recorrida
        key (str): key de id
        key2 (str): key de nombre
        key3 (str): key de precio con valor tipo float
        key4 (str): key de caracteristicas

    Returns:
        None
    """
    os.system("cls")

    print("===================================================")
    print(f"Los productos de la marca ingresada son: ")
    print("===================================================")
    for producto in productos:
        print(f"""
ID: {producto[key]}
Nombre: {producto[key2]}
Precio: ${producto[key3]}
Caracteristicas: {producto[key4.replace('[]', '')]}
Stock: {producto[key5]}
""")
        print("------------------------------------------------------------------------------")


def buscar_producto_por_marca(lista: list, key: str) -> list:
    """Recibe la marca por input y la usa para buscar en la lista ingresada todas las ocurrencias de esa marca y muestra los productos encontrados

    Args:
        productos (list): lista de productos de la marca indicada que va a ser recorrida
        key (str): key de marca

    Returns:
        list
    """
    productos_encontrados = []

    while True:
        marca = input("Ingrese la marca que quiere buscar: ").capitalize()

        for producto in lista:
            if re.search(marca, producto[key]): 
                productos_encontrados.append(producto)

        if not productos_encontrados or marca == "": # Para verificar que la marca ingresada existe
            os.system("cls")
            print(f"No se encontraron productos de la marca {marca}")
            continue

        mostrar_productos(productos_encontrados, 'id', 'nombre', 'precio', 'caracteristicas', 'stock')
        break

    return productos_encontrados


def realizar_compra(lista: list, key: str, key2: str, key3: str, key4: str, key5: str) -> None:
    """Realiza la compra en base a los productos encontrados el id y la cantidad ingresada y finalmente llama a la funcion de crear recibo con todos los datos acomodados

    Args:
        lista (list): lista a recorrer
        key (str): key de marca
        key2 (str): key de id
        key3 (str): key de precio con valor float
        key4 (str): key de nombre

    Returns:
        None
    """
    acumulador_precio = 0
    cantidad_ingresada = 0
    lista_productos_comprados = []

    while True:
        productos_encontrados = buscar_producto_por_marca(lista, key)

        if not productos_encontrados:  # Verifica si no se encontraron productos
            break

        id_ingresado = input("Ingrese el ID del producto que quiere comprar: ")

        for producto in productos_encontrados:
            if id_ingresado == producto[key2]:
                while True:
                    if producto[key5] == 0:
                        print("No hay stock de ese producto")
                        break
                    else:
                        try:
                            cantidad_ingresada = int(input("Ingrese cuántos quiere llevar: "))

                            while cantidad_ingresada > producto[key5] or cantidad_ingresada == 0:
                                cantidad_ingresada = int(input("ERROR, no hay el suficiente stock: "))
                            break
                        except ValueError:
                            print("ERROR, eso no es un número válido. Intente nuevamente.")

                precio = float(producto[key3]) * cantidad_ingresada
                acumulador_precio = acumulador_precio + precio

                lista_productos_comprados.append({
                    key4: producto[key4], 
                    key: producto[key], 
                    key3: producto[key3], 
                    'cantidad': cantidad_ingresada,
                    'precio_acumulado': precio
                    })
                break
        else:
            print("ERROR, el producto que ingresó no existe")

        respuesta = input("Quiere comprar otro producto? (si o no): ").lower()
        os.system("cls")
        while respuesta not in ['si', 'no']:
            respuesta = input("ERROR, ingrese si o no: ")
            os.system("cls")
        if respuesta == "no":
            if lista_productos_comprados:
                print("================================")
                print("El recibo fue creado con exito")
                print("================================")
                crear_recibo_txt(lista_productos_comprados, acumulador_precio)
            break

"""
7 - Guardar en formato JSON: Genera un archivo JSON con todos los productos cuyo nombre contiene la palabra "Alimento"
"""

def buscar_por_nombre(lista: list, key: str, nombre: str) -> list:
    """Recorre una lista y un nombre el cual va a buscar y va a crear una lista filtrada con solo productos que tienen ese nombre

    Args:
        lista (list): la lista a recorrer
        key (str): key de nombre
        nombre (str): el nombre por el que filtrar

    Returns:
        list
    """
    lista_filtrada = []
    for insumo in lista:
        if re.search(nombre, insumo[key]): # Busca si el insumo tiene de nombre Alimento
            lista_filtrada.append(insumo)
    return lista_filtrada

def crear_json(lista: list, key: str, nombre: str):
    """Crea el archivo lista_alimentos.json con la lista de todos los productos que tengan el nombre que se pasa por parametro

    Args:
        lista (list): la lista a recorrer
        key (str): key de nombre
        nombre (str): el nombre por el que filtrar

    Returns:
        None
    """
    lista_filtrada = buscar_por_nombre(lista, key, nombre)
    with open("D:\\Usuarios\\mylov\\Escritorio\\UTN\\Castelli Felix Parcial 1-A Laboratorio\\Primer Parcial\\lista_alimentos.json", 'w', encoding='utf-8') as file:

        json.dump(lista_filtrada, file, indent = 2 , ensure_ascii= False, separators=(", ", " : "))
    """El primer parametro es la lista en la que se va a basar, el segundo parametro es en donde va a escribir, El tercer parametro es la identacion, 
    el cuarto parametro es para que funcionen los tildes y el ultimo parametro es el separators que le va a dar forma para que no este todo junto"""

    print("===========================================================")
    print("El archivo JSON con los alimentos fue creado con exito")
    print("===========================================================")

"""
8 - Leer desde formato JSON: Permite mostrar un listado de los insumos guardados en el archivo JSON generado en la opción anterior.
"""

def leer_json(ruta: str) -> list:
    """Lee el archivo json y muestra el listado de todo lo que hay en el

    Args:
        ruta (str): La ruta del archivo json que va aleer

    Returns:
        list
    """
    with open(ruta, 'r', encoding='utf-8') as file:  # El encoding es para que se pueda abrir el archivo csv
        lista_alimentos = json.load(file)

        print("-----------------------------------------------------------------------------------------")
        for i in lista_alimentos:
            print(f"""
ID: {i['id']}
Nombre: {i['nombre']}
Marca: {i['marca']}
Precio: {i['precio']}
Caracteristicas: {i['caracteristicas']}
            """)
            print("-----------------------------------------------------------------------------------------")

"""
9 - Actualizar precios: Aplica un aumento del 8.4% a todos los productos, utilizando la función map. Los productos actualizados se guardan en el archivo "Insumos.csv".
"""

def actualizar_precios(ruta: str, lista: list, key: str, key2: str, key3: str, key4: str, key5: str, key6: str):
    """Recibe el archivo de csv y le aplica un aumento, luego reemplaza lo guardado en el archivo csv por los nuevos precios

    Args:
        ruta (str): ruta del archivo csv que va a ser leido y reemplazado
        lista (list): lista a recorrer
        key (str): key de id
        key2 (str): key de nombre
        key3 (str): key de marca
        key4 (str): key de precio con valor float
        key5 (str): key de caracteristicas
    """
    precios_actualizados = list(map(lambda precio: {
        'id': precio[key],
        'nombre': precio[key2],
        'marca': precio[key3], 
        'precio': round(((precio[key4] * 8.4 / 100) + precio[key4]), 2), 
        'caracteristicas': (precio[key5]),
        'stock': (precio[key6])}, lista))
    
    with open(ruta, 'w', encoding='utf-8') as file:
        for precio in precios_actualizados:
            lista_nuevos_precios = f"{precio['id']},{precio['nombre']},{precio['marca']},${precio['precio']},{precio['caracteristicas']},{precio['stock']}\n"  # Le doy formato a los datos
            file.write(lista_nuevos_precios)

    print("============================================================================")
    print("El archivo de insumos fue actualizado correctamente con los nuevos precios")
    print("============================================================================")

"""
El programa deberá permitir agregar un nuevo producto a la lista (mediante una nueva opción de menú). Al momento de ingresar la marca del producto se deberá mostrar por pantalla un
listado con todas las marcas disponibles. Las mismas serán cargadas al programa desde el archivo marcas.txt. En cuanto a las características, 
se podrán agregar un mínimo de una y un máximo de 3.
"""

def leer_marcas(ruta: str):
    lista_marcas = []

    with open(ruta, 'r') as file:
        marcas = file.readlines()
        for i in marcas:
            i = i.strip()
            lista_marcas.append(i)

    return lista_marcas

def mostrar_marcas(marcas: list) -> list:

    print("Marcas disponibles: ")
    print("--------------------")
    for i in marcas:
        print(i)
        print("--------------------")


def ingreso_producto(ruta: str, ruta2: str, lista_dict_transformada: list):
    lista_caracteristicas = []
    contador = 0

    for insumo in lista_dict_transformada:
        contador_de_id = int(insumo["id"])

    contador_de_id += 1

    marcas = leer_marcas(ruta)     
    mostrar_marcas(marcas)

    marca = input("Ingrese la marca del producto: ").title()
    while marca not in marcas:
        marca = input("ERROR, esa marca no esta en la lista, ingrese otra marca: ").title()

    nombre = input("Ingrese el nombre del producto que quiera agregar: ").capitalize()

    while contador < 3:
        if contador == 0:
            caracteristica = input("Ingrese la caracteristica del producto: ").capitalize()
            lista_caracteristicas.append(caracteristica)    
    
        elif contador < 3:
            opcion_caracteristica = input("Desea agregar otra caracteristica? s/n: ").lower()
            if opcion_caracteristica == 's':
                caracteristica = input("Ingrese otra caracteristica del producto: ").capitalize()
                lista_caracteristicas.append(caracteristica)
            else:
                break
        contador += 1

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0.50:
                precio = float(input("Ingrese un precio valido: "))
            break
        except ValueError:
            print("ERROR, eso no es un numero. Por favor, ingrese un numero")

    caracteristicas_str = " - ".join(lista_caracteristicas)
    producto = {
        'id': contador_de_id ,
        'nombre': nombre,
        'marca': marca,
        'precio': precio,
        'caracteristicas': lista_caracteristicas
    }

    with open(ruta2, 'a') as file:
        file.write(f"\n{contador_de_id},")
        file.write(f"{producto['nombre']},")
        file.write(f"{producto['marca']},")
        file.write(f"${producto['precio']},")
        file.write(f"{caracteristicas_str}")

"""
Agregar una opción para guardar todos los datos actualizados (incluyendo las altas). El usuario elegirá el tipo de formato de exportación: csv o json.
"""
def guardar_en_archivo(ruta: str, ruta2: str, ruta3: str):
    while True:
        try:
            opcion = input("¿En qué tipo de archivo desea guardar los productos, en CSV o JSON? ").lower()

            if opcion not in ["csv", "json"]:
                print("ERROR: opción inválida")
            else:
                break

        except ValueError:
            print("ERROR: opción inválida")

    if opcion == "csv":
        guardar_csv(ruta, ruta2)
    elif opcion == "json":
        guardar_json(ruta, ruta3)


def guardar_csv(ruta: str, ruta2: str):
    lista_productos = leer_csv(ruta)

    with open(ruta2, 'w', encoding='utf-8') as file:
        for producto in lista_productos:
            producto = [str(elemento) for elemento in producto]
            linea_csv = ','.join(producto)
            file.write(f"{linea_csv}\n")

def guardar_json(ruta: str, ruta3: str):
    lista_productos = leer_csv(ruta)

    productos_json = []

    for producto in lista_productos:
        producto_json = {
            "id": producto[0],
            "nombre": producto[1],
            "marca": producto[2],
            "precio": producto[3],
            "caracteristicas": producto[4]
        }
        productos_json.append(producto_json)

    with open(ruta3, 'w', encoding='utf-8') as file:
        json.dump(productos_json, file, indent=4)

"""
Agregar opción stock por marca: Pedirle al usuario una marca y mostrar el stock total de los productos de esa marca.
"""

def mostrar_stock_por_marca(lista: str, key: str, key2: str):
    contador_stock = 0
    lista_productos_marca = buscar_producto_por_marca(lista, key)
    for producto in lista_productos_marca:
        contador_stock += producto[key2]
    print(f"El stock total de los productos de la marca ingresada es: {contador_stock}")

"""
Agregar opción imprimir bajo stock. Que imprima en un archivo de texto en formato csv. 
Un listado con el nombre de producto y el stock de aquellos productos que tengan 2 o menos unidades de stock.
"""

def imprimir_bajo_stock(lista: list, ruta: str, key: str):

    with open(ruta, 'w', encoding='utf-8') as file:
        for producto in lista:
            if producto[key] <= 2:
                producto_completo = f"{producto['id'], producto['nombre'], producto['marca'], producto['precio'], producto['caracteristicas'], producto[key]}"
                producto_completo = producto_completo.replace("'", '').replace("(", '').replace(")", '')
                file.write(f"{producto_completo}\n")
        print("Archivo de stock creado con exito")