import random
import csv
from statistics import geometric_mean

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez" ]
sueldos = {}

def sueldos_aleatorios():
    global sueldos
    sueldos = {}
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        sueldos[trabajador] = sueldo
        print(f"Trabajador: {trabajador}, Sueldo: ${sueldo}")

def clasificar_sueldos():
        clasificaciones = {
        "Menor a $800.000" :[],
        "Entre $800.000 y $2.000.000":[],
        "Mayor a $2.000.000":[],
        }

        for trabajador , sueldo in sueldos.items():
            if not sueldos:
                print("Debe asignarles un suelo aleatoriamente en la Opcion 1")
            elif sueldo < 800000:
                clasificaciones["Menor a $800.000"].append((trabajador,sueldo))
            elif sueldo >= 80000 and sueldo < 2000000:
                clasificaciones["Entre $800.000 y $2.000.000"].append((trabajador,sueldo))
            elif sueldo > 2000000:
                clasificaciones["Mayor a $2.000.000"].append((trabajador,sueldo))
        
        for clasificacion, lista_sueldo in clasificaciones.items():
            print(f"\n{clasificacion}")
            for trabajador, sueldo in lista_sueldo:
                print(f"Trabajador: {trabajador} \nSueldo: $ {sueldo}")

def ver_estadisticas():
        sueldo_lista = list(sueldos.values())
        sueldo_maximo = max(sueldo_lista)
        sueldo_minimo = min(sueldo_lista)
        promedio = sum(sueldo_lista)/len(sueldo_lista)
        media = geometric_mean(sueldo_lista)

        print(f"Sueldo Maximo: ${sueldo_maximo}\n")
        print(f"Sueldo Minimo: ${sueldo_minimo}\n")
        print(f"Promedio: ${promedio:.2f}\n")
        print(f"Media: ${media:.2f}")

                     
def main():
    while True:
        print("Menu")
        print("1. Asignar Sueldos Aleatoriamnte")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion = input("Ingese Una Opcion ")

        if opcion == "1":
            sueldos_aleatorios()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        else:
            opcion == "5"
            print("Finalizando programa....")
            print("Desarrollado por Diego Carrillo Webar")
            print("RUT: 19.028.319-4")
            break
        
main()