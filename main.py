import random
import time


def menu(accion):

    if accion == 'principal':
        print("\n21 BLACKJACK")
        print("1. Jugar")
        print("2. Salir")
        
    elif accion == 'partida':
        print("\n21 BLACKJACK")
        print("1. Repartir cartas")
        print("2. Salir")
        
    elif accion == '2fase':
        print("\n21 BLACKJACK")
        print("1. Otra Carta")
        print("2. Quedarse")
        print("3. Salir")
def submenu():
    pass
    
def submenu_1():
    pass
    
    


def repartir_cartas(accion):
    baraja = {
    # Corazones (corazones)
    "Acorazones": 11, "2corazones": 2, "3corazones": 3, "4corazones": 4, "5corazones": 5,
    "6corazones": 6, "7corazones": 7, "8corazones": 8, "9corazones": 9, "10corazones": 10,
    "Jcorazones": 10, "Qcorazones": 10, "Kcorazones": 10,

    # Diamantes (diamantes)
    "Adiamantes": 11, "2diamantes": 2, "3diamantes": 3, "4diamantes": 4, "5diamantes": 5,
    "6diamantes": 6, "7diamantes": 7, "8diamantes": 8, "9diamantes": 9, "10diamantes": 10,
    "Jdiamantes": 10, "Qdiamantes": 10, "Kdiamantes": 10,

    # Tréboles (treboles)
    "Atreboles": 11, "2treboles": 2, "3treboles": 3, "4treboles": 4, "5treboles": 5,
    "6treboles": 6, "7treboles": 7, "8treboles": 8, "9treboles": 9, "10treboles": 10,
    "Jtreboles": 10, "Qtreboles": 10, "Ktreboles": 10,

    # Picas (picas)
    "Apicas": 11, "2picas": 2, "3picas": 3, "4picas": 4, "5picas": 5,
    "6picas": 6, "7picas": 7, "8picas": 8, "9picas": 9, "10picas": 10,
    "Jpicas": 10, "Qpicas": 10, "Kpicas": 10
}
    lista_azes = ['Acorzacones', 'Adiamantes', 'Atreboles', 'Apicas']
    
    if accion == 'primero':

        carta_1 = random.choice(list(baraja.keys()))
        carta_2 = random.choice(list(baraja.keys()))
        
        if carta_1 in lista_azes:
        
            puntos_carta1 = baraja[carta_1]
            puntos_carta2 = baraja[carta_2]
        
            puntos_parciales_a = puntos_carta1 + puntos_carta2
            puntos_parciales_b = puntos_carta2 + 1

            return carta_1, carta_2, puntos_carta1, puntos_carta2, puntos_parciales_a, puntos_parciales_b #!tupla para desempaquetar
        
        elif carta_2 in lista_azes:
            
            puntos_carta1 = baraja[carta_1]
            puntos_carta2 = baraja[carta_2]
            
            puntos_parciales_a = puntos_carta1 + puntos_carta2
            puntos_parciales_b = puntos_carta1 + 1
            
            return carta_1, carta_2, puntos_carta1, puntos_carta2, puntos_parciales_a, puntos_parciales_b
        
        elif carta_2 in lista_azes and carta_1 in lista_azes:
            
            puntos_carta1 = baraja[carta_1]
            puntos_carta2 = baraja[carta_2]
            
            puntos_parciales_a = puntos_carta1 + puntos_carta2
            puntos_parciales_b = 1 + 1
            
            return carta_1, carta_2, puntos_carta1, puntos_carta2, puntos_parciales_a, puntos_parciales_b
            
        else:
            puntos_carta1 = baraja[carta_1]
            puntos_carta2 = baraja[carta_2]
            
            puntos_parciales_a = puntos_carta1 + puntos_carta2
            puntos_parciales_b = 0
            
            return carta_1, carta_2, puntos_carta1, puntos_carta2, puntos_parciales_a, puntos_parciales_b
        
    elif accion == 'segundo':
        
        segunda_carta = random.choice(list(baraja.keys()))
        
        puntos_segunda_carta = baraja[segunda_carta]
        
        return segunda_carta, puntos_segunda_carta


