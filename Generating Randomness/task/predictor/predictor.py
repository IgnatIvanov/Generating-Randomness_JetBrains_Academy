import numpy as np


data = ''
while True:
    print('Print a random string containing 0 or 1:', sep='\n')
    user_in = str(input())
    for digit in user_in:
        if digit == '0' or digit == '1':
            data += digit

    if len(data) > 99:
        break
    else:
        print('Current data length is {}, {} symbols left'.format(len(data), 100 - len(data)))

print()
print('Final data string:', data, sep='\n')
print()

zeros = dict()
ones = dict()
# sums = dict()

for pointer in range(0, len(data) - 3):
    if data[pointer + 3] == '0':
        triad = data[pointer] + data[pointer + 1] + data[pointer + 2]
        zeros.setdefault(triad, 0)
        zeros[triad] += 1
    elif data[pointer + 3] == '1':
        triad = data[pointer] + data[pointer + 1] + data[pointer + 2]
        ones.setdefault(triad, 0)
        ones[triad] += 1

max_triad = ''
max_sum = 0

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            triad = str(x) + str(y) + str(z)
            zeros.setdefault(triad, 0)
            ones.setdefault(triad, 0)
            # print('{}{}{}: {},{}'.format(x, y, z, zeros.get(triad), ones.get(triad)))
            current_sum = zeros.get(triad) + ones.get(triad)
            if current_sum > max_sum:
                max_triad = triad

print(r'''You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!
''')

capital = 1000
while True:
    print('Print a random string containing 0 or 1:')

    test_str = str(input())
    skip_flag = False
    if test_str == 'enough':  # Exiting the game
        print('Game over!')
        break

    for letter in test_str:
        if letter != '0' and letter != '1':
            skip_flag = True
            break

    if skip_flag:
        continue

    predicted_str = ''
    predicted_str += max_triad

    for i in range(2, len(test_str) - 1):
        triad = test_str[i - 2] + test_str[i - 1] + test_str[i]
        next_bit = ''
        if zeros.get(triad) >= ones.get(triad):
            next_bit = '0'
        else:
            next_bit = '1'
        predicted_str += next_bit

    print('prediction', predicted_str, sep='\n')

    correct_n = 0
    for i in range(3, len(test_str)):
        if test_str[i] == predicted_str[i]:
            correct_n += 1

    accuracy = correct_n / (len(test_str) - 3) * 100
    accuracy = int(accuracy * 100) / 100
    print('Computer guessed right {} out of {} symbols ({} %)'.format(correct_n, len(test_str) - 3, accuracy))
    capital -= correct_n
    capital += len(test_str) - 3 - correct_n
    print('Your capital is now ${}'.format(capital))
    print()
