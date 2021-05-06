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
