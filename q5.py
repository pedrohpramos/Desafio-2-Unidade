def calcular_imc():
 

    peso = float(input("Digite seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    if peso <= 0 or altura <= 0:
      print("Peso e altura devem ser valores positivos.")
      return

    imc = peso / (altura ** 2)
    print(f"\nSeu IMC é: {imc:.2f}")

    if imc < 18.5:
      print("Classificação: Abaixo do peso")
    elif 18.5 <= imc <= 24.9:
      print("Classificação: Peso normal")
    elif 25.0 <= imc <= 29.9:
      print("Classificação: Sobrepeso")
    elif 30.0 <= imc <= 34.9:
      print("Classificação: Obesidade grau 1")
    elif 35.0 <= imc <= 39.9:
      print("Classificação: Obesidade grau 2")
    else:
      print("Classificação: Obesidade grau 3 ou mais (Obesidade Mórbida)")



calcular_imc()