def lin(m=0,a=21):
     print('-~'*a)
     if m!=0:
          print(f'{m:^42}')
          print('-~'*a)

def leiaint(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Não é número! Tente novamente.')

def leiafloat(msg):
     while True:
          try:
               a=float(input(msg))
               if a == '':
                    a=0
                    return a
          except:
                    print('Não é número! Tente novamente.')
          
def opcoes(*a):
     for pos, opcao in enumerate(a):
          print(f'[{pos+1}] - {opcao}')