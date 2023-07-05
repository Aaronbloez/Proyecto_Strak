import os
import re
from data import lista_personajes
#Verifica que sea un numero
def EsUnNuero(numero):
    try:
        float(numero)
        return False
    except ValueError:
        return True
# Verifica que el campo no este vacio
def CampoVacio(campo:str):
    retorno = False
    if campo == "":
        print("El campo esta vacio")
        retorno = True
    return retorno
#Separa a los heroes discriminando por genero
def Listar_heroes(list:dict,key:str,genero:str)->list:
    lista_masculinos = []
    for item in list:
        comparar =  item['genero']
        if(key == comparar):
            lista_masculinos.append({'nombre':item['nombre'],'identidad':item['identidad'],'empresa':item['empresa'],
            'altura':item['altura'],'peso':item['peso'],'genero':item['genero'],'color_ojos':item['color_ojos'],'color_pelo':item['color_pelo'],
            'fuerza':item['fuerza'],'inteligencia':item['inteligencia']})

    return lista_masculinos

#Verifica que no halla campos vacios en los datos
def Normalizar_datos(diccionario:list)->None:
    lista = []
    for i in diccionario:
        error = False
        nombre = CampoVacio(i['nombre'])
        identidad = CampoVacio(i['identidad'])
        empresa = CampoVacio(i['empresa'])
        altura = EsUnNuero(i['altura'])
        Peso = EsUnNuero(i['peso'])
        genero = CampoVacio(i['genero'])
        ojos = CampoVacio(i['color_ojos'])
        pelo = (i['color_pelo'])
        Fuerza = EsUnNuero(i['fuerza'])
        Inteligencia = (i['inteligencia'])

        if altura == True or Peso == True or Fuerza == True:
            print("Algunos datos no son numericos, por favor revise la lista")
            error = True
        if nombre == True or identidad == True or empresa == True  or genero == True or ojos == True or pelo == True or Inteligencia == True:
            print("Datos Nomalisados")
            error = True
        if nombre == True and identidad == True and empresa == True  and genero == True and ojos == True or pelo == True and Inteligencia == True:
            print("Error :Revise la lista todos los datos son incorrectos")
            error = True
        if error:
            break
        else:
            lista.append({'nombre':i['nombre'],'identidad':i['identidad'],'empresa':i['empresa'],
            'altura':i['altura'],'peso':i['peso'],'genero':i['genero'],'color_ojos':i['color_ojos'],'color_pelo':i['color_pelo'],
            'fuerza':i['fuerza'],'inteligencia':i['inteligencia']})
#Ensenia por consola los datos siempre y cuando halla algo en la variable
def ImprimirDaTO(key:str)->None:
    for i in key:
        a = CampoVacio(i)
        if a:
            print("-1")
            break
        else:
            print(i)
# Arma una lista con todos los nombres
def ObtenerNombre(heroe:dict)->list:
    list = []
    for nombre in heroe:
        list.append(f"Nombre: {nombre['nombre']}")
    return list
# Muestra todos los nombres de la lista de diccionarios
def Mostrar_Nombre(heroe: dict, key:str)-> None:
    for nombre in heroe:

        print(f"Nombre: {nombre[key]}")
# Convierte una lsta a un string con la clave nobre y dos mas que se pasan por parametro
def Convertir_Lista_Strings(heroe:dict, key:str, key2:str)-> list:
    lista = []
    for nombre in heroe:
        lista.append(f"Nombre: {nombre['nombre']}| {key2} : {nombre[key2]}")
    return lista
#Muestra el heroe mas alto
def Mostrar_heroe_alto(list:dict,key,key2)->str:
    Altura_max = 0
    Nombre_de_heroe_mas_alto = None

    for item in list:
        altura = float(item[key])
        if(altura > Altura_max):
            Altura_max = altura
            Nombre_de_heroe_mas_alto = item[key2]
    return Nombre_de_heroe_mas_alto

