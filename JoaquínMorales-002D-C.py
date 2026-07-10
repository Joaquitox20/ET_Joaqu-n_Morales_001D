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
            case 6:
                print ("Programa finalizado.")
                break