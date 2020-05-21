string = input('Enter: ')

if len(string)>=2:
    print(f'{string[:2]}{string[-2:]}')
    exit()

print('Empty String')