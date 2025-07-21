def soma_numeros_pares():

    N = int(input("Digite um número inteiro positivo N: "))

    if N <= 0:
      print("Por favor, digite um número inteiro positivo.")
      return

    soma = 0
    for numero in range(2, N + 1, 2):
      soma += numero

    print(f"Soma dos números pares: {soma}")


soma_numeros_pares()