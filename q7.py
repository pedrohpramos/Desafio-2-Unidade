def contador_de_vogais():
 
  frase = input("Digite uma frase: ")

  
  frase_minuscula = frase.lower()

  vogais = "aeiou"
  contagem_vogais = 0

  for i in frase_minuscula:
    if i in vogais:
      contagem_vogais += 1

  print(f"A frase contém {contagem_vogais} vogais.")


contador_de_vogais()