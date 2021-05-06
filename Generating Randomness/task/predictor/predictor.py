# print('Hello, World!')
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

print('Final data string:', data, sep='\n')
print()

zeros = dict()
ones = dict()

for pointer in range(0, len(data) - 3):
    if data[pointer + 3] == '0':
        triad = data[pointer] + data[pointer + 1] + data[pointer + 2]
        zeros.setdefault(triad, 0)
        zeros[triad] += 1
    elif data[pointer + 3] == '1':
        triad = data[pointer] + data[pointer + 1] + data[pointer + 2]
        ones.setdefault(triad, 0)
        ones[triad] += 1

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            triad = str(x) + str(y) + str(z)
            zeros.setdefault(triad, 0)
            ones.setdefault(triad, 0)
            print('{}{}{}: {},{}'.format(x, y, z, zeros.get(triad), ones.get(triad)))
