def mostrar_menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================
""")
    
def leer_opcion():
    while True:
        try:
            opc = int(input("Ingrese la opción: "))
        except ValueError:
            print ("La opción debe ser un número.")
        else:
            if opc >=1 and opc <=6:
                return opc
            else:
                print ("La opción debe ser un número entre 1 y 6.")

def validar_nombre_plan(nombre_plan):
    if nombre_plan.strip != "":
        return True
    else:
        return False
    
def validar_tipo(tipo):
    if tipo == "mensual".lower or tipo == "trismestral".lower or tipo == "anual".lower:
        return True
    else:
        return False
    
def validar_duracion_meses(duracion_meses):
    if duracion_meses >0:
        return True
    else:
        return False
    
def validar_acceso_piscina(acceso_piscina):
    if acceso_piscina == "s".lower:
        return True
    else:
        if acceso_piscina == "n".lower:
            return False

def validar_incluye_clases(incluye_clases):
    if incluye_clases == "s".lower:
        return True
    else:
        if incluye_clases == "n".lower:
            return False

def validar_horario(horario):
    if horario.strip != "":
        return True
    else:
        return False
    
def validar_precio(precio):
    if precio >0:
        return True
    else:
        return False
    
def validar_cupos(cupos):
    if cupos >=0:
        return True
    else:
        return False
    
def busqueda_precio(p_min, p_max):
    while True:
        try:
            p_min = int(input("Ingrese precio mínimo: "))
        except ValueError:
            print ("Debe ingresar valores enteros.")
        else:
            if validar_precio == True:
                break
            else:
                print ("El valor ingresado debe ser mayor a 0.")
                continue
        
    while True:
        try:
            p_max = int(input("Ingrese precio máximo: "))
        except ValueError:
            print ("Debe ingresar valores enteros.")
        else:
            if validar_precio == True:
                break
            else:
                print ("El valor ingresado debe ser mayor a 0.")
                continue

def actualizar_precio(codigo, nuevo_precio):
    codigo = input("Ingrese código del plan: ")
    nuevo_precio = int(input("Ingrese nuevo precio: "))
    print ("El código no existe.")
    print ("Desea actualizar otro precio (s/n)?: ")

def main():
    planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
    }

    inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15],
    }

    while True:
        mostrar_menu()
        opc = leer_opcion()
        match opc:
            case 1:
                tipo = input("Ingrese el tipo de plan a consultar: ")
            case 2:
                    while True:
                        try:
                            p_min = int(input("Ingrese precio mínimo: "))
                        except ValueError:
                             print ("Debe ingresar valores enteros.")
                        else:
                            if validar_precio == True:
                                break
                            else:
                                print ("El valor ingresado debe ser mayor a 0.")
                                continue
        
                    while True:
                        try:
                            p_max = int(input("Ingrese precio máximo: "))
                        except ValueError:
                            print ("Debe ingresar valores enteros.")
                        else:
                            if validar_precio == True:
                                break
                            else:
                                print ("El valor ingresado debe ser mayor a 0.")
                                continue
                                busqueda_precio(p_min, p_max)
            case 3:
                actualizar_precio()
            case 4:
                codigo = input("Ingrese código del plan: ")
                nombre_plan = input("Ingrese nombre del plan: ")
                tipo = input("Ingrese tipo (mensual/trimestral/anual): ")
                duracion_meses = int(input("Ingrese duración (meses): "))
                acceso_piscina = input("¿Incluye acceso a piscina? (s/n): ")
                incluye_clases = input("¿Incluye clases grupales? (s/n): ")
                horario = input("Ingrese horario: ")
                precio = int(input("Ingrese precio: "))
                cupos = int(input("Ingrese cupos: "))
                print ("Plan agregado")
            case 5:
                input("Ingrese el plan a eliminar: ")        
            case 6:
                print ("Programa finalizado.")
                break

main()