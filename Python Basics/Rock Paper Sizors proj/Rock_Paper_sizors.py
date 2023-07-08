import random as rn
print('BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA, GANA EL QUE APLASTE A SU ENEMIGO POR MÁS DE DOS JUEGOS')
def main():
    contador_user = 0
    contador_pc = 0
    rounds = 1
    while abs(contador_user-contador_pc) != 2:
        print(f'ROUND {rounds}')
        print('**********')
        pc_options = ('piedra','papel', 'tijera')
        user_input = EntradaUsuario(pc_options)
        pc_input = EntradaPc(pc_options)
        result = Resultatos(user_input,pc_input)
        if result == True:
            contador_user += 1
        elif result == False:
            contador_pc += 1
        rounds += 1
        print(f'Usuario victorias => {contador_user}')
        print(f'PC victorias => {contador_pc}')
    if (contador_user-contador_pc) == 2:
        print("Felicidades, has vencido a la computadora!")
    elif (contador_pc-contador_user) == 2:
        print("No has logrado vencerme :(")

#Recolección de la entrada del usuario
def EntradaUsuario(pc_options):
    user = input('Ingresa piedra, papel o tijera: ')
    user = user.lower()
    while user not in pc_options:
        user = input('Dato no válido, Ingresa piedra, papel o tijera: ')
        user = user.lower()
    return user

#Elección de la PC
def EntradaPc(pc_options):
    pc_choice = rn.choice(pc_options)
    print('La PC ha elegido',pc_choice)
    return pc_choice

#Función para definir el resultado
def Resultatos(user_input,pc_input):
    if user_input == pc_input:
        print('EMPATE!')
        return None
    elif user_input == 'piedra' and pc_input == 'tijera':
        print('HAS GANADO! :)' )
        return True
    elif user_input == 'papel' and pc_input == 'piedra':
        print('HAS GANADO! :)' )
        return True
    elif user_input == 'tijera' and pc_input == 'papel':
        print('HAS GANADO! :) ')
        return True
    else:
        print('PERDISTE:(')
        return False

main()

