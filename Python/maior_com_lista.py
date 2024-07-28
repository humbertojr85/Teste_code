s = []
soma = 0
for i in range(5):
    num = int(input(f'Digite o {i}º número: '))
    soma += num
    s.append(num)

media = soma / 5
maximo = max(s)

print(f'Os números digitados foram {s}, O maior é {maximo}, a soma de todos é {soma} e sua média é {media:.0f}')