# Rock, Paper, Scissors

def menu():
    option = input("""Welcome to rock, paper scissors!
    If you wish to leave just type "quit".
    Do you know the rules? [y/n]: """)
    while option != 'quit':
        if option == 'y':
            print('Great! You are ready to start.')
            b = int(input('Select a game mode [0 = Main menu / 1 = One game / 2 = 2/3 to win: '))
            while b != 0:
                if b == 1:
                    player_one = input('Player 1, choose: ')
                    player_two = input('Player 2, choose: ')
                    return single_game(player_one.lower(), player_two.lower())
                elif b == 2:
                    return multi_game()
                else:
                    print('Please enter a valid option.')
                b = int(input('Select a game mode [0 = Main menu / 1 = One game / 2 = 2/3 to win: ' ))
            print('Main Menu.')
        elif option == 'n':
            print('''Okay, This are the rules:
            1.- You need to choose one of this options: Rock, Paper o Scissors.
            2.- Rock wins against scissors, paper wins against rock and scissors win against paper.
            3.- "One game" mode. The first one to beat the other wins.
            4.- "2/3 to win" mode. The first one to beat 2 out of 3 games wins.''')
            b = int(input('Select a game mode [0 = Main menu / 1 = One game / 2 = 2/3 to win: '))
            while b != 0:
                if b == 1:
                    player_one = input('Player 1, choose: ')
                    player_two = input('Player 2, choose: ')
                    return single_game(player_one.lower(), player_two.lower())
                elif b == 2:
                    return multi_game()
                else:
                    print('Please enter a valid option.')
                b = int(input('Select a game mode [0 = Main menu / 1 = One game / 2 = 2/3 to win: '))
            print('Main Menu.')
        else:
            print('Please enter a valid option.')
        option = input('Do you know the rules? [y/n]: ')
    print('See you later!')

def single_game(option_one, option_two):
    if option_one == option_two:
        print("It's a tie!")
        option = input('Would you like to play again? [y/n]: ')
        while option != 'n':
            if option == 'y':
                player_one = input('Player 1, choose: ')
                player_two = input('Player 2, choose: ')
                return single_game(player_one.lower(), player_two.lower())
            else:
                print('Please enter a valid option')
                option = input('Would you like to play again? [y/n]: ')
        print('See you later!')
    elif (option_one == 'rock' and option_two == 'paper') or (option_one == 'paper' and option_two == 'scissors') or (option_one == 'scissors' and option_two == 'rock'):
        print('Player 2 wins!')
        option = input('Would you like to play again? [y/n]: ')
        while option != 'n':
            if option == 'y':
                player_one = input('Player 1, choose: ')
                player_two = input('Player 2, choose: ')
                return single_game(player_one.lower(), player_two.lower())
            else:
                print('Please enter a valid option')
                option = input('Would you like to play again? [y/n]:')
        print('See you later!')
    elif (option_one == 'rock' and option_two == 'scissors') or (option_one == 'paper' and option_two == 'rock') or (option_one == 'scissors' and option_two == 'paper'):
        print('Player 1 wins!')
        option = input('Would you like to play again? [y/n]: ')
        while option != 'n':
            if option == 'y':
                player_one = input('Player 1, choose: ')
                player_two = input('Player 2, choose: ')
                return single_game(player_one.lower(), player_two.lower())
            else:
                print('Please enter a valid option')
                option = input('Would you like to play again? [y/n]: ')
        print('See you later!')
    else:
        print('Please enter a valid option')
        player_one = input('Pleayer 1, choose: ')
        player_two = input('Player 2, choose: ')
        return single_game(player_one.lower(), player_two.lower())
        
def multi_game():
    print('If you wish to leave both players type "quit".')
    player_one = input('Player 1, choose: ')
    player_two = input('Player 2, choose: ')
    counter_player1 = 0
    counter_player2 = 0
    while player_one != 'quit' or player_two != 'quit':
        if player_one == player_two:
            print("It's a tie!")
        elif (player_one == 'rock' and player_two == 'paper') or (player_one == 'paper' and player_two == 'scissors') or (player_one == 'scissors' and player_two == 'rock'):
            print("Point for player 2!") 
            counter_player2 += 1
            if counter_player2 == 2:
                return winner(counter_player1, counter_player2)
        elif (player_one == 'rock' and player_two == 'scissors') or (player_one == 'paper' and player_two == 'rock') or (player_one == 'scissors' and player_two == 'paper'):
            print ("Point for palyer 1!")
            counter_player1 += 1
            if counter_player1 == 2:
                return winner(counter_player1, counter_player2)       
        else:
            print('Please enter a valid option.') 
        player_one = input('Player 1, choose: ')
        player_two = input('Player 2, choose: ')
    print('See you later!')


def winner(counter1, counter2):
    if counter1 > counter2:
        print('Player 1 won!')
        print(f'Player 1: {counter1} \t Player 2: {counter2}')
        a = input('Want to play again? [y/n]: ')
        while a != 'n':
            if a == 'y':
                return multi_game()
            else:
                print('Please enter a valid option.')
                a = input('Want to play again? [y/n]: ')
        print('See you later!')
    elif counter2 > counter1: 
        print('Player 2 won!')
        print(f'Player 1: {counter1} \t Player 2: {counter2}')
        a = input('Want to play again? [y/n]: ')
        while a != 'n':
            if a == 'y':
                return multi_game()
            else:
                print('Please enter a valid option.')
                a = input('Want to play again? [y/n]: ')
        print('See you later!')
    

menu()