def divisao_por_zero(numerador, denominador): 
    try:
        resultado = numerador / denominador
        return resultado
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero!")
        return None

print("\nTestando divisao_por_zero\n")
print(f"10 / 2 = {divisao_por_zero(10, 2)}")
print(f"5 / 0 = {divisao_por_zero(5, 0)}")
print(f"20 / 4 = {divisao_por_zero(20, 4)}")
print(f"100 / 0 = {divisao_por_zero(100, 0)}")