#Muestra el heroe mas bajo
def Mostrar_heroe_bajo(list:dict,key,key2)->str:
    Altura_min = 100000000000
    Nombre_de_heroe_mas_bajo = None

    for item in list:
        altura = float(item[key])
        if(altura < Altura_min):
            Altura_min = altura
            Nombre_de_heroe_mas_bajo = item[key2]
    return Nombre_de_heroe_mas_bajo
#Calcula el maximo
def CalcularMax(list:dict,key)->str:
    Altura_min = 0

    for item in list:
        altura = float(item[key])
        if(altura > Altura_min):
            Altura_min = altura
    return Altura_min

#Calcula promedios
def Calcular_promedios(list:dict,key)->float:
    contador = 0
    acumulador = 0

    for item in list:
        altura = float(item[key])
        acumulador += altura
        contador += 1
    Promedio = acumulador/contador
    return Promedio

# Aisla la caracteristica que se le pase por parametro
def Contar_aislar_caracteristica(list:dict,key)->list:
    contador = []
    for color in list:
        if color in contador:
            contador
        else:
            contador.append(color[key])


    return contador
#Elimina los elemento repetidos de una lista de diccionarios
def Sacar_Repetidos(list:list)->dict:
    lista_sin_repetidos = []
    lista_aux = []
    for elemento in list:
        if not elemento in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)

    return lista_sin_repetidos
# Cuenta la cantidad de un tipo determinado de caracteristica que se le pase por parametro
def Contar_caracteristica(list:list,dict:dict,key:str)->dict:
    lista_aux = []
    for elemento in list:
        cuenta = 0
        for item in dict:
            if elemento == item[key]:
                cuenta += 1
        lista_aux.append({elemento:cuenta})
    return lista_aux
#Agrupa a los heroes discriminando por una caracteristica
def Retornar_heroes_agrupados_por_carac(diccionario:dict,lista:list,key:str)->dict:
    lista_colores = []
    for elemento in lista:
        flag = True
        for item in diccionario:
            if elemento == item[key] and flag:
                lista_colores.append("-------------------------------------")
                lista_colores.append(item[key])
                lista_colores.append("-------------------------------------\n")
                lista_colores.append(item['nombre'])
                flag = False
            elif elemento == item[key]:
                lista_colores.append(item['nombre'])
    return lista_colores
#Muestra una lista
def Mostrar_lista(diccionario:dict)->None:
    for color in diccionario:
        a = str(color)
        colora = a.replace("{","").replace("}","").replace("'","")
        if colora == "":
            print("No tiene")
        else:
            print(colora)

#Printea los colores que tenga en el diccionario
def Mostrar_color_diccionario(diccionario:dict)->None:
    for color in diccionario:
        if color == '' or color == "":
            print("No tiene")
        else:
            cadena = str(color).replace("{","",).replace("}","").replace('',"").replace("'","")
            print(cadena)
# Calculo el maxioo o el minimo dependiendo lo que pida el usuario
def Calcular_max_min(diccionario:list, key2:str,key:str)->int:
    if key2 == "maximo":
        Altura_min = 0
        for item in diccionario:
            altura = float(item[key])
            if(altura > Altura_min):
                Altura_min = altura
    elif key2 == "minimo":
        Altura_min = 100000000000

        for item in diccionario:
            altura = float(item[key])
            if(altura < Altura_min):
                Altura_min = altura
    return Altura_min
# Suma todas las clave de un tipo la cual se pasa por parametro
def SumarDatoHeroe(diccionario:list,key:str)->int:
    suma = 0 
    for i in diccionario:
        a = float(i[key])
        suma += a
    print(suma)
    return suma
#Cuenta la cantidad de heroes
def Contar_heroes(diicionario:dict)->int:
    contador = 0
    for i in diicionario:
        contador += 1
    return contador
# Divide un divisor por su dividendo
def Dividir(divisor:float,dividendo:float)->float:
    resultado = divisor/dividendo

    return resultado