def juego():

    while True:
        menu('partida')
        global contador

        try:
            seleccion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("\nSelección no valida")

        if seleccion == 1:
            print("\n1 FASE")
            print("----------")
            print("\nRepartiendo cartas...")
            time.sleep(2)
            carta_1j, carta_2j, puntos_carta_1j, puntos_carta2j, puntos_parcialesaj, puntos_parcialesbj = repartir_cartas('primero')
            print(f"""
                --------------------------------------------------
                Tus Cartas: {carta_1j}, {carta_2j}
                * Puntos Cartas: {puntos_carta_1j}, {puntos_carta2j}
                * Puntos Parciales a: {puntos_parcialesaj}
                * Puntos Parciales b: {puntos_parcialesbj}
                ----------------------------------------------------
                Partidas Ganadas: {contador}""")

            print("\nRepartiendo cartas...")
            time.sleep(2)
            carta_1d, carta_2d, puntos_carta1d, puntos_carta2d, puntos_parcialesad, puntos_parcialesbd = repartir_cartas('primero')
            print(f"""
                -----------------------------------------
                * Cartas Dealer: {carta_1d}, Carta oculta
                * Puntoa Cartas: {puntos_carta1d}, oculto
                * Puntos parciales a: {puntos_carta1d}
                -------------------------------------------""")
            
            if puntos_parcialesaj == 21 or puntos_parcialesbj == 21:
                contador += 1
                print("\n21 BlackJack")
                print("GANAS")
                
            elif puntos_parcialesaj > 21 or puntos_parcialesbj > 21:
                print("\nmayor a 21")
                print("PIERDES")
                print("GAME OVER")
                
                
            else:
                menu('2fase') #! seguir jugando
                try:
                    seleccion_2 = int(input("\nSeleccione una opcion:  "))
                    
                except ValueError:
                    print("\nSeleccion incorrecta")
                    
                if seleccion_2 == 1: #! Repartir otra carta
                    print("\n2 FASE")
                    print("----------")
                    print("OTRA CARTA")
                    print("\nRepartiendo cartas...")
                    time.sleep(2)
                    nueva_carta, puntaje_nueva_carta = repartir_cartas("segundo")
                    nuevo_puntajea = puntaje_nueva_carta + puntos_parcialesaj
                    if puntos_parcialesbj:
                        nuevo_puntajeb = puntaje_nueva_carta + puntos_parcialesbj
                    else:
                        nuevo_puntajeb = 0
                    print(f"""
                        -----------------------------------------------------
                        Tus Cartas: {carta_1j}, {carta_2j}, {nueva_carta}
                        Puntos Cartas: {puntos_carta_1j}, {puntos_carta2j}, {puntaje_nueva_carta}
                        Puntaje total a: {nuevo_puntajea}
                        Puntaje total b: {nuevo_puntajeb}
                        --------------------------------------------------------
                        Partidas Ganadas: {contador}""")
                    
                    if nuevo_puntajea > 21 or nuevo_puntajeb > 21:
                        print("\nPIERDES")
                        print("GAME OVER")
                    elif nuevo_puntajea == 21 or nuevo_puntajeb == 21:
                        contador += 1
                        print("\n21 BlackJack")
                        print("\n GANAS")
                        
                    else:
                        print("\nRevelando carta dealer....")
                        time.sleep(2)
                        print(f"""
                            -----------------------------------------------
                            Cartas Dealer: {carta_1d}, {carta_2d}
                            Puntos parciales: {puntos_carta1d}, {puntos_carta2d}
                            Puntos totales a: {puntos_parcialesad}
                            Puntos totales b: {puntos_parcialesbd}
                            ---------------------------------------------------""")
                        
                        if nuevo_puntajeb == 0 and puntos_parcialesbd == 0:
                            if nuevo_puntajea > puntos_parcialesad:
                                contador += 1
                                print("\nGANAS")
                                print('GAME OVER')
                            else:
                                print("\nPIERDES")
                                print('GAME OVER')
                        elif nuevo_puntajeb != 0 and puntos_parcialesbd == 0:
                            if nuevo_puntajea > puntos_parcialesad or nuevo_puntajeb > puntos_parcialesad:
                                contador += 1
                                print("\nGANAS")
                                print('GAME OVER')
                            else:
                                print("\nPIERDES")
                                print('GAME OVER')
                                
                        elif nuevo_puntajeb == 0 and puntos_parcialesbd != 0:
                            if nuevo_puntajea > puntos_parcialesad or nuevo_puntajea > puntos_parcialesbd:
                                contador += 1
                                print("\nGANAS")
                                print('GAME OVER')
                            else:
                                print("\nPIERDES")
                                print('GAME OVER')
                                
                        elif puntos_parcialesad == 21 or puntos_parcialesbd == 21:
                            print("\n21 BlackJack Dealer")
                            print("PIERDES")
                        else:
                            print("\npierdes")
                            
                elif seleccion_2 == 2:
                    print("\n2 FASE")
                    print("----------")
                    print("QUEDARSE")
                    print(f"""
                        ---------------------------------------------------
                        * Tus Cartas: {carta_1j}, {carta_2j}
                        * Puntos Cartas: {puntos_carta_1j}, {puntos_carta2j}
                        * Puntos Totales a: {puntos_parcialesaj}
                        * Puntos Totales b: {puntos_parcialesbj}
                        ---------------------------------------------------
                        Partidas Ganadas: {contador}""")
                    
                    print("\nRevelando carta dealer....")
                    time.sleep(2)
                    print(f"""
                        ----------------------------------------------------
                        * Cartas Dealer: {carta_1d}, {carta_2d}
                        * Puntos Cartas: {puntos_carta1d}, {puntos_carta2d}
                        * Puntos Totales a: {puntos_parcialesad}
                        * Puntos Totales b: {puntos_parcialesbd}
                        -----------------------------------------------------""")
                    
                    if puntos_parcialesaj == 21 or puntos_parcialesbj == 21:
                        contador += 1
                        print("\nBlackJack!")
                        print("\nGANAS")
                        print('GAME OVER')
                    
                    elif puntos_parcialesbj == 0 and puntos_parcialesbd == 0:
                        if  puntos_parcialesaj > puntos_parcialesad:
                            contador += 1
                            print("\nGANAS")
                            print('GAME OVER')
                        else:
                            print("\nPIERDES")
                            print('GAME OVER')
                            
                    elif puntos_parcialesbj != 0 and puntos_parcialesbd == 0:
                        if puntos_parcialesaj > puntos_parcialesad or puntos_parcialesbj > puntos_parcialesad:
                            contador += 1
                            print("\nGANAS")
                            print('GAME OVER')
                        else:
                            print("\nPIERDES")
                            print('GAME OVER')
                            
                    elif puntos_parcialesbj == 0 and puntos_parcialesbd != 0:
                        if puntos_parcialesaj > puntos_parcialesad or puntos_parcialesaj > puntos_parcialesbd:
                            contador += 1
                            print("\nGANAS")
                            print('GAME OVER')
                        else:
                            print("\nPIERDES")
                            print('GAME OVER')
                            
                    elif puntos_parcialesad == 21 or puntos_parcialesbd == 21:
                            print("\nBlackJack dealer")
                            print("\nPIERDES")
                            print('GAME OVER')
                    else:
                            print("\nPIERDES")
                
                
                elif seleccion_2 == 3:
                    print("GAME OVER")
                    print("Saliendo de la partida...")
                    time.sleep(2)
                    break
                else:
                    print("\nSeleccion no valida")

        elif seleccion == 2:
            print("\nGAME OVER")
            break
        else:
            print("\nSelección no valida")

contador = 0

def main():
    
    while True:
        menu('principal')

        try:
            opcion = int(input("\nSeleccione un opción: "))

        except ValueError:
            print("\nOpcion no valida")
            #continue

        if opcion == 1:
            print("\nIniciando juego...")
            time.sleep(1)
            juego()
        elif opcion == 2:
            print("\nSaliendo del juego...")
            break
        else:
            print("\nOpcion no valida")


if __name__ == "__main__":
    main()
    print("todo se ejecuta desde aqui")
