import os
from funciones_administracion_insumos_tienda_de_mascotas import *

def menu_opciones():
    os.system("cls")
    print(""" 
*** Tienda de Mascotas *** 
1- Cargar datos del archivo
2- Listar cantidad por marca
3- Listar insumos por marca
4- Buscar insumo por característica
5- Listar insumos ordenados
6- Realizar compras
7- Guardar en Alimentos en formato JSON
8- Leer desde formato JSON
9- Actualizar precios
10- Agregar un nuevo producto a la lista
11- Guardar datos actualizados
12- Mostrar stock total de marca ingresada
13- Crear archivo csv con productos con 2 o menos de stock
14- Salir del programa 
    """)
    
    while True:
        try:
            opcion = int(input("Ingrese la opcion: "))
            while opcion < 1 or opcion > 14:
                opcion = int(input("ERROR, ingrese un numero que este dentro de las opciones: "))

            return opcion
        
        except ValueError:
            print("ERROR, eso no es un numero")
            os.system("pause")
            os.system("cls")


    
def elegir_opcion(opcion: int, ruta_csv: str, lista_csv: list, lista_dict_transformada: list, lista_alimentos: list, ruta_json: str, 
                  ruta_marcas_txt: str, ruta_csv_nueva: str, ruta_json_nueva: str, ruta_csv_stock: str):
    salir = None # Inicializado en None indica que el usuario todavia no salio, si decide salir esta variable cambia de valor
    match opcion:
        case 1:
            lista_csv = leer_csv(ruta_csv)
            lista_dict_transformada = transformar_lista_a_dict(ruta_csv, lista_csv, 'id', 'nombre', 'marca', 'precio', 'caracteristicas')
        case 2:
            listar_cantidad_por_clave(lista_dict_transformada, 'marca')
        case 3:
            listar_insumos_por_clave(lista_dict_transformada, 'marca', 'precio', 'nombre')
        case 4:
            buscar_insumo_por_caracteristica(lista_dict_transformada, 'caracteristicas', 'nombre', 'marca', 'precio', 'id')
        case 5:
            listar_insumos_ordenados(lista_dict_transformada, 'marca', 'precio', 'nombre', 'id', 'caracteristicas')
        case 6:
            realizar_compra(lista_dict_transformada, 'marca', 'id', 'precio', 'nombre', 'stock')
        case 7:
            crear_json(lista_dict_transformada, 'nombre', 'Alimento')
        case 8:
            leer_json(ruta_json)
        case 9:
            actualizar_precios(ruta_csv, lista_dict_transformada, 'id', 'nombre', 'marca', 'precio', 'caracteristicas', 'stock')
        case 10:
            ingreso_producto(ruta_marcas_txt, ruta_csv, lista_dict_transformada)
            lista_csv = leer_csv(ruta_csv)
            lista_dict_transformada = transformar_lista_a_dict(ruta_csv, lista_csv, 'id', 'nombre', 'marca', 'precio', 'caracteristicas')
        case 11:
            guardar_en_archivo(ruta_csv, ruta_csv_nueva, ruta_json_nueva)
        case 12:
            mostrar_stock_por_marca(lista_dict_transformada, "marca", "stock")
        case 13:
            imprimir_bajo_stock(lista_dict_transformada, ruta_csv_stock, "stock")
        case 14:
            os.system("cls")
            salir = input("Seguro que desea salir? s/n: ")
            pass

    return salir, lista_csv, lista_dict_transformada, lista_alimentos