#Agrega las iniciales  a el diccionario
def definir_iniciales_nombre(diccionario:dict)->list:
    lista_dict = []
    iniciales = []
    tipo = type(diccionario)
    if tipo == list:
        #if "nombre" in diccionario:
        for i in diccionario:
            iniciales = []
            palabras = str(i['nombre']).split()
                #NO_Paso = False
            for letra in palabras:
                if letra == "-":
                    letra = letra.replace("-","")
                if letra == "the":
                    pass
                else:
                    print(letra)
                    iniciales.append(letra[0])
            iniciales = str(iniciales).replace("[","").replace("]","").replace(",",'')
            lista_dict.append({'nombre':i['nombre'],'iniciales':iniciales,'identidad':i['identidad'],'empresa':i['empresa'],
                'altura':i['altura'],'peso':i['peso'],'genero':i['genero'],'color_ojos':i['color_ojos'],'color_pelo':i['color_pelo'],
                'fuerza':i['fuerza'],'inteligencia':i['inteligencia']})
    return lista_dict


# Agrega el ID al diccionario
def generar_Lista_con_id(diccionario:list)->list:
    contador = 1
    lista_dict = []
    for i in diccionario:
        lista_dict.append({'Id':contador,'nombre':i['nombre'],'identidad':i['identidad'],'empresa':i['empresa'],
                'altura':i['altura'],'peso':i['peso'],'genero':i['genero'],'color_ojos':i['color_ojos'],'color_pelo':i['color_pelo'],
                'fuerza':i['fuerza'],'inteligencia':i['inteligencia']})
        contador += 1
    return lista_dict
# Crea una lista con el campo ID y el campo Genero
def sacar_id_genero(diccionario:list)->list:
    lista_genero_id = []
    for i in diccionario:
        lista_genero_id.append({'Id':i['Id'],'genero':i['genero']})
    return lista_genero_id

# Verifica que un entero no sea un campo vacio y que sea un numero
def sanitizar_entero(numero:str)->int:
    try:
        numero = int(numero)
        if numero > 0:
            return numero
        elif 0 > numero:
            return -2
            
    except ValueError:
        if numero.isalnum():
            return -1
        else:
            return -3
# Verifica que un flotante no sea un campo vacio y que sea un numero
def sanitizar_flotante(numero:str)->float:
    try:
        numero = float(numero)
        if numero > 0:
            return numero
        elif 0 > numero:
            return -2
            
    except ValueError:
        if numero.isalnum():
            return -1
        else:
            return -3
# Verifica que un string no este vacio y que solo sean caracteres alphanumericos
def sanitizar_strings(string:str)->str:
    string = string.strip()
    string = string.lower()
    if "/" in string:
        string = string.replace("/","")
    if "(" in string or ")" in string:
        string = string.replace("(","")
        string = string.replace(")","")
    string  = string.replace(" ","ñ")
    if string.isalpha():
        string = string.replace("ñ","y")
        string = string.lower()
        return string
    else:
        return "N/A"

def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str)->str:
    Flag_se_sanitiza = True
    if clave != "nombre" and clave != "altura" and clave != "peso" and clave != "identidad" and clave != "empresa" and clave != "genero" and clave != "color_ojos" and clave != "color_pelo" and clave != "fuerza" and clave != "inteligencia":
        print("esa clave no existe")
        Flag_se_sanitiza = False

    if tipo_dato != "int" and tipo_dato != "float" and tipo_dato != "string":
        print("Tipo de dato no reconocido")
        Flag_se_sanitiza = False
    if Flag_se_sanitiza:
        match tipo_dato:
            case "string":
                for i in heroe:
                    sanitizado = sanitizar_strings(i[clave])
                    print(sanitizado)
                    if sanitizado == "string vacio":
                        print("Hubo un error con un un string vacio, revise la lista")
                return sanitizado
            case "int":
                for i in heroe:
                    sanitizado = sanitizar_entero(i[clave])
                return sanitizado
            case "float":
                for i in heroe:
                    sanitizado = sanitizar_flotante(i[clave])
                return sanitizado
