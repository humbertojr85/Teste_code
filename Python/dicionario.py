#funções:
def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['Maio'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/ len(n)

    return r

#função main
def main():
    resp = notas(4.5, 6, 9, 10)
    print(resp)
    for r in resp:
        print(r, resp[r])

#inicio do main
main()