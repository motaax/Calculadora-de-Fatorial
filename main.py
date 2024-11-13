def calcula_fatorial(n):
    if n < 0:
        return "Erro: fatorial não definido para números negativos"
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

fatorial_de_5 = calcula_fatorial(5)
print("O fatorial de 5 é:", fatorial_de_5)