# Verifica que no haya campos vacios o que este mal el tipo de dato
def stark_normalizar_datos(heroe:list)->None:
    contador_sanitisados = 0
    if len(heroe) > 0:
        for i in heroe:
            altura_sanitizada = sanitizar_flotante(i['altura'])
            peso_sanitizado = sanitizar_flotante(i['peso'])
            color_ojos_sanitizados = sanitizar_strings(i['color_ojos'])
            color_pelo_sanitizado = sanitizar_strings(i['color_pelo'])
            fuerza_sanitizado = sanitizar_entero(i['fuerza'])
            inteligencia_sanitizado = sanitizar_strings(i['inteligencia'])
            if altura_sanitizada != -3 and peso_sanitizado != -3 and color_ojos_sanitizados != "N/A" and color_pelo_sanitizado != "N/A" and fuerza_sanitizado != -3 and inteligencia_sanitizado != "N/A":
                contador_sanitisados += 1
        if contador_sanitisados == len(heroe):
            print("datos sanitizados")
        else:
            print("ERROR: Hay campos vacios en la lista verifique los campo ojos y pelo")
# Genera una lista con todos los nombres
def generar_indices_nombres(heroe:list)->list:
    lista = []
    for i in heroe:
        tipo = type(i)
        if tipo == dict and i['nombre'] != "":
            nombre = str(i['nombre'])
            nombre = nombre.split()
            lista.extend(nombre)
        else:
            lista = "El tipo de dato es incorrecto"
        lista.extend("/")
    return lista
# Muestra la lista de nombres pero arreglando ciertas imperfecciones
def stark_imprimir_indice_nombre(lista_nombre:list)->list:
    lista_nombres = str(lista_nombre)
    lista_nombres = lista_nombres.replace("[","").replace("]","").replace(",","-").replace("'","").replace(" ","").replace("/","")
    return lista_nombres
# Pasa de cm a metros
def convertir_cm_a_Mt(medida_cm:float)->float:
    medida_cm = float(medida_cm)
    if medida_cm > 0:
        medido_mt= medida_cm/100
        return medido_mt
    else:
        return -1
# Crea un separador para las fichas
def generar_separador(patron:str,largo:int,imprimir:bool)->str:
    if patron == "":
        return "N/A"
    elif largo > 0 and largo <= 235:
        cadena = patron*largo
        if imprimir:
            print(cadena)
    else:
        return "N/A"
    return cadena
# Genera un encabezado para las fichas
def generar_encabezado(titulo:str)->str:
    titulo = titulo.upper()
    cadena = generar_separador("*",235,False)
    Encabezado = cadena + "\n" + titulo + "\n" + cadena
    return Encabezado
# Imprime las fichas
def imprimir_ficha_heroe(heroe:list,lista_nombres,lista_genero_id)->None:
    lista_nombres = str(lista_nombres['iniciales']).replace("{","").replace("}","").replace("'","").replace(",","|")
    palabra = str(lista_genero_id['genero']).replace("{","").replace("}","").replace("'","").replace(",","|")
    palabra2 = str(lista_genero_id['Id']).replace("{","").replace("}","").replace("'","").replace(",","-")
    palabra2 = palabra2.zfill(8)
    f = generar_encabezado("PRINCIPAL")
    print(f)
    print("")
    print(f"    Nombre:            {heroe['nombre']} ({lista_nombres})")
    print("")
    print(f"    Identidad secreta: {heroe['identidad']}")
    print("")
    print(f"    Consultora:        {heroe['empresa']}")
    print("")
    print(f"    Codigo:            {palabra}-{palabra2}")
    s =generar_encabezado("FISICO")
    print(s)

    altura_metros = convertir_cm_a_Mt(heroe['altura'])
    print("")
    print(f"    Altura:            {altura_metros}Mtrs")
    print("")
    print(f"    Peso:              {heroe['peso']}Kg")
    print("")
    print(f"    Fuerza:            {heroe['fuerza']}N")
        
    g = generar_encabezado("SEÑAS PARTICULARES")
    print(g)

    print("")
    print(f"    Color Ojos:        {heroe['color_ojos']}")
    print("")
    print(f"    Color Pelo:        {heroe['color_pelo']}")

