 #Conversor de Moeda
valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

#Conversão
valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro

#Exibição
print(f"Valor em reais: R$ {valor_em_reais:.2f}")
print(f"Valor em dólares: US$ {valor_em_dolar:.2f}")
print(f"Valor em euros: € {valor_em_euro:.2f}")