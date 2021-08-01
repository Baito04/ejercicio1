class Basico:
    def num_n(self, n=10):
        print('N del 1 al', n)
        for i in range(1, n+1):
            if i == n:
                print(str(i) + '.')
            else: print(str(i) + ', ' ,end='')

    def multiplo(self, num=36):
        print('Multiplos de', num, '\n0, ', end='')
        for i in range(1, num+1):
            if (num * i) % i == 0:
                if i == numero:
                    print(str(i*num) + '.')
                else: print(str(i*num) + ', ' ,end='')

    def divisores_numeros(self, num=42):
        print('Divisores de', num)
        for i in range(1, num+1):
            if num % i == 0:
                if i == num:
                    print(str(i) + '.')
                else: print(str(i) + ', ' ,end='')

    def primo(self, num=7):
        primo = False
        print('Número primo')
        if num >= 2:
            for i in range(2, num):
                if num % i == 0:
                    print(' -No es primo')
                    primo = True
                    break
            if not primo:
                print(' -Es primo')
        else:
            print(' -No es primo')

    def perfecto(self, num=6):
        print('Número perfecto')
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if num == sum:
            print(' -El número es perfecto')
        else:
            print(' -El número no es perfecto')