# Te permite navegar entre las fichas
def stark_Navegar_fichas(lista_personajes:list,Lista_genero_ID)->None:
    contador_indice_nombre = 0
    Lista_con_iniciales = definir_iniciales_nombre(lista_personajes)
    seguir = True
    imprmir = True
    while seguir:
        if imprmir:
            imprimir_ficha_heroe(lista_personajes[contador_indice_nombre],Lista_con_iniciales[contador_indice_nombre],Lista_genero_ID[contador_indice_nombre])
        print("Ingrese una de las siguientes opciones")
        respuesta = input("[1] ir a la izquierda         [2] ir a la derecha             [S] salir:  ")
        respuesta_sanitizada = sanitizar_entero(respuesta)
        match (respuesta_sanitizada):
            case 1:
                print("cambio")
                contador_indice_nombre -= 1
                imprmir = True
            case 2:
                contador_indice_nombre += 1
                imprmir = True
            case -1:
                seguir = False
                imprmir = True
            case -3:
                print("El campo no puede estar vacio")
                imprmir = False

# Menu proyecto strak 1
def Menu1(diccionario:dict)->None:
        while(True):
            os.system("cls")
            a = False
            lista_personajes = diccionario
            lista_normalizada = Normalizar_datos(lista_personajes)
            print("""
            **** Menu de opciones ****
            ------------------------------------------------------------------------------
            1- Mostrar todos los nombres
            2- Mostrar nombres y alturas
            3- Mostrar heroe mas alto
            4- Mostar heroe mas bajo
            5- Mostrar la altura promedio
            6- Mostrar heroe mas pesado y liviano
            S- Salir
            """)
            decision = input("Ingrese que opcion elige: ")
            respuesta_sanitizada = sanitizar_entero(decision)
            while decision == "":
                print("El campo no puede estar vacio")
                decision = (input("Ingrese la opcion devuelta: "))
                respuesta_sanitizada = sanitizar_entero(decision)

            match(respuesta_sanitizada):
                case 1:
                    Lista_nombres = ObtenerNombre(lista_personajes)
                    ImprimirDaTO(Lista_nombres)
                case 2:
                    Lista_strings = Convertir_Lista_Strings(lista_personajes,'nombre','altura')
                    ImprimirDaTO(Lista_strings)
                case 3:
                    heroe_alto = Mostrar_heroe_alto(lista_personajes,'altura','nombre')
                    altura_alta = Calcular_max_min(lista_personajes,'maximo','altura')
                    print(f"Nombre: {heroe_alto} |altura: {altura_alta}")
                case 4:
                    heroe_bajo = Mostrar_heroe_bajo(lista_personajes,'altura','nombre')
                    altura_mas_baja = Calcular_max_min(lista_personajes,'minimo','altura')
                    print(f"Nombre: {heroe_bajo} | altura: {altura_mas_baja}")
                case 5:
                    suma = SumarDatoHeroe(lista_personajes,'altura')
                    cantidad_heroes = Contar_heroes(lista_personajes)
                    Promedio_altura = Dividir(suma,cantidad_heroes)
                    print(f"La altura promedio es {Promedio_altura}")
                case 6:
                    heroe_pesado = Mostrar_heroe_alto(lista_personajes,'peso','nombre')
                    heroe_liviano = Mostrar_heroe_bajo(lista_personajes,'peso','nombre')

                    print(f"El heroe mas pesado es {heroe_pesado}, \nEl mas liviano es {heroe_liviano}")
                case -1:
                    break

            a = input("pause")
           
