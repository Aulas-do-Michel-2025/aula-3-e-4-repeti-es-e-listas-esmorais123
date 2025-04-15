n = int(input("Digite um número: "))
i = 1
f = n

while i < n:
    f *= n - i
    i = i + 1

print(f'O fatorial de {n} é {f}')
