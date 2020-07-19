secret_word = 'LOL'
guess = ''
guess_count = 0
guess_limit = 4
out_of_guess = False

while guess != secret_word and not (out_of_guess):
    if guess_count < guess_limit:
        guess = input('Введите секретное слово: ')
        guess_count += 1
        out_limit = guess_limit-guess_count
        if out_limit == 0:
            print('попытки закончились')
        elif guess == secret_word:
            print('ПОБЕДА! Вы угадали слово!')

        else:
            print('У вас осталось '+ str(out_limit) + ' попыток!')
    else:
        out_of_guess = True

