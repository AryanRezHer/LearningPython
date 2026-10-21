"""
---
PROYECTO  Tic-Tac-Toe
---

Escenario
Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
la maquina responde con su movimiento y se verifica el estado del juego;
no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.


Requerimientos
Implementa las siguientes características:

el tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

board[row][column]
 

cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro (dicho cuadro se considera como libre)
la apariencia de tablero debe de ser igual a la presentada en el ejemplo.
implementa las funciones definidas para ti en el editor.

Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

Nota: la instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.
from random import randrange
 
for i in range(10):
    print(randrange(8))
"""

from random import randrange

move = 0
board = [
                            [1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]
                        ]
sign2 = False

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("Tablero actual:")
    print("\n")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("\n")


def enter_move(board):
    global move
    fila = 10000000
    columna = 10000000
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while fila > 2 or columna > 2 or fila < 0 or columna < 0:
        fila = int(input("¿En que fila te gustaría añadir tu O?"))
        columna = int(input("¿En que columna te gustaría añadir tu O?"))
        if fila < 3 and columna < 3 and fila > -1 and columna > -1:
            if (fila, columna) not in make_list_of_free_fields(board):
                print("Casilla ocupada vulvelo a intentar")
                fila = 100000
            else:
                board[fila][columna] = "O"
                victory_for(board, False)
                move += 1
                break
            
def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    list_of_free_fields = [
                            (0,0), (0,1), (0,2),
                            (1,0), (1,1), (1,2),
                            (2,0), (2,1), (2,2)
                        ]
    for row in range(0,len(board)):
        for i in range(0,len(board)):
            if board[row][i] == "O" or board[row][i] == "X":
                if row == 0  and i == 0:
                    list_of_free_fields[0] = ""
                elif row == 0  and i == 1:
                    list_of_free_fields[1] = ""
                elif row == 0  and i == 2:
                    list_of_free_fields[2] = ""
                elif row == 1  and i == 0:
                    list_of_free_fields[3] = ""
                elif row == 1  and i == 1:
                    list_of_free_fields[4] = ""
                elif row == 1  and i == 2:
                    list_of_free_fields[5] = ""
                elif row == 2  and i == 0:
                    list_of_free_fields[6] = ""
                elif row == 2  and i == 1:
                    list_of_free_fields[7] = ""
                else:
                    list_of_free_fields[8] = ""
    return list_of_free_fields

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    global sign2
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" \
    or board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" \
    or board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" \
    or board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("Has ganado a la máquina, Enhorabuena!!")
        sign2 = True
        return sign
    elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" \
    or board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" \
    or board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" \
    or board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" \
    or board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X" \
    or board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" \
    or board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" \
    or board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("Perdiste ante la máquina, vuelve a intentarlo")
        sign2 = True
        return sign
    elif move == 9:
        print("EMPATEE vuelve a intentarlo")
        sign2 = True
        return sign
    else:
        return sign
def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    global move
    while True:
        if move == 0:
            board[1][1] = "X"
            move += 1
            break
        elif move % 2 == 0:
            fila = randrange(3)
            columna = randrange(3)
            if (fila, columna) not in make_list_of_free_fields(board):
                print("La maquina escogió una Casilla ocupada vulvelo a intentar")
            else:
                board[fila][columna] = "X"
                move += 1
                victory_for(board, False)
                break
        else:
            break
    


while True:
    display_board(board)
    if sign2 == False:
        draw_move(board)
        display_board(board)
        if victory_for(board, sign2) == True:
            break
        enter_move(board)
    else:
        break