# Menu proyecto strak 2
def Menu2(diccionario:dict)->None:
    while(True):
            os.system("cls")
            a = False
            lista_personajes = diccionario
            lista_masculinos = [{}]
            lista_femeninos = [{}]
            lista_masculinos = Listar_heroes(lista_personajes,'M','genero')
            lista_femeninos = Listar_heroes(lista_personajes,'F','genero')
            print("""
            **** Menu de opciones ****
            ------------------------------------------------------------------------------
            1- Todos los superheroes de genero Masculino
            2- Todos los superheroes de genero Femenino
            3- El heroe masculino mas alto
            4-El heroe femenino mas alto
            5-El promedio de altura de los heroes
            6-El promedio de altura de las heroinas
            7-Informar cuantos heroes tiene cada color de ojos
            8-Informar cuantos heroes tiene cada color de pelo
            9-Cuantos heroes tienen cada tipo de inteligencia
            10-Agrupar los heroes por color de ojos
            11-Agrupar los heroes por color de pelo
            12-Agrupar los heroes por tipo de inteligencia
            S-Salir
            """)
            decision = input("Ingrese que opcion elige: ")
            respuesta_sanitizada = sanitizar_entero(decision)
            while decision == "":
                print("El campo no puede estar vacio")
                decision = (input("Ingrese la opcion devuelta: "))
                respuesta_sanitizada = sanitizar_entero(decision)
        
            match(respuesta_sanitizada):
                case 1:
                    Mostrar_Nombre(lista_masculinos,'nombre')
                case 2:
                    Mostrar_Nombre(lista_femeninos,'nombre')
                case 3:
                    heroe_alto = Mostrar_heroe_alto(lista_masculinos,'altura','nombre')
                    altura_alta = CalcularMax(lista_masculinos,'altura')
                    print(f"El heroe mascilino mas alto es: {heroe_alto}\nY su altura es: {altura_alta}")
                case 4:
                    heroe_alto = Mostrar_heroe_alto(lista_femeninos,'altura','nombre')
                    altura_alta = Calcular_max_min(lista_femeninos,'maximo','altura')
                    print(f"La heroina mas alta es: {heroe_alto}\nY su altura es: {altura_alta}") 
                case 5:
                    Promedio_altura = Calcular_promedios(lista_masculinos,'altura')
                    print(f"La altura promedio es: {Promedio_altura}") 
                case 6:
                    Promedio_altura = Calcular_promedios(lista_femeninos,'altura')
                    print(f"La altura promedio es: {Promedio_altura}")
                case 7:
                    lista_ojos = Contar_aislar_caracteristica(lista_personajes,'color_ojos')
                    Lista_sin_repetir= Sacar_Repetidos(lista_ojos)
                    Lista_dividida_ojos = Contar_caracteristica(Lista_sin_repetir,lista_personajes,'color_ojos')
                    Mostrar_color_diccionario(Lista_dividida_ojos)
                case 8:
                    lista_pelo = Contar_aislar_caracteristica(lista_personajes,'color_pelo')
                    Lista_sin_repetir_pelo= Sacar_Repetidos(lista_pelo)
                    Lista_dividida_pelo = Contar_caracteristica(Lista_sin_repetir_pelo,lista_personajes,'color_pelo')
                    Mostrar_color_diccionario(Lista_dividida_pelo)
                            
                case 9:
                    lista_inteligencia = Contar_aislar_caracteristica(lista_personajes,'inteligencia')
                    Lista_sin_repetir_inteligencia= Sacar_Repetidos(lista_inteligencia)
                    Lista_dividida_inteligencia = Contar_caracteristica(Lista_sin_repetir_inteligencia,lista_personajes,'inteligencia')
                    Mostrar_lista(Lista_dividida_inteligencia)
                case 10:
                    lista_ojos = Contar_aislar_caracteristica(lista_personajes,'color_ojos')
                    Lista_sin_repetir= Sacar_Repetidos(lista_ojos)
                    lista_nombres_ojos = Retornar_heroes_agrupados_por_carac(lista_personajes,Lista_sin_repetir,'color_ojos')
                    Mostrar_lista(lista_nombres_ojos)
                case 11:
                    lista_pelo = Contar_aislar_caracteristica(lista_personajes,'color_pelo')
                    Lista_sin_repetir_pelo= Sacar_Repetidos(lista_pelo)
                    lista_de_nombres_pelo = Retornar_heroes_agrupados_por_carac(lista_personajes,Lista_sin_repetir_pelo,'color_pelo')
                    Mostrar_lista(lista_de_nombres_pelo)
                        
                case 12:
                    lista_inteligencia = Contar_aislar_caracteristica(lista_personajes,'inteligencia')
                    Lista_sin_repetir_inteligencia= Sacar_Repetidos(lista_inteligencia)
                    Lista_nombre_inteligencia = Retornar_heroes_agrupados_por_carac(lista_personajes,Lista_sin_repetir_inteligencia,'inteligencia')
                    Mostrar_lista(Lista_nombre_inteligencia)
                case -1:
                    break

            a = input("pause")

