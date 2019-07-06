#from easygui import 
from os      import system, name
from random  import sample
from time    import strftime


def limpar():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

while True:
    limpar()
    loto = []
    acertados = []

    loteria1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']

    loteria2 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']

    escolhidos = sample(loteria1, 6)

    print('|---------------------|')
    print('| + Loteria Federal + |')
    print('|---------------------|\n')  
    print(escolhidos)

    while len(loto) != 6:
        if loto == []:
            n = str(input('Digite um número entre 1-60: '))

        else:
            n = str(input(f'Digite um número entre 1-60 \nexceto {loto}: '))

        if len(n) == 1:
                n = f'0{n}'

        if n != '' and int(n) > 0 and int(n) < 61 and n not in loto:
            loto.append(n)

        limpar()

    for i in loto:
        if i in escolhidos:
            acertados.append(i)

    print(f"Números escolhidos:  {' '.join(loto)}"  )
    print(f"Números sorteados :  {' '.join(escolhidos)}")
    print(f"Números acertados :  {' '.join(acertados)}")

    for i in loto:
        loteria1[loteria1.index(i)] = 'XX'

    for i in escolhidos:
        loteria2[loteria2.index(i)] = 'XX'

    print('\n +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria1[ 0]} - {loteria1[ 1]} - {loteria1[ 2]} - {loteria1[ 3]} : {loteria1[ 4]} - {loteria1[ 5]} - {loteria1[ 6]} - {loteria1[ 7]} - {loteria1[ 8]} - {loteria1[ 9]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria1[10]} - {loteria1[11]} - {loteria1[12]} - {loteria1[13]} : {loteria1[14]} - {loteria1[15]} - {loteria1[16]} - {loteria1[17]} - {loteria1[18]} - {loteria1[19]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria1[20]} - {loteria1[21]} - {loteria1[22]} - {loteria1[23]} : {loteria1[24]} - {loteria1[25]} - {loteria1[26]} - {loteria1[27]} - {loteria1[28]} - {loteria1[29]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria1[30]} - {loteria1[31]} - {loteria1[32]} - {loteria1[33]} : {loteria1[34]} - {loteria1[35]} - {loteria1[36]} - {loteria1[37]} - {loteria1[38]} - {loteria1[39]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria1[40]} - {loteria1[41]} - {loteria1[42]} - {loteria1[43]} : {loteria1[44]} - {loteria1[45]} - {loteria1[46]} - {loteria1[47]} - {loteria1[48]} - {loteria1[49]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria1[50]} - {loteria1[51]} - {loteria1[52]} - {loteria1[53]} : {loteria1[54]} - {loteria1[55]} - {loteria1[56]} - {loteria1[57]} - {loteria1[58]} - {loteria1[59]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')

    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria2[ 0]} - {loteria2[ 1]} - {loteria2[ 2]} - {loteria2[ 3]} : {loteria2[ 4]} - {loteria2[ 5]} - {loteria2[ 6]} - {loteria2[ 7]} - {loteria2[ 8]} - {loteria2[ 9]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria2[10]} - {loteria2[11]} - {loteria2[12]} - {loteria2[13]} : {loteria2[14]} - {loteria2[15]} - {loteria2[16]} - {loteria2[17]} - {loteria2[18]} - {loteria2[19]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria2[20]} - {loteria2[21]} - {loteria2[22]} - {loteria2[23]} : {loteria2[24]} - {loteria2[25]} - {loteria2[26]} - {loteria2[27]} - {loteria2[28]} - {loteria2[29]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria2[30]} - {loteria2[31]} - {loteria2[32]} - {loteria2[33]} : {loteria2[34]} - {loteria2[35]} - {loteria2[36]} - {loteria2[37]} - {loteria2[38]} - {loteria2[39]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria2[40]} - {loteria2[41]} - {loteria2[42]} - {loteria2[43]} : {loteria2[44]} - {loteria2[45]} - {loteria2[46]} - {loteria2[47]} - {loteria2[48]} - {loteria2[49]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+')
    print(f' : {loteria2[50]} - {loteria2[51]} - {loteria2[52]} - {loteria2[53]} : {loteria2[54]} - {loteria2[55]} - {loteria2[56]} - {loteria2[57]} - {loteria2[58]} - {loteria2[59]} :')
    print(' +----+----+----+----+----+----+----+----+----+----+\n')

    input()