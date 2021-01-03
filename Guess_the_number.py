import random

n = random.randint(1, 101)  # losowanie liczny przez komputer


def user_choice():  # funkcja przyjmująca dane od użytkownika oraz sprawdzająca czy podane dane są liczbą
    while True:
        user_number = input("Guess the number!: ")
        try:
            int(user_number)
            break
        except ValueError:
            str(user_number)
            print("It's not a number!")
    return user_number


def guess():    # funkcja sprawdzająca czy wprowadzona liczbna jest taka sama jak wylosowana przez komputer
    while user_choice:
        liczba = int(user_choice())
        if liczba == n:
            print("You win!")
            break
        if liczba > n:
            print("To big!")
            continue
        elif liczba < n:
            print("To small!")
            continue


guess()    # uruchomienie programu poprzez wywołanie funkcji