#Menu proyecto strak 3
def Menu3(diccionario:dict)->None:
        while(True):
            os.system("cls")
            lista_personajes = diccionario
            primer_heroe_flag = True
            a = False
            lista_normalizada = Normalizar_datos(lista_personajes)
            Listas_Id = generar_Lista_con_id(lista_personajes)
            print("""
            **** Menu de opciones ****
            ------------------------------------------------------------------------------
            1 - Imprimir la lista de nombres junto con sus iniciales
            2 - Generar códigos de héroes
            3 - Normalizar datos
            4 - Imprimir índice de nombres
            5 - Navegar fichas
            S - Salir
            """)
            decision = input("Ingrese que opcion elige: ")
            respuesta_sanitizada = sanitizar_entero(decision)
            while decision == "":
                print("El campo no puede estar vacio")
                decision = (input("Ingrese la opcion devuelta: "))
                respuesta_sanitizada = sanitizar_entero(decision)

            match(respuesta_sanitizada):
                case 1:
                    Lista_con_iniciales = definir_iniciales_nombre(lista_personajes)
                    for i in Lista_con_iniciales:
                        palabras = str(i['iniciales']).replace("{","").replace("}","").replace("'","").replace(",","|")
                        print(f"* {i['nombre']}, ({palabras})")
                case 2:
                    Lista_genero_ID = sacar_id_genero(Listas_Id)
                    Ultimo = len(Lista_genero_ID)
                    print("## codigos generados")
                    if len(Lista_genero_ID) == 0:
                        print("La lista esta vacia no se puede imprimier")
                    else:
                        for i in Lista_genero_ID:
                            palabra = str(i['genero']).replace("{","").replace("}","").replace("'","").replace(",","|")
                            palabra2 = str(i['Id']).replace("{","").replace("}","").replace("'","").replace(",","-")
                            palabra2 = palabra2.zfill(8)
                            if primer_heroe_flag:
                                print(f"*El código del primer héroe:{palabra} - {palabra2}")
                                primer_heroe_flag = False
                            elif Ultimo == i['Id']:
                                print(f"*El código del ultimo héroe:{palabra} - {palabra2}")
                            else:
                                print(f"{palabra} - {palabra2}")

                case 3:
                    stark_normalizar_datos(lista_personajes)
                case 4:
                    lista_nombres_unidos = generar_indices_nombres(lista_personajes)
                    p = stark_imprimir_indice_nombre(lista_nombres_unidos)
                    print(p)
                case 5:
                    Lista_genero_ID = sacar_id_genero(Listas_Id)
                    stark_Navegar_fichas(lista_personajes,Lista_genero_ID)

                case -1:
                   break
            a = input("pause")


# Menu general de la aplicacion
def Stark_Marvel_app(diccionaro:dict)->None:
    while True:
        os.system("cls")
        print("""
        **** Menu de opciones ****
            1 Para ver el Stark 0
            2 Para ver el Stark 1
            3 Para ver el Stark 3
            """)
        
        decision = (input("Ingrese que opcion elige: "))
        a = EsUnNuero(decision)
        while decision == "" or a == True:
            print("El campo no puede estar vacio")
            decision = (input("Ingrese la opcion devuelta: "))
            a = EsUnNuero(decision)
        else:
            decision = int(decision)
            match(decision):
                case 1:
                    Menu1(lista_personajes)
                case 2:
                    Menu2(lista_personajes)
                case 3:
                    Menu3(lista_personajes)
                case "":
                    print("El campo no puede estar vacio")

