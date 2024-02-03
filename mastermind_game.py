import random

#####
def displayCorrectNumbers(random_num: str, usrGuess: str) -> None:
    for i in range(len(usrGuess)):
        print(usrGuess[i] if usrGuess[i] == random_num[i] else 'X', end=' ')
    print()
#####

#####
def checkAnswer(random_num: str, usrGuess: str): # returns the list of correct digits
    res = []
    for i in range(len(usrGuess)):
        if usrGuess[i] == random_num[i]:
            res.append(usrGuess[i])

    return res
#####

#####
def startGame(random_num, digits) -> None:
    cycle = 1

    while True:

        usrGuess = ''
        while True:
            # check if usrGuess is decimal and number of its digits are 4
            if usrGuess.isdecimal() and len(usrGuess) == digits: break
            else: usrGuess = input('Guess the ' + str(digits) + ' ditig number: ')
        
        if int(usrGuess) == random_num:
            if cycle == 1:
                print('\nGreat! You guessed the number in just', cycle, 'try! You\'re a Mastermind!')
            else:
                print('\nYou\'ve become a Mastermind.')
                print('It took you only', cycle, 'tries.')
            break
        else:
            res = checkAnswer(str(random_num), usrGuess)
            print('\nNot quite the number. But you did get', len(res), 'digit(s) correct!')
            print('Also these numbers in your input were correct.')
            displayCorrectNumbers(str(random_num), usrGuess)
            cycle += 1
#####

#####
def init() -> None:
    
    random_num = random.randint(1000, 10000) # playing game with four digit numbers

    startGame(random_num, 4)
#####

init()