# NUMBERS = "481597632"
# NUMBERS = "483579612"
NUMBERS = "99911970693140134989872398"

# brute force - szka wszystkich podziałów numbers takich że x * y = z.
# numbers jest dzielone w pozycjach i,j na x,y,z
def processNumbers(numbers) -> list:
    for i in range(1, len(numbers)-1):
        x, reszta = numbers[:i], numbers[i:]
        for j in range(1, len(reszta)):
            y, z = reszta[:j], reszta[j:]
            if int(x) * int(y) == int(z):
                return(x, y, z)

        
numbers = NUMBERS

for _ in range(len(numbers)):
    wynik = processNumbers(numbers)
    if wynik:
        print(f'Podane cyfry:   {NUMBERS}')
        print(f'Aktualny układ: {numbers}')
        print(f'{wynik[0]} * {wynik[1]} = {wynik[2]}')

    numbers = numbers[1:] + numbers[0]

