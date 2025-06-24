class IdadeInvalidaException(Exception):
    def __init__(self, idade):
        self.idade = idade
        super().__init__(f"Idade inválida: {idade}. A idade deve estar entre 18 e 100 anos.")

def verificar_idade(idade):
    if not (18 <= idade <= 100):
        raise IdadeInvalidaException(idade)
    else:
        print(f"Idade {idade} é válida.")


print("\nTestando verificar_idade com exceção personalizada")
try:
    verificar_idade(25)
    verificar_idade(17)
except IdadeInvalidaException as e:
    print(e)

try:
    verificar_idade(101)
except IdadeInvalidaException as e:
    print(e)

try:
    verificar_idade(50)
except IdadeInvalidaException as e:
    print(e)