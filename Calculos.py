import statistics    


print('Olá, essa é a sua calculadora digital, bem vindo!')
name = input('Primeiramente, digite o seu nome: ')

numbers = input('Agora, digite os números que deseja calcular média, mediana, e a moda: ')
lista = [float(i) for i in numbers.split(' ')]

# Média:
m = sum(lista) / len(lista)
print('A média dos valores escolhidos é {:.2f}!'.format(m))

# Mediana:
lista = sorted(lista)
median = len(lista) // 2

if len(lista) % 2 == 0:
    resultado = (lista[median] + lista[median - 1]) / 2
    print('A mediana dos valores escolhidos é {:.2f}!'.format(median))
else:
    print('A mediana dos valores escolhidos é {0}'.format(lista[median]))

# Moda:
statistics.mode(lista)
moda = statistics.mode(lista)
print('A moda dos valores escolhidos é {:.2f}'.format(moda))
