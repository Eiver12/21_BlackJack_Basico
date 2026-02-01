import random
import time


def menu():

    print("\n21 BLACKJACK")
    print("1. Jugar")
    print("2. Salir")


def submenu():
    print("\n21 BLACKJACK")
    print("1. Repartir cartas")
    print("2. Salir")
    
def submenu_1():
    
    print("\n21 BLACKJACK")
    print("1. Otra Carta")
    print("2. Quedarse")
    print("3. Salir")
    


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
    
    if accion == 'primero':

        carta_1 = random.choice(list(baraja.keys()))
        carta_2 = random.choice(list(baraja.keys()))
        
        puntos_card1 = baraja[carta_1]
        puntos_card2 = baraja[carta_2]
        
        puntos_totales = puntos_card1 + puntos_card2

        return carta_1, carta_2, puntos_card1, puntos_card2, puntos_totales #!tupla para desempaquetar
    
    elif accion == 'segundo':
        
        segunda_carta = random.choice(list(baraja.keys()))
        
        puntos_segunda_carta = baraja[segunda_carta]
        
        return segunda_carta, puntos_segunda_carta


def juego():

    while True:
        submenu()
        global contador

        try:
            seleccion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("\nSelección no valida")

        if seleccion == 1:

            print("\nRepartiendo cartas...")
            time.sleep(2)
            carta_1j, carta_2j, puntos_card1j, puntos_card2j, puntos_totalesj = repartir_cartas('primero')
            print(f"\nTus Cartas: {carta_1j}, {carta_2j}\nPuntos parciales: {puntos_card1j}, {puntos_card2j}\nPuntos totales: {puntos_totalesj}\nPartidas Ganadas: {contador}")

            print("\nRepartiendo cartas...")
            time.sleep(2)
            carta_1d, carta_2d, puntos_card1d, puntos_card2d, puntos_totalesd = repartir_cartas('primero')
            print(f"\nCartas Dealer: {carta_1d}, Carta oculta\nPuntos parciales: {puntos_card1d}")
            
            if puntos_totalesj == 21:
                contador += 1
                print("\n21 BlackJack")
                print("GANAS")
            elif puntos_totalesj > 21:
                print("\nPIERDES")
                print("GAME OVER")
                
            else:
                submenu_1()
                try:
                    seleccion_2 = int(input("\nSeleccione una opcion:  "))
                    
                except ValueError:
                    print("\nseleccion incorrecta")
                    
                if seleccion_2 == 1:
                    print("\nRepartiendo cartas...")
                    time.sleep(2)
                    nueva_carta, puntaje_nueva_carta = repartir_cartas("segundo")
                    nuevo_puntaje = puntaje_nueva_carta + puntos_totalesj
                    print(f"\nTus Cartas: {carta_1j}, {carta_2j}, {nueva_carta}\nPuntos parciales: {puntos_card1j}, {puntos_card2j}, {puntaje_nueva_carta}\nPuntos totales: {nuevo_puntaje}\nPartidas Ganadas: {contador}")
                    
                    if nuevo_puntaje > 21:
                        print("\nGAME OVER")
                    elif nuevo_puntaje == 21:
                        contador += 1
                        print("\n21 BlackJack")
                        
                    else:
                        print("\nRevelando carta dealer....")
                        time.sleep(2)
                        print(f"\nCartas Dealer: {carta_1d}, {carta_2d}\nPuntos parciales: {puntos_card1d}, {puntos_card2d}\nPuntos totales: {puntos_totalesd}")
                        
                        if nuevo_puntaje < puntos_totalesd:
                            print("\nPIERDES")
                            print('GAME OVER')
                            
                        elif puntos_totalesd == 21:
                            print("\n21 BlackJack Dealer")
                            print("PIERDES")
                        else:
                            print("\nGANAS")
                elif seleccion_2 == 2:
                    print(f"\nTus Cartas: {carta_1j}, {carta_2j}\nPuntos parciales: {puntos_card1j}, {puntos_card2j}\nPuntos totales: {puntos_totalesj}\nPuntos totales: {puntos_totalesj}\nPartidas Ganadas: {contador}")
                    
                    print("\nRevelando carta dealer....")
                    time.sleep(2)
                    print(f"\nCartas Dealer: {carta_1d}, {carta_2d}\nPuntos parciales: {puntos_card1d}, {puntos_card2d}\nPuntos totales: {puntos_totalesd}")
                    
                    
                    if puntos_totalesj > puntos_totalesd:
                        contador += 1
                        print("\nGANASTE")
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
        menu()

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
            print("\nSaliendo del juego")
            break
        else:
            print("\nOpcion no valida")


if __name__ == "__main__":
    main()
    print("todo se ejecuta desde aqui")
