def calcular_troco():
    
        total_compra = float(input("Digite o valor total da compra: "))
        valor_pago = float(input("Digite o valor pago: "))

        if valor_pago < total_compra:
            print("Erro: O valor pago é insuficiente para cobrir o total da compra.")
        elif valor_pago == total_compra:
            print("Troco: R$ 0.00")
        else:
            troco = valor_pago - total_compra
            print(f"Troco: R$ {troco:.2f}")
calcular_troco()